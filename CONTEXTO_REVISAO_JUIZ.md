## Contexto para continuar — Revisão Juiz Workshop IA

### O que estamos fazendo
Revisando uma a uma as 83 intervenções do relatório `plano_topicos/roteiro-revisao-juiz.md`, gerado por 3 agentes simulando plateia (Iniciante, Intermediário, Avançado) sobre o workshop "IA para Desenvolvimento de Software" (~16h, 2 dias, 7 módulos).

Arquivos principais:
- `plano_topicos/workshop-ia-para-devs.md` — conteúdo programático
- `plano_topicos/roteiro-apresentacao.md` — roteiro do instrutor
- `plano_topicos/roteiro-revisao-juiz.md` — relatório com 83 intervenções e parecer do juiz

### Onde paramos
Intervenção #33 (de 83). Já passamos #1 a #32 com ações tomadas.

### Status das intervenções já discutidas

**Resolvidas (já apliquei a correção no roteiro):**
- #1: MCP/SDD no slide 1.0 → trocar texto
- #3: "Token" usado antes de definição → definição-relâmpago
- #4+#5: Analogia do GPS → removida, substituída por autocomplete turbinado
- #6: Janela de contexto não definida → analogia nova: token=gasolina, janela=porta-malas
- #7: Três conceitos em 5 min → pausas explícitas no roteiro
- #8: Lost in the middle → nota de rodapé para instrutor (Liu et al. 2023)
- #9+#10: Cálculo de tokens + custos → demo ao vivo com OpenRouter
- #12: "Explique RAG" → troquei exemplo para "Explique SQL injection"
- #13: Data de corte → uma frase: "modelo congelado como binário compilado"
- #14: Conexão janela→degradação → ponte explícita na fala da limitação 4
- #15: Demo de alucinação → discutimos exemplos (Java 25, comida, nome da plateia)
- Slide 1.4 reescrito: analogia da graduação, exemplo concreto Java 500 repositórios, caso Rio 3.5
- #22: Não-determinismo → adicionada explicação de 1 frase
- #11: Multimodalidade → demo ao vivo de wireframe (encaminhado)
- #23: Ollama omite limitações → nota de rodapé no slide 2.2 + diagrama auxiliar (vllm-vs-llamacpp.excalidraw)
- #24: Sopa de letrinhas (SLM, Phi-3, Llama 8B) → acrônimos expandidos na fala
- #25: Parâmetros definidos vagamente → nova definição: "arquivo de números, igual receita de bolo"
- #26: Remover parâmetros melhora sem contexto → nota com 3 papers (Lottery Ticket, SparseGPT, Wanda)
- #27: Slide 3.1 sem template → card com template copiável [ROLE][CONTEXTO][INSTRUÇÃO][RESTRIÇÕES][FORMATO]
- #28: Slide 3.2 frameworks sem prompt real → prompts Java reais (RTF=endpoint REST, CARE=otimizar consulta, RISE=diagnóstico consolidação notas)
- #29: Zero-shot, Few-shot, CoT não desempacotados → etimologia na fala: "zero exemplos, poucos exemplos, cadeia de raciocínio"
- #30: Demo de CoT sem exemplo no slide → acatado, slide terá exemplo com/sem CoT
- #31: Cheat sheet não integra frameworks com técnicas → acatado, segunda camada na árvore
- #32: RISE+CoT complexo demais → acatado, cenário pré-mordido no laboratório

**Parcialmente resolvidas:**
- #2: OpenCode como única ferramenta → reconhecido, apêndice de equivalentes pendente
- #16: Taxonomia de alucinações → nota de rodapé pendente (factual/raciocínio/fidelidade)
- #17+#18: Embedding/reindexa no M1 → slide tem a palavra "embedding", decisão pendente

**Em discussão agora:**
- #33: Pipeline RAG sem código → slide 4.2 precisa de mini-snippet de 5 linhas

### Insumos criados durante a revisão
- `excalidraw/auxiliares/llamavsvllm/vllm-vs-llamacpp.excalidraw` — diagrama Ollama vs llama.cpp vs vLLM
- `excalidraw/auxiliares/llamavsvllm/explicacao.md` — explicação completa com OpenCode
- `excalidraw/auxiliares/llamavsvllm/visao-vs-linguagem.excalidraw` — comparação modelo de visão vs LLM
- Analogias de pizza para RTF ("pedir pizza"), CARE ("pedir pizza com visita"), RISE ("ensinar o pizzaiolo")

### Formato de cada intervenção

```
**#N — Perfil — Slide X.Y: "título do slide"** (Gravidade)

> Citação do trecho problemático do roteiro ou slide.

**Parecer do juiz**: Acolho / Acolho parcialmente / Nota de rodapé.

**Sugestão**: o que fazer.
```

### Regras da dinâmica
- Eu (instrutor) pergunto e aplico as correções manualmente
- Você (Claude) sugere, eu decido
- Sempre que a intervenção for sobre o roteiro, mostre o trecho atual antes de sugerir
- Sempre indique qual perfil de agente fez o apontamento (Iniciante/Intermediário/Avançado)
- Se o Avançado criticar algo que é simplificação didática intencional, sugira nota de rodapé, não mudança de slide
- Sempre me diga em qual intervenção estamos e quantas faltam

### Próximas intervenções na fila
#34 — Iniciante — Slide 4.2: "Embeddings chamados de mágica"
#35 — Iniciante — Slide 4.2: "Cosseno sem contexto matemático"
#38 — Avançado — Slide 4.2: "Estratégias de chunking e hybrid search omitidas"
#39 — Iniciante — Slide 4.3: "PCA nunca explicado"
... e seguimos até #83
