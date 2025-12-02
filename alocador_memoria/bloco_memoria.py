class BlocoMemoria:
    """Representa um bloco de memória no simulador.
    
    Attributes:
        id: Identificador do processo que ocupa o bloco (None se livre).
        tamanho: Tamanho do bloco em bytes.
        livre: Indica se o bloco está livre ou ocupado.
    """
    
    def __init__(self, id_processo, tamanho, livre=True):
        """Inicializa um bloco de memória.
        
        Args:
            id_processo: ID do processo (None se livre).
            tamanho: Tamanho do bloco em bytes.
            livre: Se o bloco está livre (padrão: True).
        """
        self.id = id_processo    
        self.tamanho = tamanho   
        self.livre = livre       
    
    def __repr__(self):
        """Retorna uma representação string do bloco."""
        status = "Livre" if self.livre else f"ID={self.id}"
        return f"[{status}, {self.tamanho}B]"