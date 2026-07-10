# Laboratório — Embeddings + PCA (versão CEP/Estados)

> **Analogia**: CEP = embedding (muitos números). Estado = PCA (só o que importa).

---

## Motivação — O que isso tem a ver com RAG?

RAG precisa buscar chunks parecidos com sua pergunta. O embedding transforma texto em ~768 números. Mas como saber se a busca funcionou? Você precisa **visualizar** os embeddings. Só que 768 dimensões não cabem na tela. O PCA comprime pra 2.

---

## Passo 1 — Os dados (8 dígitos por endereço = embedding)

```json
{ rua: "Beira-Mar Norte, 1000",      cep: "88010-400" },  // Florianópolis, SC
{ rua: "Av. Mauro Ramos, 500",       cep: "88020-160" },  // Florianópolis, SC
{ rua: "Rua XV de Novembro, 200",    cep: "89201-300" },  // Joinville, SC
{ rua: "Av. Batel, 1500",            cep: "80420-010" },  // Curitiba, PR
{ rua: "Rua XV de Novembro, 100",    cep: "80010-000" },  // Curitiba, PR
{ rua: "Av. Afonso Pena, 2500",      cep: "30130-000" },  // Belo Horizonte, MG
{ rua: "Rua da Bahia, 800",          cep: "30160-010" },  // Belo Horizonte, MG
{ rua: "Av. do Contorno, 500",       cep: "30110-000" },  // Belo Horizonte, MG
```

**Problema**: 8 dígitos. Impossível desenhar um gráfico com 8 eixos. Mas o olho humano já vê o padrão: os CEPs começam com 88 (SC), 80 (PR) ou 30 (MG).

**O PCA faz exatamente isso — só que com 768 dígitos em vez de 8.**

---

## Passo 2 — PCA analisa

O PCA pega os 8 dígitos e pergunta: **"qual dígito mais separa esses endereços?"**

```
Dígito 1 (8, 8, 3)       → separa MG (3) de SC+PR (8)                     ← BOM
Dígito 2 (8, 0, 0)       → separa SC (8) de PR (0) e MG (0)               ← BOM
Dígito 3 (0, 2, 1, 0, 1) → varia aleatoriamente, não separa nada          ← lixo
Dígito 4 (1, 2, 0, 2)    → não separa nada                                ← lixo
Dígito 5 (0, 1, 0, 0)    → não separa nada                                ← lixo
Dígito 6 (4, 6, 0, 1)    → não separa nada                                ← lixo
Dígito 7 (0, 1, 0, 0)    → não separa nada                                ← lixo
Dígito 8 (0, 0, 0, 0)    → todos zero, inútil                             ← lixo
```

**Veredito do PCA**: "Dígitos 1 e 2 juntos separam SC, PR e MG. Os outros 6 são ruído."

---

## Passo 3 — PCA comprime 8 → 1

```json
{ rua: "Beira-Mar Norte, 1000",     estado: 88 },  // SC
{ rua: "Av. Mauro Ramos, 500",      estado: 88 },  // SC
{ rua: "Rua XV de Novembro, 200",   estado: 88 },  // SC (Joinville)
{ rua: "Av. Batel, 1500",           estado: 80 },  // PR
{ rua: "Rua XV de Novembro, 100",   estado: 80 },  // PR
{ rua: "Av. Afonso Pena, 2500",     estado: 30 },  // MG
{ rua: "Rua da Bahia, 800",         estado: 30 },  // MG
{ rua: "Av. do Contorno, 500",      estado: 30 },  // MG
```

De 8 dígitos pra 1 (os 2 primeiros dígitos do CEP). A informação que importa ficou. O detalhe (rua, bairro) foi descartado.

---

## Passo 4 — "Gráfico" (1D, linha reta)

```
  MG                PR                SC
  ──●──●──●───────────●──●───────────────●──●──●──
  30 30 30         80 80             88 88 88
Afonso Pena     XV Novembro       Beira-Mar Norte
Rua da Bahia    Av. Batel         Mauro Ramos
Av. Contorno                      XV de Novembro
```

3 grupos nítidos. O PCA descartou 6 dígitos e manteve 2 (os que formam o prefixo do estado). Ainda assim, você sabe quem é vizinho de quem.

---

## Bônus — Consulta RAG com um CEP que não está na base

Agora chega um endereço NOVO, que o sistema nunca viu:

```json
{ rua: "Av. Higienópolis, 500",  cep: "83020-000" }
```

O RAG transforma o CEP em embedding: `[8, 3, 0, 2, 0, 0, 0, 0]`.

O PCA comprime: primeiros dois dígitos = **83**.

E agora pergunta: **"qual endereço da base é o mais parecido?"**

```
CEP novo: 83020-000  → prefixo 83 (não está no treinamento!)
                          │
                          ▼
                     MG (30)         PR (80)   (83)     SC (88)
                     ──●──●──●─────────●──●──────●─────────●──●──●──
                                                  ↑
                                             Londrina aqui

Resultado: XV de Novembro/Curitiba e Av. Batel/Curitiba (prefixo 80)
           ↑ os 2 vizinhos mais próximos, ambos no Paraná
```

**O PCA nunca viu 83 durante o treinamento. Mas acertou: Londrina é Paraná!**

E se o RAG não fosse por significado, mas por Ctrl+F? Procuraria "83" nos CEPs da base e não acharia nada. **Zero resultados.** Fim da história. O embedding salvou.

---

### Traduzindo pra RAG de verdade

```json
// Consulta nova (nunca esteve na base):
{ pergunta: "Como faço para devolver um produto com defeito?" }

// Embedding comprimido com PCA → cai perto de:
{ chunk: "Política de reembolso e devoluções" }
{ chunk: "Prazo para troca: 7 dias úteis" }
{ chunk: "Defeito de fabricação: troca imediata" }

// NÃO cai perto de (apesar de ter palavras parecidas):
{ chunk: "Investimento em renda fixa" }
{ chunk: "Cadastro de novo fornecedor" }
```

O RAG não fez Ctrl+F por "devolver" ou "defeito". Ele foi pelo **significado** — e acertou. O PCA só mostrou no gráfico que a busca fez sentido.

---

## Passo 5 — Aplicando isso a embeddings de verdade

```
CEP (8 dígitos)                    Embedding (768 dimensões)
─────────────────────────────────────────────────────────────
Cada dígito = uma dimensão        Cada número = uma dimensão
Dígito 1 = estado                 Dimensão 37 = "é animal?"
Dígitos 2-8 = rua, bairro         Dimensões 38-768 = detalhes
PCA descarta 7, fica com 1        PCA descarta 766, fica com 2
3 grupos: SP, RJ, PR              4 grupos: animais, veículos, profissões, verbos
```

---

## PCA em 1 frase

> **CEP tem 8 dígitos, mas o primeiro já te diz o estado. O PCA acha esse "primeiro dígito" sozinho.**

## Embedding + PCA em 1 frase

> **Embedding é o CEP da palavra. PCA é descobrir que só o estado importa pra separar os grupos.**
