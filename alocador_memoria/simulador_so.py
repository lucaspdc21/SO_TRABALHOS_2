from bloco_memoria import BlocoMemoria

class SimuladorSO:
    def __init__(self):
        self.memoria = []      
        self.tamanho_total = 0
        self.next_id = 1       

    def init(self, tamanho):
        """Inicializa a memória com um único bloco livre."""
        self.tamanho_total = tamanho
        self.memoria = [BlocoMemoria(None, tamanho, livre=True)]
        self.next_id = 1
        print(f"Memória inicializada com {tamanho} bytes.")

    def choose_block(self, tamanho, alg):
        """Seleciona o índice do bloco ideal baseado no algoritmo."""
        candidatos = [
            i for i, b in enumerate(self.memoria) 
            if b.livre and b.tamanho >= tamanho
        ]
        
        if not candidatos:
            return -1

        if alg == 'first':
            return candidatos[0]
            
        elif alg == 'best':
            candidatos.sort(key=lambda i: self.memoria[i].tamanho - tamanho)
            return candidatos[0]
            
        elif alg == 'worst':
            candidatos.sort(key=lambda i: self.memoria[i].tamanho - tamanho, reverse=True)
            return candidatos[0]
            
        return -1

    def alloc(self, tamanho, alg_nome):
        """Executa a alocação e divide o bloco (split)."""
        alg = alg_nome.lower()
        idx = self.choose_block(tamanho, alg)
        
        if idx == -1:
            print(f"Erro: Memória insuficiente para alocar {tamanho}B ({alg}).")
            return

        bloco_atual = self.memoria[idx]
        sobra = bloco_atual.tamanho - tamanho
        pid = self.next_id
        self.next_id += 1

        bloco_atual.id = pid
        bloco_atual.tamanho = tamanho
        bloco_atual.livre = False

        if sobra > 0:
            novo_bloco = BlocoMemoria(None, sobra, livre=True)
            self.memoria.insert(idx + 1, novo_bloco)
            
        print(f"Bloco alocado: ID {pid} ({tamanho} bytes) usando {alg}.")

    def free_id(self, id_alvo):
        """Libera memória e faz o merge de vizinhos livres."""
        encontrado = False
        for bloco in self.memoria:
            if not bloco.livre and bloco.id == id_alvo:
                bloco.livre = True
                bloco.id = None
                encontrado = True
                print(f"Processo {id_alvo} liberado.")
                break
        
        if not encontrado:
            print(f"Erro: Processo ID {id_alvo} não encontrado.")
            return

        i = 0
        while i < len(self.memoria) - 1:
            atual = self.memoria[i]
            proximo = self.memoria[i+1]
            
            if atual.livre and proximo.livre:
                atual.tamanho += proximo.tamanho
                self.memoria.pop(i+1)
            else:
                i += 1

    def show(self):
        """Gera o mapa visual."""
        if not self.memoria:
            print("Memória não inicializada.")
            return

        print(f"\nMapa de Memória ({self.tamanho_total} bytes)")
        print("-" * 60)
        
        linha_uso = ""
        linha_ids = ""
        endereco_atual = 0
        info_blocos = []

        for bloco in self.memoria:
            char_uso = '.' if bloco.livre else '#'
            char_id = '.' if bloco.livre else str(bloco.id)[-1] 
            
            linha_uso += char_uso * bloco.tamanho
            linha_ids += char_id * bloco.tamanho
            
            if not bloco.livre:
                info_blocos.append(f"[id={bloco.id}] @{endereco_atual} +{bloco.tamanho}B (usado={bloco.tamanho}B)")
            
            endereco_atual += bloco.tamanho

        print(f"[{linha_uso}]")
        print(f"[{linha_ids}]")
        print("-" * 60)
        print("Blocos ativos: " + " | ".join(info_blocos))

    def stats(self):
        """Exibe estatísticas de fragmentação."""
        livre = sum(b.tamanho for b in self.memoria if b.livre)
        ocupado = self.tamanho_total - livre
        buracos = sum(1 for b in self.memoria if b.livre)
        pct_uso = (ocupado / self.tamanho_total) * 100 if self.tamanho_total > 0 else 0

        print("== Estatísticas ==")
        print(f"Tamanho total: {self.tamanho_total} bytes")
        print(f"Ocupado: {ocupado} bytes | Livre: {livre} bytes")
        print(f"Buracos (fragmentação externa): {buracos}")
        print(f"Uso efetivo: {pct_uso:.2f}%")