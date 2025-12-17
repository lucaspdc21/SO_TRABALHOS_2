# SO_TRABALHOS_2

## Simulador de Gerenciamento de Memória

Este projeto implementa um simulador interativo de alocação de memória com suporte a diferentes algoritmos.

### Funcionalidades

- **Algoritmos de Alocação**: First Fit, Best Fit, Worst Fit
- **Visualização de Memória**: Mapa visual mostrando blocos livres e ocupados
- **Estatísticas**: Fragmentação e uso de memória
- **Merge Automático**: Combina blocos livres adjacentes

### Como Usar

```bash
cd alocador_memoria
python3 main.py
```

### Comandos Disponíveis

- `init <tamanho>` - Inicializa a memória com o tamanho especificado
- `alloc <tamanho> <algoritmo>` - Aloca memória (algoritmos: first, best, worst)
- `freeid <id>` - Libera memória do processo especificado
- `show` - Exibe o mapa visual da memória
- `stats` - Exibe estatísticas de uso e fragmentação
- `sair` ou `exit` - Sai do simulador

### Estrutura do Código

- `bloco_memoria.py` - Classe que representa um bloco de memória
- `simulador_so.py` - Lógica principal de gerenciamento de memória
- `main.py` - Interface de linha de comando
