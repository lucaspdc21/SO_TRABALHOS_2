from typing import List
from base import Page
from base import AlgoritmoSubstituicaoGenerico

class LRU(AlgoritmoSubstituicaoGenerico):
    def selecionar_alvo(self, future_references: List[int]) -> Page:
        # Retorna a página menos recentemente usada
        alvo = min(self.memory, key=lambda p: p.last_access_time)
        return alvo

    def atualizar_uso(self, page: Page, is_hit: bool):
        if is_hit:
            page.last_access_time = self.current_time