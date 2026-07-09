### A "Matriz" de CEPs (Como a IA organiza as informações)
| Lugar / Palavra | Região (0 a 9) | Estado/Cidade (00 a 99) | Bairro/Rua (000 a 999) | O "Embedding" (O CEP Completo) |
| --- | --- | --- | --- | --- |
| 📍 Av. Paulista (São Paulo) | 0 | 13 | 001 | [0, 13, 001] (01300-001) |
| 📍 Rua Augusta (São Paulo) | 0 | 13 | 005 | [0, 13, 005] (01300-005) |
| 📍 Copacabana (Rio de Janeiro) | 2 | 20 | 001 | [2, 20, 001] (22000-001) |

---

### O Mapa de CEPs na Memória da IA (Visualização de Proximidade)

```text
[Região de SP: Começa com 013]               [Região do RJ: Começa com 220]
-----------------------------------------     ------------------------------

|   |            |   |                        |   |
|  Av. Paulista  |  Rua Augusta   | ...     | |  Copacabana    | ...       
-----------------------------------------     ------------------------------
       ▲                ▲                                    ▲
       │                │                                    │
       └───────┬────────┘                                    │
         SÃO VIZINHOS DE CEP!                      ESTÁ MUITO LONGE!
      (Distância matemática = 4)              (Distância de milhares)

```

---

### O Fluxo da Busca por Embedding

```text
1. VOCÊ DIGITA: ───► "Quero um lugar perto da Paulista"
                          │
                          ▼
2. A IA TRADUZ: ───► Transforma em código ───► [0, 13, 002] (O "CEP" da sua busca)
                          │
                          ▼
3. A IA COMPARA OS "CEPs" NA TABELA:

   [0, 13, 002] (Sua Busca)
        │
        ├──► Está a 1 ponto de [0, 13, 001] (Av. Paulista)  ──► ⭐ PAR PERFEITO!
        ├──► Está a 3 pontos de [0, 13, 005] (Rua Augusta)  ──► 🎯 MUITO PERTO!
        │
        └──► Está a 2.000 pontos de [2, 20, 001] (Copacabana) ──► ❌ LONGE DEMAIS

```

> **Resultado da Busca:** O robô calcula a menor distância numérica e te entrega as opções mais próximas na tela (Av. Paulista e Rua Augusta), sem precisar ler uma única palavra em português.