import sys
from simulador_so import SimuladorSO

def main():
    sim = SimuladorSO()
    print("Simulador de Memória Modularizado.")
    print("Comandos: init <tam>, alloc <tam> <alg>, freeid <id>, show, stats, sair")
    
    while True:
        try:
            # Lê a entrada do usuário
            entrada_raw = input("> ").strip()
            if not entrada_raw: continue
            
            entrada = entrada_raw.split()
            cmd = entrada[0].lower()
            
            if cmd in ["sair", "exit"]:
                break
                
            elif cmd == "init":
                if len(entrada) < 2: raise IndexError
                sim.init(int(entrada[1]))
                
            elif cmd == "alloc":
                if len(entrada) < 2: raise IndexError
                tamanho = int(entrada[1])
                alg = entrada[2] if len(entrada) > 2 else "first"
                sim.alloc(tamanho, alg)
                
            elif cmd == "freeid":
                if len(entrada) < 2: raise IndexError
                sim.free_id(int(entrada[1]))
                
            elif cmd == "show":
                sim.show()
                
            elif cmd == "stats":
                sim.stats()
                
            else:
                print(f"Comando desconhecido: {cmd}")
                
        except IndexError:
            print("Erro: Faltam argumentos para o comando.")
        except ValueError:
            print("Erro: Argumento deve ser um número inteiro.")
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()