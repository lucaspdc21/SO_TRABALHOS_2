from abc import ABC, abstractmethod
from typing import List, Optional
from src.models import Page

class AlgoritmoSubstituicaoGenerico(ABC):
    def __init__(self, num_frames: int):
        self.num_frames = num_frames
        self.memory: List[Page] = []  # Mémoria física a ser peenchida
        self.current_time = 0         # Clock para LRU/FIFO

    def acessar_pagina(self, page_id: int, future_references: List[int] = None) -> bool:
        self.current_time += 1

        # Verificando se a página já está na memória
        page = self.verificar_pagina_memoria(page_id)
        if page:
            self.atualizar_uso(page, is_hit=True)
            return False # Não houve fault
        
        # Entrando no caso em que ela não está na memória
        new_page = Page(id=page_id, load_time=self.current_time)
        
        # Verificando se há espaço na memória para a alocação
        if len(self.memory) < self.num_frames:
            self.memory.append(new_page)
            self.atualizar_uso(new_page, is_hit=False)
        else:
            pagina_alvo = self.selecionar_alvo(future_references)
            if pagina_alvo in self.memory:
                self.memory.remove(pagina_alvo)
            
            self.memory.append(new_page)
            self.atualizar_uso(new_page, is_hit=False)
            return True 
            
        return True

    def verificar_pagina_memoria(self, page_id: int) -> Optional[Page]:
        for page in self.memory:
            if page.id == page_id:
                return page
        return None

    @abstractmethod
    def selecionar_alvo(self, future_references: List[int]) -> Page:
        pass

    @abstractmethod
    def atualizar_uso(self, page: Page, is_hit: bool):
        pass