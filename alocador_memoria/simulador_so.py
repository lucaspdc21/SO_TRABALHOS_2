from bloco_memoria import BlocoMemoria
from estrategias_alocacao import FirstFit, BestFit, WorstFit

# Mapeamento dos algoritmos
MAP_STRATEGIES = {
    "first": FirstFit(),
    "best": BestFit(),
    "worst": WorstFit()
}

# Caracteres para visualização
CHAR_LIVRE = '.'
CHAR_OCUPADO = '#'

class SimuladorSO:
    """Simulador de Sistema Operacional com gerenciamento de memória.
    
    Implementa algoritmos de alocação (First Fit, Best Fit, Worst Fit)
    e gerenciamento de fragmentação externa
    """
    
    # Inicialização do simulador com memória vazia
    def __init__(self):
        
        self.memoria = []  # Lista de objetos da classe blocoMemoria 
        self.tamanho_total = 0  # Tamanho total da memória
        self.next_id = 1  # IDs únicos para os processos      

    # Inicializa a memória com um único bloco livre 
    def init(self, tamanho):
        """Args:
            tamanho: Tamanho total da memória em bytes.
        """
        self.tamanho_total = tamanho
        self.memoria = [BlocoMemoria(None, tamanho, livre=True)]
        self.next_id = 1
        print(f"Memória inicializada com {tamanho} bytes.")

    # Executa a alocação de memória e divide o bloco (split), o espaço que sobra vira um novo bloco
    def alloc(self, tamanho, alg_nome):
        alg_nome = alg_nome.lower()

        estrategia = MAP_STRATEGIES.get(alg_nome)
        if not estrategia:
            print(f"Erro: Algoritmo '{alg_nome}' inválido.")
            return

        idx = estrategia.escolher_bloco(self.memoria, tamanho)

        if idx == -1:
            print(f"Erro: Memória insuficiente para alocar {tamanho}B ({alg_nome}).")
            return

        bloco_atual = self.memoria[idx]
        sobra = bloco_atual.tamanho - tamanho
        pid = self.next_id
        self.next_id += 1

        bloco_atual.id = pid
        bloco_atual.tamanho = tamanho
        bloco_atual.livre = False

        if sobra > 0:
            self.memoria.insert(idx + 1, BlocoMemoria(None, sobra, livre=True))

        print(f"Bloco alocado: ID {pid} ({tamanho} bytes) usando {alg_nome}.")


    # Libera memória de um processo e faz merge de blocos adjacentes.
    def free_id(self, id_alvo):
        """Args:
            id_alvo: ID do processo a ser liberado.
        """
        encontrado = self._liberar_bloco(id_alvo)
        
        if not encontrado:
            print(f"Erro: Processo ID {id_alvo} não encontrado.")
            return

        self._merge_blocos_livres()
    
    # Libera o bloco de memória de um processo.
    def _liberar_bloco(self, id_alvo):
        """Args:
            id_alvo: ID do processo a liberar.
            
        Returns:
            True se o processo foi encontrado e liberado, False caso contrário.
        """

        for bloco in self.memoria:
            if not bloco.livre and bloco.id == id_alvo:
                bloco.livre = True
                bloco.id = None
                print(f"Processo {id_alvo} liberado.")
                return True
        return False
    
    # Faz merge de blocos livres adjacentes para reduzir fragmentação externa
    def _merge_blocos_livres(self):
        
        i = 0
        while i < len(self.memoria) - 1:
            atual = self.memoria[i]
            proximo = self.memoria[i+1]
            
            if atual.livre and proximo.livre:
                atual.tamanho += proximo.tamanho
                self.memoria.pop(i+1)
            else:
                i += 1

    # Função que gera e exibe o mapa visual da memória
    def show(self):
        
        if not self.memoria:
            print("Memória não inicializada.")
            return

        print(f"\nMapa de Memória ({self.tamanho_total} bytes)")
        print("-" * 60)
        
        linha_uso, linha_ids, info_blocos = self._gerar_visualizacao()

        print(f"[{linha_uso}]")
        print(f"[{linha_ids}]")
        print("-" * 60)
        print("Blocos ativos: " + " | ".join(info_blocos))
    
    # Função que gera as linhas de visualização da memória.
    def _gerar_visualizacao(self):
        """Returns:
            Tupla com (linha_uso, linha_ids, info_blocos).
        """
        linha_uso = ""
        linha_ids = ""
        endereco_atual = 0
        info_blocos = []

        for bloco in self.memoria:
            char_uso = CHAR_LIVRE if bloco.livre else CHAR_OCUPADO
            char_id = CHAR_LIVRE if bloco.livre else str(bloco.id)[-1] 
            
            linha_uso += char_uso * bloco.tamanho
            linha_ids += char_id * bloco.tamanho
            
            if not bloco.livre:
                info_blocos.append(f"[id={bloco.id}] @{endereco_atual} +{bloco.tamanho}B (usado={bloco.tamanho}B)")
            
            endereco_atual += bloco.tamanho
        
        return linha_uso, linha_ids, info_blocos

    # Exibe estatísticas de uso e fragmentação da memória
    def stats(self):
        livre = sum(b.tamanho for b in self.memoria if b.livre)
        ocupado = self.tamanho_total - livre
        buracos = sum(1 for b in self.memoria if b.livre)
        pct_uso = (ocupado / self.tamanho_total) * 100 if self.tamanho_total > 0 else 0

        print("== Estatísticas ==")
        print(f"Tamanho total: {self.tamanho_total} bytes")
        print(f"Ocupado: {ocupado} bytes | Livre: {livre} bytes")
        print(f"Buracos (fragmentação externa): {buracos}")
        print(f"Uso efetivo: {pct_uso:.2f}%")