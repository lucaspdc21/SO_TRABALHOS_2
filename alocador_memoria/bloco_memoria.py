class BlocoMemoria:
    """Representa um bloco de memória no simulador.
    
    Atributos:
        id: Identificador do processo que ocupa o bloco (None se o bloco estiver livre).
        tamanho: Tamanho do bloco em bytes.
        livre: Especifica se o bloco está livre ou ocupado por algum processo (padrão: True).
    """
    
    # Método de inicialização de um bloco de memória com os argumentos: id_processo, tamanho e livre
    def __init__(self, id_processo, tamanho, livre=True):  

        self.id = id_processo    
        self.tamanho = tamanho   
        self.livre = livre       
    
    # Retorna uma representação do bloco na forma de uma string
    def __repr__(self):
        
        status = "Livre" if self.livre else f"ID={self.id}"
        return f"[{status}, {self.tamanho}B]"