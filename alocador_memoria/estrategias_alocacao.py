from abc import ABC, abstractmethod

# Classe abstrata que funciona como uma interface para as estratégias de alocação de memória
class EstrategiaAlocacao(ABC):
    """Interface para estratégias de alocação de memória"""

    @abstractmethod
    def escolher_bloco(self, memoria, tamanho):
        pass

# Implementação de classes conctretas para cada algoritmo de alocação

# Algoritmo First Fit
class FirstFit(EstrategiaAlocacao):
    def escolher_bloco(self, memoria, tamanho):
        for i, bloco in enumerate(memoria):
            if bloco.livre and bloco.tamanho >= tamanho:
                return i
        return -1
    
# Algoritmo Best Fit
class BestFit(EstrategiaAlocacao):
    def escolher_bloco(self, memoria, tamanho):
        candidatos = [
            (i, b) for i, b in enumerate(memoria)
            if b.livre and b.tamanho >= tamanho
        ]
        if not candidatos:
            return -1

        candidatos.sort(key=lambda x: x[1].tamanho - tamanho)
        return candidatos[0][0]

# Algoritmo Worst Fit
class WorstFit(EstrategiaAlocacao):
    def escolher_bloco(self, memoria, tamanho):
        candidatos = [
            (i, b) for i, b in enumerate(memoria)
            if b.livre and b.tamanho >= tamanho
        ]
        if not candidatos:
            return -1

        candidatos.sort(key=lambda x: x[1].tamanho - tamanho, reverse=True)
        return candidatos[0][0]


