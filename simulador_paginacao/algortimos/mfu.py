from typing import List
from .base import Page, AlgoritmoSubstituicaoGenerico

class MFU(AlgoritmoSubstituicaoGenerico):
    def selecionar_alvo(self, future_references: List[int]) -> Page:
        # Retorna a página menos recentemente usada
        alvo = min(self.memory, key=lambda p: (p.frequency, -p.load_time))
        return alvo

    def atualizar_uso(self, page: Page, is_hit: bool):
        page.frequency += 1
        page.last_access_time = self.current_time