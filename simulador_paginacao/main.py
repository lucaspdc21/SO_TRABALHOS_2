import argparse

from algortimos.fifo import FIFO
from algortimos.lru import LRU
from algortimos.opt import Otimo
from algortimos.clock import Clock
from algortimos.segunda_chance import SegundaChance
from algortimos.nru import NRU
from algortimos.lfu import LFU
from algortimos.mfu import MFU
from src.simulador import Simulator

def main():

    parser = argparse.ArgumentParser()
    
    parser.add_argument("--algo")
    parser.add_argument("--frames")
    parser.add_argument("--trace")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    algoritmos_map = {
        'lru': LRU,
        'fifo': FIFO,
        'otimo': Otimo,
        'clock': Clock,
        'segunda_chance': SegundaChance,
        'nru': NRU,
        'lfu': LFU,
        'mfu': MFU,
    }

    algoritmo_paginacao = algoritmos_map.get(args.algo.lower())
    
    if algoritmo_paginacao is None:
        print(f"Algoritmo de paginação desconhecido: {args.algo}")
        return
    
    Simulator(algorithm= algoritmo_paginacao(int(args.frames)), trace_file=args.trace).run().print_report(args.algo)

if __name__ == "__main__":
    main()