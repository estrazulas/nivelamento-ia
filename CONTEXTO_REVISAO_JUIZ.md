## Contexto para continuar — Revisão Juiz Workshop IA

### O que estamos fazendo
Revisando uma a uma as 83 intervenções do relatório `plano_topicos/roteiro-revisao-juiz.md`, gerado por 3 agentes simulando plateia (Iniciante, Intermediário, Avançado) sobre o workshop "IA para Desenvolvimento de Software" (~16h, 2 dias, 7 módulos).

Arquivos principais:
- `plano_topicos/workshop-ia-para-devs.md` — conteúdo programático
- `plano_topicos/roteiro-apresentacao.md` — roteiro do instrutor
- `plano_topicos/roteiro-revisao-juiz.md` — relatório com 83 intervenções e parecer do juiz

### Onde paramos
Intervenção #23 (de 83). Já passamos #1 a #22 com ações tomadas.

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

**Parcialmente resolvidas:**
- #2: OpenCode como única ferramenta → reconhecido, apêndice de equivalentes pendente
- #16: Taxonomia de alucinações → nota de rodapé pendente (factual/raciocínio/fidelidade)
- #17+#18: Embedding/reindexa no M1 → slide tem a palavra "embedding", decisão pendente

**Em discussão agora:**
- #23: Ollama omite limitações para produção → já expliquei vLLM e llama.cpp, nota de rodapé sugerida para Slide 2.2 (Ollama e Hugging Face, Módulo 2). Slide 2.2 = "Ollama e Hugging Face (25 min)", linha 172 do roteiro.

### Formato de cada intervenção

```
**#N — Perfil — Slide X.Y: "título do slide"** (Gravidade)

> Citação do trecho problemático do roteiro ou slide.

**Parecer do juiz**: Acolho / Acolho parcialmente / Nota de rodapé.

**Sugestão**: o que fazer.
```

Exemplo de como conduzimos:

```
#24 — Iniciante — Slide 2.3: "Sopa de letrinhas" (Média)

> "SLMs (Phi-3, Llama 8B) entregam 80% da qualidade por 10% do custo."
> Três coisas novas de uma vez: SLM, Phi-3, Llama 8B. O que significa cada uma?

Sugestão: expandir acrônimos e notações na fala.

Daí eu (instrutor) pergunto, debato, peço alternativas, e aplico a correção.
Depois digo "próxima pergunta" e você traz a intervenção seguinte na fila.
```

### Regras da dinâmica
- Eu (instrutor) pergunto e aplico as correções manualmente
- Você (Claude) sugere, eu decido
- Sempre que a intervenção for sobre o roteiro, mostre o trecho atual antes de sugerir
- Sempre indique qual perfil de agente fez o apontamento (Iniciante/Intermediário/Avançado)
- Se o Avançado criticar algo que é simplificação didática intencional, sugira nota de rodapé, não mudança de slide
- Sempre me diga em qual intervenção estamos e quantas faltam

### Próximas intervenções na fila
#24 — Iniciante — Slide 2.3: "Sopa de letrinhas" (SLM, Phi-3, Llama 8B)
#25 — Iniciante — Slide 2.3: "Parâmetros definidos vagamente como neurônios"
#26 — Avançado — Slide 2.3: "Remover parâmetros melhora sem contexto"
... e seguimos até #83
