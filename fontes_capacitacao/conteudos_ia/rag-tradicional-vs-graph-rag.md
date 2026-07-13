# RAG Tradicional vs Graph RAG — Do texto bruto à resposta

## Por que RAG tradicional NÃO resolve perguntas relacionais

A resposta pra perguntas como *"Quais professores orientam alunos que publicaram NLP mas NÃO deram aula pra eles?"* está espalhada em **4 fatos de 4 documentos diferentes** que precisam ser verificados em sequência lógica. RAG tradicional é **Ctrl+F inteligente** — busca similaridade, não faz raciocínio relacional.

---

## RAG Tradicional — Tentativa (e falha)

### 1. Chunking

O sistema acadêmico tem documentos espalhados. Cada um vira chunks independentes:

```
Fonte A — PDF do departamento:
  chk_7:  "O Departamento de Computação conta com 34
           professores. João Silva é professor titular..."

Fonte B — Currículo Lattes (PDF):
  chk_142: "João Silva orienta atualmente 3 alunos de
            mestrado: Ana Costa, Bruno Lima, Carla Pereira."
  chk_143: "Publicações recentes: BERT-based NER for Legal
            Documents, EMNLP 2025, com Ana Costa."

Fonte C — Catálogo de disciplinas (PDF):
  chk_301: "Disciplina: Inteligência Artificial (CMP-701).
            Ministrada por: João Silva. Turma 2025/1."
  chk_302: "Alunos matriculados em CMP-701: Ana Costa,
            Bruno Lima, Daniel Rocha..."

Fonte D — Anais de conferência (PDF):
  chk_488: "EMNLP 2025 Proceedings. Paper #42: Transformer
            Architectures for Low-Resource Languages.
            Autores: Ana Costa, João Silva..."
```

### 2. Embedding

Cada chunk vira vetor. Chunks sobre departamento ficam próximos entre si. Chunks sobre NLP ficam próximos entre si. Mas **eles estão em regiões diferentes do espaço**:

```
       Região "NLP/Publicações"          Região "Departamento"
              ↑                                  ↑
    chk_488 [0.89, 0.34, -0.12...]     chk_7 [0.01, -0.67, 0.45...]
    chk_143 [0.91, 0.30, -0.15...]

         "transformers"                    "professores"
         "NLP, EMNLP"                      "departamento"
              │                                  │
              └─────────── distância grande ──────┘
```

### 3. Armazenar

Os 500+ chunks estão no Vector DB. O banco sabe que chk_488 é próximo de chk_143 (ambos falam de NLP). Mas **não sabe que chk_488 (paper da Ana) está conectado a chk_142 (João orienta Ana) e a chk_302 (Ana cursou IA com João)**. O Vector DB só tem vetores e texto — não tem grafo de relações.

### 4. Busca (o momento da falha)

```
Pergunta: "Quais professores do depto de Computação
           orientam alunos de mestrado que publicaram
           papers sobre NLP em 2025, mas NÃO deram
           aula pra esses mesmos alunos?"
                ↓ embedding
query_vec → [0.52, -0.18, 0.63, ...]

O Vector DB busca os chunks mais próximos:

query × chk_142 → cos = 0.81  ✓ "João orienta Ana..."
query × chk_7   → cos = 0.76  ✓ "Depto de Computação..."
query × chk_488 → cos = 0.74  ✓ "Paper NLP, Ana Costa..."
query × chk_301 → cos = 0.71  ✓ "João ministra IA..."
```

**Todos os 4 chunks são relevantes.** Mas isso NÃO adianta:

```
O que o RAG entrega pra LLM:
┌─────────────────────────────────────────────────┐
│ Contexto (top-3 chunks):                        │
│                                                 │
│ "João Silva orienta Ana Costa, Bruno Lima..."   │ ← chk_142
│ "Departamento de Computação: 34 professores..." │ ← chk_7
│ "Ana Costa publicou Transformer Architectures   │ ← chk_488
│  na EMNLP 2025 com João Silva..."               │
│                                                 │
│ Pergunta: "Quais professores..."                │
└─────────────────────────────────────────────────┘
```

### 5. Injeção e falha

A LLM lê o contexto. Sabe que:
- João orienta Ana ✓
- Ana publicou NLP em 2025 ✓
- João é da Computação ✓

Mas **NÃO sabe** se João deu aula pra Ana. O chk_302 ("Alunos matriculados em CMP-701: Ana Costa...") **não foi incluído** — perdeu no top-K porque o cosseno foi 0.71 e só entram 3 chunks. Mesmo se entrasse, a LLM precisaria **comparar 4 fatos de 4 chunks diferentes e aplicar uma negação lógica** — algo que ela é péssima em fazer:

```
Resposta típica: "João Silva orienta Ana Costa, que
publicou sobre Transformers na EMNLP 2025."

Erro: omite a restrição "NÃO deu aula pra esses alunos".
Ou alucina: afirma que não deu aula sem ter evidência.
Ou acerta por coincidência e erra o próximo professor.
```

**Por que falha:** a resposta está espalhada em 4 fatos de 4 documentos que precisam ser verificados em sequência. RAG tradicional busca similaridade — não cruza relações.

---

## Graph RAG — Como resolve

### Fase extra: do texto ao grafo

Antes de poder responder, uma LLM lê cada chunk extraindo entidades e relações:

```
chk_142 → LLM extrai:
  (João Silva)-[:ORIENTA]->(Ana Costa, nível: mestrado)
  (João Silva)-[:ORIENTA]->(Bruno Lima, nível: mestrado)

chk_488 → LLM extrai:
  (Ana Costa)-[:PUBLICOU]->(Paper #42, tema: NLP, ano: 2025)

chk_301 → LLM extrai:
  (João Silva)-[:MINISTROU]->(CMP-701 IA, turma: 2025/1)

chk_302 → LLM extrai:
  (Ana Costa)-[:MATRICULADA]->(CMP-701 IA)
```

**É aqui que o custo 5-10x morre**: cada chunk passa por uma LLM. 500 chunks = 500 chamadas. E é assim a cada reindexação.

### Consulta: Cypher vs SQL

```
Cypher:                                SQL equivalente:

MATCH (p:Professor)                    SELECT p.nome, a.nome, paper.titulo
  -[:BELONGS_TO]->                     FROM professor p
  (d:Department {nome:"Computação"})   JOIN departamento d
                                          ON p.dept_id = d.id
                                        JOIN orientacao o
MATCH (p)                                  ON p.id = o.prof_id
  -[:ORIENTA]->                        JOIN aluno a
  (a:Aluno {nivel:"mestrado"})             ON o.aluno_id = a.id
                                        JOIN publicacao pub
MATCH (a)                                  ON a.id = pub.aluno_id
  -[:PUBLICOU]->                       JOIN paper
  (paper:Paper)                            ON pub.paper_id = paper.id
WHERE paper.tema CONTAINS "NLP"        LEFT JOIN turma t
  AND paper.ano = 2025                     ON p.id = t.prof_id
  AND NOT (p)                          LEFT JOIN matricula m
    -[:MINISTROU]->                        ON a.id = m.aluno_id
    (:Disciplina)                          AND t.disciplina_id
    <-[:MATRICULADA]-(a)                      = m.disciplina_id
                                        WHERE d.nome = 'Computação'
RETURN p.nome, a.nome, paper.titulo       AND a.nivel = 'mestrado'
                                          AND paper.tema ILIKE '%NLP%'
                                          AND paper.ano = 2025
                                          AND m.id IS NULL
```

| | Cypher | SQL |
|---|---|---|
| **Modelagem** | LLM extrai do texto automaticamente | Humano define schema e povoa tabelas |
| **Navegação** | `(A)-[:REL]->(B)` — setas no grafo | `JOIN ON FK = PK` — chaves estrangeiras |
| **Negação** | `AND NOT (p)-[:MINISTROU]->()<-[:MATRICULADA]-(a)` — caminho não existe | `LEFT JOIN ... WHERE m.id IS NULL` — anti-join |
| **Adicionar relação** | LLM extrai nova aresta automaticamente | `ALTER TABLE` + migration + repovoamento |
| **Custo de setup** | 500+ chamadas de LLM pra extrair entidades/relações | Zero chamadas, horas de modelagem humana |
| **Manutenção** | Reindexa (mais 500 chamadas de LLM) | `INSERT`/`UPDATE` pontuais |

### Resultado

```
João Silva orienta Ana Costa (NLP paper, EMNLP 2025)
  → João MINISTROU CMP-701, Ana MATRICULADA em CMP-701
  → ❌ NÃO atende (deu aula pra ela)

João Silva orienta Bruno Lima (GNN paper, 2025)
  → João MINISTROU CMP-701, Bruno MATRICULADO em CMP-701
  → ❌ NÃO atende

...se houvesse professor orientando aluno com NLP 2025
   mas NUNCA deu aula pra ele:
  → ✅ ATENDE
```

---

## Resumo visual

```
RAG Tradicional:
  Documentos → [chunks] → embeddings → Vector DB
                                         ↓
  Pergunta → embedding → busca top-3 → LLM
                                         ↓
                                   Resposta INCOMPLETA
                                   (só o que cabe em 3 chunks)

Graph RAG:
  Documentos → [chunks] → LLM extrai entidades → Grafo
                                                     ↓
  Pergunta → LLM gera Cypher → executa no grafo → LLM
                                                     ↓
                                               Resposta COMPLETA
                                               (atravessou 5 relações)
```

**Trade-off**: RAG tradicional — barato, rápido, resolve ~90%. Graph RAG — caro (5-10x), lento (LLM extraindo entidade de cada chunk), resolve os 10% que exigem conexões entre entidades.
