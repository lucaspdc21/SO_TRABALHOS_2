class Page:
    def __init__(self, id, referenced=False, modified=False, last_access_time=0, frequency=0, load_time=0):
        self.id = int(id)
        self.referenced = referenced      # Bit R
        self.modified = modified          # Bit M
        self.last_access_time = last_access_time
        self.frequency = frequency
        self.load_time = load_time

    def __repr__(self):
        # Facilita a visualização no print()
        return f"Page(id={self.id}, R={self.referenced}, M={self.modified})"

    def __eq__(self, other):
        # Permite comparar se duas páginas são iguais pelo ID (útil para listas)
        if isinstance(other, Page):
            return self.id == other.id
        return False

class Statistics:
    """Coleta métricas da simulação."""
    def __init__(self):
        self.total_references = 0
        self.page_faults = 0
        self.evictions = 0

    @property
    def fault_rate(self):
        if self.total_references == 0:
            return 0.0
        return (self.page_faults / self.total_references) * 100

    def __str__(self):
        return (
            f"Referências: {self.total_references}\n"
            f"Faltas de página: {self.page_faults}\n"
            f"Taxa de faltas: {self.fault_rate:.2f}%\n"
            f"Evicções: {self.evictions}"
        )