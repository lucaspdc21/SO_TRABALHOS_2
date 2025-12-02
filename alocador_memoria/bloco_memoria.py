class BlocoMemoria:
    def __init__(self, id_processo, tamanho, livre=True):
        self.id = id_processo    
        self.tamanho = tamanho   
        self.livre = livre       
    
    def __repr__(self):
        status = "Livre" if self.livre else f"ID={self.id}"
        return f"[{status}, {self.tamanho}B]"