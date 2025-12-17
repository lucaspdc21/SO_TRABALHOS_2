"""Simulador de Gerenciamento de Memória

Simulação do processo de alocação iterativa de memória
Utilização dos algoritmos de alocação First Fit, Best Fit e Worst Fit
"""

import sys
from simulador_so import SimuladorSO

# Comandos disponíveis
CMD_INIT = "init"
CMD_ALLOC = "alloc"
CMD_FREE = "freeid"
CMD_SHOW = "show"
CMD_STATS = "stats"
CMD_EXIT = ["sair", "exit"]


# Função principal do simulador
def main():

    sim = SimuladorSO()
    print("Simulador de Memória Modularizado.")
    print("Comandos: init <tam>, alloc <tam> <alg>, freeid <id>, show, stats, sair")
    
    while True:
        try:
            entrada_raw = input("> ").strip()
            if not entrada_raw: 
                continue
            
            entrada = entrada_raw.split()
            cmd = entrada[0].lower()
            
            if cmd in CMD_EXIT:
                break
            
            processar_comando(sim, cmd, entrada)
                
        except IndexError:
            print("Erro: Faltam argumentos para o comando.")
        except ValueError:
            print("Erro: Argumento deve ser um número inteiro.")
        except Exception as e:
            print(f"Erro inesperado: {e}")

def processar_comando(sim, cmd, entrada):
    """Processa um comando do usuário.
    
    Args:
        sim: Instância do SimuladorSO.
        cmd: Comando a ser executado.
        entrada: Lista com o comando e seus argumentos.
    """
    if cmd == CMD_INIT:
        if len(entrada) < 2: 
            raise IndexError
        sim.init(int(entrada[1]))
        
    elif cmd == CMD_ALLOC:
        if len(entrada) < 2: 
            raise IndexError
        tamanho = int(entrada[1])
        alg = entrada[2] if len(entrada) > 2 else "first"
        sim.alloc(tamanho, alg)
        
    elif cmd == CMD_FREE:
        if len(entrada) < 2: 
            raise IndexError
        sim.free_id(int(entrada[1]))
        
    elif cmd == CMD_SHOW:
        sim.show()
        
    elif cmd == CMD_STATS:
        sim.stats()
        
    else:
        print(f"Comando desconhecido: {cmd}")

if __name__ == "__main__":
    main()