from typing import List
from .base import Page, AlgoritmoSubstituicaoGenerico


class Clock(AlgoritmoSubstituicaoGenerico):
    def __init__(self, num_frames: int):
        super().__init__(num_frames)
        self.ponteiro = 0
    
    def selecionar_alvo(self, future_references: List[int]) -> Page:
        while True:
            # Resolve bug fora dos limites
            if self.ponteiro >= len(self.memory):
                self.ponteiro = 0
            page = self.memory[self.ponteiro]
            if page.referenced:
                # Dá uma "segunda chance" e avança o ponteiro
                page.referenced = False
                self.ponteiro = (self.ponteiro + 1) % len(self.memory)
            else: 
                alvo = page
                self.ponteiro = (self.ponteiro + 1) % len(self.memory)
                return alvo
            
    def atualizar_uso(self, page: Page, is_hit: bool):
        page.referenced = True