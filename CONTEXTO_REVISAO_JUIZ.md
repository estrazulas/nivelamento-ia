## Contexto para continuar — Revisão Juiz Workshop IA

### O que estamos fazendo
Revisando uma a uma as 83 intervenções do relatório `plano_topicos/roteiro-revisao-juiz.md`, gerado por 3 agentes simulando plateia (Iniciante, Intermediário, Avançado) sobre o workshop "IA para Desenvolvimento de Software" (~16h, 2 dias, 7 módulos).

Arquivos principais:
- `plano_topicos/workshop-ia-para-devs.md` — conteúdo programático
- `plano_topicos/roteiro-apresentacao.md` — roteiro do instrutor
- `plano_topicos/roteiro-revisao-juiz.md` — relatório com 83 intervenções e parecer do juiz

### Onde paramos
Intervenção #58 (de 83). Já passamos #1 a #58 com ações discutidas.

### Status das intervenções já discutidas

**Resolvidas (já apliquei a correção):**
- #1: MCP/SDD no slide 1.0 → trocar texto
- #3: "Token" usado antes de definição → definição-relâmpago
- #4+#5: Analogia do GPS → removida, substituída por autocomplete turbinado
- #6: Janela de contexto não definida → analogia: token=gasolina, janela=porta-malas
- #7: Três conceitos em 5 min → pausas explícitas no roteiro
- #8: Lost in the middle → nota de rodapé (Liu et al. 2023)
- #9+#10: Cálculo de tokens + custos → demo ao vivo com OpenRouter
- #12: "Explique RAG" → troquei exemplo para "Explique SQL injection"
- #13: Data de corte → "modelo congelado como binário compilado"
- #14: Conexão janela→degradação → ponte explícita na limitação 4
- #15: Demo de alucinação → exemplos Java 25, comida, nome da plateia
- Slide 1.4 reescrito: analogia da graduação, Java 500 repositórios, caso Rio 3.5
- #22: Não-determinismo → 1 frase de explicação
- #11: Multimodalidade → demo ao vivo de wireframe (encaminhado)
- #23: Ollama limitações → nota de rodapé slide 2.2 + diagrama vllm-vs-llamacpp
- #24: Sopa de letrinhas → acrônimos expandidos (SLM, Phi-3, Llama 8B)
- #25: Parâmetros vagos → "arquivo de números", exemplo receita de bolo
- #26: Remover parâmetros → nota com 3 papers (Lottery Ticket, SparseGPT, Wanda)
- #27: Slide 3.1 sem template → card [ROLE][CONTEXTO][INSTRUÇÃO][RESTRIÇÕES][FORMATO]
- #28: Slide 3.2 sem prompt real → prompts Java (RTF=endpoint, CARE=otimizar consulta, RISE=consolidação notas) + analogias pizza
- Roteiro Slide 3.2 atualizado: RTF="Pedir pizza. Três frases.", CARE="Pedir pizza com visita.", RISE="Ensinar o pizzaiolo."
- #29: Zero-shot, Few-shot, CoT → etimologia na fala
- #30: Demo de CoT sem exemplo → slide terá exemplo com/sem CoT (#34 resolvida junto: "mágica" removida da linha 365)
- #31: Cheat sheet não integra → segunda camada na árvore de decisão
- #32: RISE+CoT complexo → cenário pré-mordido no laboratório
- #33: Pipeline RAG sem código → snippet de 5 linhas adicionado ao slide 4.2
- #34: Embeddings = "mágica" → removido da linha 365, trocado por "GPS no espaço do significado"
- #35: Cosseno sem contexto → explicado como "setas apontando mesma direção"
- #38: Chunking e hybrid search → nota de rodapé com 3 técnicas
- #39: PCA nunca explicado → resolvido com os labs (CEP + palavras)
- #40: 768 desatualizado → explicado (varia por modelo: 384, 512, 768, 1536, 3072)
- #41: Cypher/Neo4j sem explicação → absorvida por #42+#43 (Graph RAG vira teaser, não menciona Cypher/Neo4j)
- #42+#43: Graph RAG em 10 min é avançado + omite custo → reduzido a teaser de 3 min com menção a custo 5-10x e paper Microsoft GraphRAG
- #44: Maior diferencial só 10 min → dividido: 5 min regra dos 50-70% + 5 min ponte explícita pro Módulo 6
- #45: Regra dos 40% sem suporte → nota de rodapé (heurística conservadora, RULER benchmark mostra 50-70%)
- #46: "Padrão da indústria" ignora fragmentação → matizado: MCP é o mais adotado, mas não universal (OpenAI function calling, Google A2A, Copilot via adaptador)
- #47: Frameworks de agentes omitidos → mini-quadro LangGraph/CrewAI/AutoGen no slide 5.3
- #48: Segurança de agentes omitida → novo tópico 5.6 com 4 perigos (prompt injection, excessive agency, tool poisoning, loop infinito) + mitigações + OWASP Top 10
- #49: Loop sem trace concreto → diagrama loop-agente-monitor.excalidraw com as 4 fases e trace real
- #50: "PDCA" sem explicação → expandir sigla na fala: Plan-Do-Check-Act
- #51: Loops infinitos, custo explosivo, task drift → mini-quadro com 3 problemas e mitigacoes (max_etapas, budget cap, checkpoint)
- #52: "Skill" usado antes de definido → definição-relâmpago no slide 5.5: "Skill = conhecimento estável encapsulado (ex: como criar testes). Detalhes no Módulo 6."
- #53: Distinção mutável/estável frágil → nota de rodapé (é ponto de partida, não lei; MCP = dados/ações, Skill = conhecimento procedural)
- #54: Narrativa linear não reflete realidade → nota de rodapé (3 padrões coexistem em 2026, Fase 3 é o destino mas não o único presente) + analogia melhorada: canivete suíço vs caixa de ferramentas
- #55: Agents.md/CLAUDE.md/.cursorrules sem contexto → explicar que cada ferramenta tem seu nome, mesma ideia: README pra IA. Roteiro atualizado com exemplo GitLab/SIGAA.
- #56: "Não crie sub-agents" é dogmático → confirmado que é posição do Waldemar no vídeo (33:00). Workshop reproduz fielmente. Avançado discorda do autor, não do workshop.
- #57: Contradiz documentação do Claude Code → nota: .claude/agents/*.md existe, Waldemar desencoraja super-agentes de 3000 linhas, não agentes focados de 100-200 linhas
- #58: Sobreposição conceitual com M4 e M5 → 3 pontes verbais no roteiro (M4.5→M6, M7.2→M5.4, M6.2→M4)

**Parcialmente resolvidas:**
- #2: OpenCode como única ferramenta → apêndice de equivalentes pendente
- #16: Taxonomia de alucinações → nota de rodapé pendente
- #17+#18: Embedding/reindexa no M1 → decisão pendente

**Próxima na fila:**
- #59: "PRD" mencionado sem definição no slide 7.1

### Insumos criados durante a revisão
- `excalidraw/auxiliares/llamavsvllm/` — diagrama Ollama vs llama.cpp vs vLLM + explicação
- `excalidraw/auxiliares/llamavsvllm/visao-vs-linguagem.excalidraw` — classificador cachorros vs LLM
- `excalidraw/auxiliares/lab-embeddings-pca.md` — lab completo embeddings+PCA (6→2 dimensões, 12 palavras)
- `excalidraw/auxiliares/lab-embeddings-pca-cep.md` — lab simplificado PCA (8→2 dígitos, CEPs SC/PR/MG)
- Analogias de pizza: RTF=pedir pizza, CARE=pedir com visita, RISE=ensinar pizzaiolo
- Analogias de PCA: CEP (estado), selfie (foto de grupo), ranking de importância
- PCA em 1 frase: "A máquina que olha N dimensões e te devolve só as que importam"
- 5 passos macro do PCA: Mede → Ranqueia → Junta redundantes → Descarta lixo → Devolve

### Formato de cada intervenção
```
**#N — Perfil — Slide X.Y: "título do slide"** (Gravidade)
> Citação do trecho problemático.
**Parecer do juiz**: Acolho / Parcial / Nota de rodapé.
**Sugestão**: o que fazer.
```

### Regras da dinâmica
- Eu (instrutor) pergunto e aplico as correções manualmente
- Você (Claude) sugere, eu decido
- Sempre mostre o trecho atual do roteiro antes de sugerir mudança
- Indique qual perfil de agente (Iniciante/Intermediário/Avançado)
- Avançado criticando simplificação didática → nota de rodapé, não mudança de slide
- Sempre diga em qual intervenção estamos e quantas faltam

### Próximas intervenções na fila
#42+#43 — Intermediário + Avançado — Slide 4.4: "Graph RAG em 10 min é avançado demais + omite custo"
#44 — Intermediário — Slide 4.5: "Maior diferencial recebe só 10 minutos"
#45 — Avançado — Slide 4.5: "Regra dos 40% sem suporte empírico"
... e seguimos até #83
