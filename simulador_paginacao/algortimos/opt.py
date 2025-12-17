from typing import List
from base import Page
from base import AlgoritmoSubstituicaoGenerico

class OPT(AlgoritmoSubstituicaoGenerico):
    def selecionar_alvo(self, future_references: List[int]) -> Page:
        candidates = []
        for page in self.memory:
            if page.id in future_references:
                next_use = future_references.index(page.id)
            else:
                next_use = float('inf')  # Nunca será usado novamente
            candidates.append((next_use, page))
        alvo = max(candidates, key=lambda x: x[0])[1]
        return alvo

    def atualizar_uso(self, page: Page, is_hit: bool):
        pass