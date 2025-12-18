from typing import List
from .base import Page, AlgoritmoSubstituicaoGenerico

class NRU(AlgoritmoSubstituicaoGenerico):
    def selecionar_alvo(self, future_references: List[int]) -> Page:
        classes = {0: [], 1: [], 2: [], 3: []}
        for page in self.memory:
            r = 1 if page.referenced else 0
            m = 1 if page.modified else 0
            class_index = 2 * r + m
            classes[class_index].append(page)
        
        # Busca a primeira classe não vazia
        for i in range(4):
            if classes[i]:
                return classes[i][0]
        return self.memory[0]  

    def atualizar_uso(self, page: Page, is_hit: bool):
        page.referenced = True