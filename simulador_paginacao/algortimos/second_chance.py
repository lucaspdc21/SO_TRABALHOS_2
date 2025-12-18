from typing import List
from .base import Page, AlgoritmoSubstituicaoGenerico

class SecondChance(AlgoritmoSubstituicaoGenerico):
    def selecionar_alvo(self, future_references: List[int]) -> Page:
        while True:
            page = self.memory[0]
            if page.referenced:
                page.referenced = False
                self.memory.append(self.memory.pop(0))
            else:
                return page

    def atualizar_uso(self, page: Page, is_hit: bool):
        page.referenced = True