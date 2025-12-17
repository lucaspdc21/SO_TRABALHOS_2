from typing import List
from base import Page
from base import AlgoritmoSubstituicaoGenerico

class FIFO(AlgoritmoSubstituicaoGenerico):
    def selecionar_alvo(self, future_references: List[int]) -> Page:
        # Retorna a página mais antiga
        return self.memory[0]

    def atualizar_uso(self, page: Page, is_hit: bool):
        # FIFO não altera estado em caso de HIT, apenas no carregamento
        pass