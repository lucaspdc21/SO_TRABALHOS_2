from typing import List
from .models import Statistics
from algortimos.base import AlgoritmoSubstituicaoGenerico

class Simulator:
    def __init__(self, algorithm: AlgoritmoSubstituicaoGenerico, trace_file: str):
        self.algorithm = algorithm
        self.trace_file = trace_file 
        self.stats = Statistics()
        self.references: List[int] = []

    def load_trace(self):
        try:
            with open(self.trace_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line.isdigit():
                        self.references.append(int(line))
        except FileNotFoundError:
            print(f"Erro: Arquivo {self.trace_file} não encontrado.")
            exit(1)

    def run(self):
        self.load_trace()
        self.stats.total_references = len(self.references)

        for i, page_id in enumerate(self.references):
            future_refs = self.references[i+1:]
            is_fault = self.algorithm.acessar_pagina(page_id, future_refs)

            if is_fault:
                self.stats.page_faults += 1
                
        self.stats.evictions = max(0, self.stats.page_faults - self.algorithm.num_frames)
        return self


    def print_report(self, algo_name: str):
        # Formato exato solicitado no PDF 
        print(f"Algoritmo: {algo_name}")
        print(f"Frames: {self.algorithm.num_frames}")
        print(str(self.stats))
        print("Conjunto residente final:")
        
        print("frame_ids: ", end="")
        print(" ".join([str(i) for i in range(len(self.algorithm.memory))]))
        
        print("page_ids:  ", end="")
        print(" ".join([str(p.id) for p in self.algorithm.memory]))
        print("-" * 30)