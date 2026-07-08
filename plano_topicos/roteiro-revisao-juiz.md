# Revisão do Juiz — Workshop "IA para Desenvolvimento de Software"

> **Origem**: Compilação de 83 intervenções de 3 agentes simulando a plateia
> **Agente 1 (Iniciante)**: 30 intervenções — Clareza, saltos lógicos, assunções
> **Agente 2 (Intermediário)**: 21 intervenções — Profundidade prática, exemplos, laboratórios
> **Agente 3 (Avançado)**: 32 intervenções — Precisão técnica, omissões, ferramentas
> **Data**: 2026-07-08

---

## Resumo das Intervenções

| # | Módulo | Slide | Agente | Tipo | Gravidade | Tema |
|---|--------|-------|--------|------|-----------|------|
| 1 | 1 | 1.0 | Iniciante | Assunção | Média | MCP e SDD mencionados sem definição |
| 2 | 1 | 1.0 | Avançado | Ferramentas | Alta | OpenCode como única ferramenta obrigatória |
| 3 | 1 | 1.1 | Iniciante | Clareza | Média | "Token" usado antes de ser definido |
| 4 | 1 | 1.1 | Iniciante | Analogia | Média | Analogia do GPS é imprecisa |
| 5 | 1 | 1.1 | Avançado | Imprecisão | Média | "Grande Autocomplete" simplifica o mecanismo transformer |
| 6 | 1 | 1.2 | Iniciante | Assunção | Alta | "Janela de contexto" não definida |
| 7 | 1 | 1.2 | Iniciante | Salto lógico | Média | Três conceitos novos em 5 minutos sem pausa |
| 8 | 1 | 1.2 | Avançado | Imprecisão | Alta | "Esquecer coisas no meio" explicado incorretamente |
| 9 | 1 | 1.2 | Intermediário | Profundidade | Alta | Cálculo de tokens prometido mas nunca demonstrado |
| 10 | 1 | 1.2 | Avançado | Omissão | Média | Custos reais de API nunca traduzidos em valores |
| 11 | 1 | 1.2 | Avançado | Omissão | Média | Multimodalidade sem demonstração prática |
| 12 | 1 | 1.3 | Iniciante | Clareza | Alta | "RAG" usado como exemplo antes de ser definido |
| 13 | 1 | 1.3 | Iniciante | Assunção | Baixa | Mecanismo da data de corte nunca explicado |
| 14 | 1 | 1.3 | Iniciante | Salto lógico | Média | Conexão janela→degradação não estabelecida |
| 15 | 1 | 1.3 | Intermediário | Exemplo | Média | Demo de alucinação usa storytelling, não evidência |
| 16 | 1 | 1.3 | Avançado | Omissão | Alta | Taxonomia de alucinações ignorada |
| 17 | 1 | 1.4 | Iniciante | Clareza | Alta | "Embedding" mencionado sem definição |
| 18 | 1 | 1.4 | Iniciante | Assunção | Baixa | "Reindexa" pressupõe conhecimento de índices vetoriais |
| 19 | 1 | 1.4 | Iniciante | Analogia | Baixa | Analogia do chef não explica mecanismo |
| 20 | 1 | 1.4 | Intermediário | Profundidade | Alta | Regra dos 95% afirmada sem evidência |
| 21 | 1 | 1.4 | Avançado | Imprecisão | Média | Regra dos 95% é dogmática; ignora LoRA e casos legítimos |
| 22 | 1 | 1.5 | Iniciante | Assunção | Baixa | "Não-determinismo" jogado sem explicação |
| 23 | 2 | 2.2 | Avançado | Imprecisão | Média | Ollama omite limitações para produção |
| 24 | 2 | 2.3 | Iniciante | Assunção | Média | Sopa de letrinhas: SLM, Phi-3, Llama 8B |
| 25 | 2 | 2.3 | Iniciante | Clareza | Média | "Parâmetros" definidos vagamente como "neurônios" |
| 26 | 2 | 2.3 | Avançado | Imprecisão | Baixa | "Remover parâmetros melhora" sem contexto |
| 27 | 3 | 3.1 | Intermediário | Exemplo | Alta | Slide não contém template reutilizável |
| 28 | 3 | 3.2 | Intermediário | Exemplo | Alta | Frameworks descritos mas sem prompt real |
| 29 | 3 | 3.3 | Iniciante | Clareza | Alta | "Zero-shot", "Few-shot", "CoT" não desempacotados |
| 30 | 3 | 3.3 | Intermediário | Profundidade | Média | Demo de CoT prometida mas slide não contém exemplo |
| 31 | 3 | 3.5 | Intermediário | Laboratório | Baixa | Cheat sheet não integra frameworks com técnicas |
| 32 | 3 | Lab | Intermediário | Laboratório | Média | RISE+CoT é ordens de grandeza mais complexo que SQL/RTF |
| 33 | 4 | 4.2 | Intermediário | Profundidade | Alta | Pipeline RAG sem uma linha de código |
| 34 | 4 | 4.2 | Iniciante | Clareza | Alta | "Embeddings" chamados de "mágica" |
| 35 | 4 | 4.2 | Iniciante | Assunção | Alta | "Cosseno" sem contexto matemático |
| 36 | 4 | 4.2 | Iniciante | Clareza | Média | "Top-K" e "Threshold" sem definição |
| 37 | 4 | 4.2 | Iniciante | Clareza | Média | Trade-off de chunks explicado como regra, não mecanismo |
| 38 | 4 | 4.2 | Avançado | Omissão | Alta | Estratégias de chunking e hybrid search omitidas |
| 39 | 4 | 4.3 | Iniciante | Clareza | Alta | "PCA" nunca expandido nem explicado |
| 40 | 4 | 4.3 | Avançado | Ferramentas | Média | "768+ números" desatualizado; omite Matryoshka |
| 41 | 4 | 4.4 | Iniciante | Assunção | Média | "Cypher" e "Neo4j" sem explicação |
| 42 | 4 | 4.4 | Intermediário | Ritmo | Média | Graph RAG em 10 min é avançado demais |
| 43 | 4 | 4.4 | Avançado | Omissão | Média | Custo do Graph RAG 5-10x maior não mencionado |
| 44 | 4 | 4.5 | Intermediário | Ritmo | Alta | Maior diferencial recebe só 10 minutos |
| 45 | 4 | 4.5 | Avançado | Imprecisão | Média | Regra dos 40% sem suporte empírico robusto |
| 46 | 5 | 5.1 | Avançado | Imprecisão | Alta | "Padrão da indústria" ignora fragmentação real |
| 47 | 5 | 5.3 | Avançado | Omissão | Alta | Frameworks de agentes (LangGraph, CrewAI) omitidos |
| 48 | 5 | 5.3-5.4 | Avançado | Omissão | Alta | Segurança de agentes: prompt injection, tool poisoning |
| 49 | 5 | 5.4 | Intermediário | Profundidade | Média | Loop sem trace concreto de execução real |
| 50 | 5 | 5.4 | Iniciante | Assunção | Baixa | "PDCA" referenciado sem explicação |
| 51 | 5 | 5.4 | Avançado | Omissão | Alta | Loops infinitos, custo explosivo, task drift não mencionados |
| 52 | 5 | 5.5 | Iniciante | Salto lógico | Alta | "Skill" usado antes de ser definido no Módulo 6 |
| 53 | 5 | 5.5 | Avançado | Imprecisão | Baixa | Distinção mutável/estável é frágil |
| 54 | 6 | 6.1 | Avançado | Imprecisão | Baixa | Narrativa linear não reflete realidade do ecossistema |
| 55 | 6 | 6.2-6.3 | Iniciante | Clareza | Média | "Agents.md", "CLAUDE.md", "claude onboard" sem contexto |
| 56 | 6 | 6.5 | Avançado | Imprecisão | Alta | "Não crie sub-agents" é dogmático |
| 57 | 6 | 6.5-6.6 | Avançado | Imprecisão | Média | Contradiz documentação do Claude Code sobre custom agents |
| 58 | 6 | 6.1-6.6 | Intermediário | Ritmo | Média | Sobreposição conceitual com Módulos 4 e 5 |
| 59 | 7 | 7.1 | Iniciante | Assunção | Baixa | "PRD" mencionado sem definição |
| 60 | 7 | 7.1 | Intermediário | Profundidade | Média | Solução é "use SDD" sem primeira ação concreta |
| 61 | 7 | 7.2 | Intermediário | Exemplo | Alta | spec.md, design.md, tasks.md referenciados mas não mostrados |
| 62 | 7 | 7.3 | Intermediário | Exemplo | Alta | STATE.md explicado mas sem formato concreto |
| 63 | 7 | 7.3 | Iniciante | Clareza | Média | STATE.md sem exemplo visual |
| 64 | 7 | 7.4 | Iniciante | Assunção | Baixa | "Vibe coding" mencionado sem definição |
| 65 | 7 | 7.4 | Avançado | Imprecisão | Baixa | RPI deveria incluir Verify |
| 66 | 7 | 7.5 | Intermediário | Profundidade | Média | Ferramentas puramente descritivas, sem critérios |
| 67 | 7 | 7.5 | Avançado | Ferramentas | Média | Omite categorias inteiras e info desatualizada do Copilot |
| 68 | 7 | 7.6 | Intermediário | Laboratório | Alta | 10 min para Specify é irrealista |
| 69 | 7 | 7.6 | Intermediário | Promessa | Baixa | Resumo final omite Módulos 2, 3, 4, 5 |
| 70 | 7 | 7.1-7.4 | Avançado | Referências | Baixa | SDD sem referências a SWE-bench, SWE-agent |
| 71 | Geral | — | Iniciante | Salto lógico | Média | Transição M3→M4 sem ponte narrativa |
| 72 | Geral | — | Iniciante | Salto lógico | Alta | Conceitos interdependentes mencionados cedo, explicados tarde |
| 73 | Geral | — | Intermediário | Profundidade | Alta | 71% teoria / 29% prática |
| 74 | Geral | — | Intermediário | Promessa | Alta | Templates prometidos mas não fornecidos |
| 75 | Geral | — | Avançado | Omissão | Alta | Falta módulo de avaliação e métricas |
| 76 | Geral | — | Avançado | Referências | Alta | 100% vídeos YouTube, zero papers ou docs oficiais |
| 77 | Geral | — | Avançado | Ordem | Média | RAG antes de Prompt Engineering seria melhor |
| 78 | Geral | — | Avançado | Omissão | Alta | Prompt Caching nunca mencionado |
| 79 | Geral | — | Avançado | Omissão | Média | LLM-as-Judge completamente ignorado |
| 80 | Geral | — | Avançado | Omissão | Baixa | Local-first e edge AI ausentes |
| 81 | Geral | — | Intermediário | Laboratório | Alta | Labs ambiciosos demais para o tempo alocado |
| 82 | Mód. 4 | Ref | Iniciante | Clareza | Baixa | RAGAS mencionado nas refs mas nunca no workshop |
| 83 | Mód. 1 | 1.3 | Iniciante | Salto lógico | Média | Conexão janela→degradação não estabelecida |

---

## Intervenções por Módulo

---

### Módulo 1 — Como LLMs Funcionam de Verdade

#### Slide 1.0 — Pré-requisitos

**#1 — Iniciante: "MCP e SDD mencionados sem definição"** (Média)
> O slide de pré-requisitos lista "Conta no GitHub — Para laboratórios de MCP e SDD". Estou no minuto 5 e o instrutor já joga duas siglas que jamais ouvi.

**Parecer do juiz**: **Acolho.** É desnecessário usar siglas não definidas no slide de abertura. Isso gera ansiedade desnecessária no iniciante.
**Ação**: Trocar para "Conta no GitHub — Para laboratórios de integração (Módulos 5 e 7)".

---

**#2 — Avançado: "OpenCode como única ferramenta obrigatória"** (Alta)
> OpenCode é do Waldemar Neto, autor do workshop e de todos os vídeos. Isso configura potencial conflito de interesses. O workshop vira um tutorial disfarçado do OpenCode.

**Parecer do juiz**: **Acolho parcialmente.** O apontamento sobre conflito de interesses é legítimo, mas a escolha de uma ferramenta única para padronizar os laboratórios tem mérito didático real (evita o caos de suportar 6 ferramentas simultaneamente). O problema não é usar OpenCode — é não oferecer alternativas.
**Ação**: Adicionar ao slide de pré-requisitos uma nota: "Os exemplos usam OpenCode, mas os princípios se aplicam a Cursor, Claude Code e Copilot. Consulte o guia de equivalentes no material do aluno." E criar um apêndice de 1 página com equivalentes por ferramenta.

---

#### Slide 1.1 — O Grande Autocomplete

**#3 — Iniciante: "Token usado antes de ser definido"** (Média)
> O subtítulo diz "máquina de previsão estatística de tokens" mas eu nem sei o que é token.

**Parecer do juiz**: **Acolho.** É uma correção trivial com alto impacto.
**Ação**: Na primeira menção a "token", inserir: "Token é um pedaço de palavra — 'inteligência artificial' são 2 tokens. No próximo slide a gente aprofunda."

---

**#4 — Iniciante + #5 — Avançado: "Analogia do GPS é imprecisa"** (Média)
> Iniciante: Um GPS de verdade usa Dijkstra/A*, não "histórico de rotas". Avançado: Sugere que a LLM tem acesso ao histórico de treinamento durante inferência.

**Parecer do juiz**: **Acolho.** Dois agentes independentes identificaram o mesmo problema. A analogia do autocomplete do celular é suficiente e mais precisa.
**Ação**: Remover a analogia do GPS. Usar apenas: "É como o autocomplete do celular, mas em vez de prever entre 3 opções baseado nas últimas 2 palavras, prevê entre milhões baseado em TODAS as palavras da conversa atual."

---

**#5 — Avançado: "Grande Autocomplete simplifica demais o mecanismo"** (Média)
> O autocomplete do celular é n-grama/Markov. LLMs usam atenção multi-head com complexidade quadrática. São fundamentalmente diferentes.

**Parecer do juiz**: **Discordo da intervenção como crítica, mas acolho como nota de rodapé.** A simplificação é INTENCIONAL e didaticamente correta: o princípio de "prever próximo token" é o mesmo. A diferença arquitetural (transformers vs n-gramas) não ajuda o aluno a usar IA melhor. Explicar multi-head attention no Módulo 1 afogaria os iniciantes.
**Ação**: Adicionar nota de rodapé para o instrutor: "Se algum aluno perguntar sobre a diferença entre autocomplete e LLM: o mecanismo é diferente (transformers com atenção vs n-gramas), mas o princípio de previsão do próximo token é o mesmo. O transformer consegue 'prestar atenção' em todas as palavras simultaneamente."

---

#### Slide 1.2 — Tokens e Modelos Multimodais

**#6 — Iniciante: "Janela de contexto não definida"** (Alta)
> "A janela é a RAM da IA." Mas o que É a janela de contexto? A analogia com RAM não me ajuda porque RAM é hardware; janela de contexto é um conceito abstrato.

**Parecer do juiz**: **Acolho com força.** Este é um dos problemas mais graves do Módulo 1. "Janela de contexto" é um conceito central que aparece em todos os módulos seguintes. Se não ficar claro aqui, o aluno passa 16 horas com compreensão turva.
**Ação**: Antes da analogia com RAM, dar a definição em uma frase: "Janela de contexto é quanto texto a IA consegue processar de uma vez — como um campo de texto com tamanho máximo. O modelo 'vê' tudo dentro da janela, mas ignora o que está fora."

---

**#7 — Iniciante: "Três conceitos em 5 minutos sem pausa"** (Média)
> Em 5 minutos: token, janela de contexto, lost-in-the-middle. Não há tempo para absorver.

**Parecer do juiz**: **Acolho.** O Slide 1.2 está sobrecarregado: tokenização, modelos multimodais, janela de contexto E lost-in-the-middle em 15 minutos.
**Ação**: Separar claramente com pausas e checkpoints: "Primeiro: token. [pausa, respira, pergunta se alguém tem dúvida]. Agora: janela de contexto. [pausa]. E aqui está a pegadinha..."

---

**#8 — Avançado: "Esquecer coisas no meio explicado incorretamente"** (Alta)
> Não é que o modelo "prioriza" início e fim estrategicamente. É um viés arquitetural do mecanismo de atenção (Liu et al., 2023 — "Lost in the Middle"). Modelos 2025 (Gemini 1.5, Claude 3.5) melhoraram significativamente.

**Parecer do juiz**: **Acolho como nota de rodapé.** A explicação coloquial ("prioriza início e fim") é didaticamente válida para iniciantes, mas o instrutor deve saber a explicação correta para o caso de um aluno avançado perguntar.
**Ação**: Nota de rodapé: "Tecnicamente, é um viés do mecanismo de atenção (Liu et al., 2023). Modelos com MoE e atenção de longo alcance estão reduzindo esse efeito. A regra dos 40% (Módulo 4) é a solução prática."

---

**#9 — Intermediário: "Cálculo de tokens prometido mas nunca demonstrado"** (Alta)
> O programa promete "Calcular tokens em cenários reais" mas o bônus do laboratório trata isso como opcional.

**Parecer do juiz**: **Acolho.** O objetivo de aprendizagem explicitamente promete "Calcular tokens em cenários reais". Se é um objetivo declarado, não pode ser bônus opcional.
**Ação**: Dedicar 5 minutos do slide a uma demonstração com `tiktoken` ou com o token counter do OpenCode: "Este prompt de 50 linhas = 2.300 tokens. No Claude Sonnet a $3/MTok input = $0,007. Se você fizer 100 por dia = $0,69/dia." Isso conecta o abstrato ao concreto.

---

**#10 — Avançado: "Custos reais de API nunca traduzidos em valores"** (Média)
> O aluno sai sem saber que uma sessão de dev com Claude Code consome ~$5-20/dia.

**Parecer do juiz**: **Acolho** — complementa a intervenção #9.
**Ação**: Adicionar tabela de preços referenciais (julho 2026): Claude Sonnet $3/$15 por 1M input/output, GPT-4o $2.50/$10, Gemini Flash $0.075/$0.30. "Um dev ativo consome ~R$ 20-80/dia de tokens. Compare com o salário-hora."

---

**#11 — Avançado: "Multimodalidade sem demonstração prática"** (Média)
> 16 horas de workshop e nenhum laboratório multimodal. Um lab de 10 min com print de erro seria memorável.

**Parecer do juiz**: **Acolho.** O impacto visual e pedagógico da multimodalidade ao vivo é altíssimo. Não precisa ser um laboratório completo — uma demo de 5 minutos já seria transformadora.
**Ação**: No Slide 1.2, demo ao vivo: tirar foto de um wireframe no quadro, colar no chat, pedir "gere HTML/CSS disso". Impacto garantido.

---

#### Slide 1.3 — As 4 Grandes Limitações

**#12 — Iniciante: "RAG usado como exemplo antes de ser definido"** (Alta)
> "Digitar 'Explique RAG' vs 'Explique RAG pra uma criança de 10 anos'". RAG? Estou no Módulo 1, RAG é Módulo 4.

**Parecer do juiz**: **Acolho com força.** Este é um erro didático clássico: usar conhecimento futuro como exemplo. O aluno se divide entre "preciso entender RAG" e "preciso entender sensibilidade ao prompt".
**Ação**: Trocar o exemplo para: "Explique SQL injection" vs "Explique SQL injection pra uma criança de 10 anos". Usar um termo que devs conhecem.

---

**#13 — Iniciante: "Mecanismo da data de corte nunca explicado"** (Baixa)
> Por que a IA tem data de corte? O conceito de "treinamento congelado" vs "inferência com acesso a dados" nunca fica explícito.

**Parecer do juiz**: **Acolho.** Uma frase resolve.
**Ação**: "O modelo foi treinado até uma data e depois 'congelado'. É como compilar um binário: ele não muda depois de compilado, a menos que você link bibliotecas externas (RAG, web search)."

---

**#15 — Intermediário: "Demo de alucinação usa storytelling, não evidência"** (Média)
> "Contar caso real" é relato anedótico. O público de devs precisa VER a alucinação acontecer.

**Parecer do juiz**: **Acolho.** A demonstração ao vivo de sensibilidade ao prompt está no roteiro — por que não fazer o mesmo para alucinações?
**Ação**: Demo ao vivo: "Me liste 3 artigos do Dr. Carlos Mendonça sobre redes neurais publicados em 2024 com DOI". Mostrar que a IA inventa. Depois: "Agora me mostre os links no Google Scholar." A IA admite que não existem.

---

**#16 — Avançado: "Taxonomia de alucinações ignorada"** (Alta)
> Alucinações têm tipos diferentes (intrínsecas, extrínsecas, factuais) e cada tipo tem estratégia de mitigação diferente. Tratar como um fenômeno único leva a aplicar a estratégia errada.

**Parecer do juiz**: **Acolho como nota de rodapé, não como conteúdo do slide.** A taxonomia completa sobrecarregaria o slide de fundamentos, mas o instrutor precisa saber para responder perguntas.
**Ação**: Nota de rodapé: "Se perguntarem: existem alucinações de factualidade (RAG resolve), de raciocínio (CoT resolve) e de fidelidade à fonte (validação cruzada resolve)."

---

#### Slide 1.4 — Pré-Treinamento, Fine-Tuning e RAG

**#17 — Iniciante: "Embedding mencionado sem definição"** (Alta)
> "Só custo de embedding + busca." Embedding? O que é isso? A explicação chega 4 módulos depois.

**Parecer do juiz**: **Acolho.** Este é o mesmo padrão da intervenção #12: mencionar conceitos futuros sem definição-relâmpago.
**Ação**: No card do RAG, adicionar: "Embedding = transformar texto em coordenadas numéricas (detalhes no Módulo 4)."

---

**#20 — Intermediário + #21 — Avançado: "Regra dos 95% sem evidência e dogmática"** (Alta/Média)
> Intermediário: A regra é apresentada como dogma, não como evidência. Avançado: Fine-tuning tem casos legítimos (estilo, latência, raciocínio sobre domínio inteiro). LoRA/QLoRA reduziu custo drasticamente.

**Parecer do juiz**: **Acolho a crítica do Intermediário (precisa de evidência), acolho parcialmente a do Avançado (não remover a regra, mas matizá-la).** A regra dos 95% é uma heurística excelente para evitar que devs pulem direto para fine-tuning — o que realmente acontece. Mas apresentar sem evidência e sem exceções enfraquece o argumento.
**Ação**: (1) Adicionar mini-matriz comparativa com números realistas: "Cenário: FAQ de 500 páginas. Fine-tuning: 4h prep, $40, re-treino a cada atualização. RAG: 30min setup, $0.50/mês, atualização instantânea." (2) Adicionar quadro "Quando fine-tuning faz sentido": estilo/tonalidade muito específico, latência baixíssima, raciocínio sobre domínio inteiro. (3) Mencionar LoRA/QLoRA como opção de custo reduzido.

---

#### Slide 1.5 — Quando NÃO Usar

**#22 — Iniciante: "Não-determinismo jogado sem explicação"** (Baixa)
> Por que a IA é não-determinística? Conexão "modelo probabilístico → não-determinismo" merece 30 segundos.

**Parecer do juiz**: **Acolho.** Trinta segundos resolvem.
**Ação**: "A IA é não-determinística porque escolhe tokens com base em probabilidades, não em regras fixas. A mesma pergunta pode gerar respostas diferentes."

---

### Módulo 2 — Ecossistema Open-Source

#### Slide 2.2 — Ollama e Hugging Face

**#23 — Avançado: "Ollama omite limitações para produção"** (Média)
> Ollama é ótimo para dev local, mas para produção: vLLM, TGI, llama.cpp server mode.

**Parecer do juiz**: **Acolho como nota de rodapé.** O foco do workshop é desenvolvimento, não produção. Mas mencionar que existem alternativas para produção é honesto e útil.
**Ação**: Nota: "Ollama é perfeito para dev. Para produção com alta concorrência: vLLM ou llama.cpp server mode. A API é compatível."

---

#### Slide 2.3 — Parâmetros

**#24 — Iniciante: "Sopa de letrinhas"** (Média)
> SLM, Phi-3, Llama 8B — três coisas novas de uma vez.

**Parecer do juiz**: **Acolho.** Expandir acrônimos e explicar notações é barato e resolve.
**Ação**: "SLM = Small Language Model. Ex: Phi-3 (Microsoft), Llama 8B (Meta). '8B' = 8 bilhões de parâmetros. O GPT-4o tem centenas de bilhões."

---

**#25 — Iniciante: "Parâmetros definidos vagamente"** (Média)
> "Parâmetros são tipo neurônios." Para um dev, parâmetro = argumento de função.

**Parecer do juiz**: **Acolho.** A definição para devs deveria usar a linguagem deles.
**Ação**: "Parâmetros são pesos numéricos que a rede ajusta durante o treinamento. São como coeficientes de uma regressão: y = ax + b tem 2 parâmetros. Uma LLM tem bilhões."

---

**#26 — Avançado: "Remover parâmetros melhora sem contexto"** (Baixa)
> Isso é pruning/model compression. Não é qualquer remoção que melhora.

**Parecer do juiz**: **Acolho como nota de rodapé.** O ponto principal ("não assuma que maior é melhor") permanece válido.
**Ação**: Nota: "Isso se refere a técnicas de pruning estruturado. Não é que qualquer remoção melhora — são técnicas com critérios rigorosos."

---

### Módulo 3 — Prompt Engineering

#### Slide 3.1 — Os 5 Elementos

**#27 — Intermediário: "Slide não contém template reutilizável"** (Alta)
> O dev que tirar print leva uma lista abstrata, não um template pronto para copiar e adaptar.

**Parecer do juiz**: **Acolho com força.** Esta é a intervenção mais importante do Módulo 3. O slide explica O QUE mas não entrega O COMO. Um template literal no slide multiplica a utilidade prática.
**Ação**: Adicionar ao slide um card com template copiável:
```
[ROLE] Você é um dev sênior especialista em [tecnologia]
[CONTEXTO] Projeto: [stack, versões]. Restrição: [limite]
[INSTRUÇÃO] [Verbo: Refatore/Implemente/Explique] o [alvo]
[RESTRIÇÕES] NÃO use [X]. Mantenha [Y].
[FORMATO] Retorne [código/json/tabela] com [estrutura]
```

---

#### Slide 3.2 — Frameworks RTF, CARE, RISE

**#28 — Intermediário: "Frameworks descritos mas sem prompt real"** (Alta)
> Os exemplos são tópicos ("Gerar Dockerfile"), não prompts. O aluno sai sabendo o que RTF significa mas não como escrever um.

**Parecer do juiz**: **Acolho com força.** Mesmo padrão da #27.
**Ação**: Substituir tópicos genéricos por prompts completos dentro de cada card. Exemplo para RTF:
```
Role: Você é um dev DevOps
Task: Gere um Dockerfile multi-stage para API Go 1.22
Format: Apenas o Dockerfile em markdown com comentários
```

---

#### Slide 3.3 — Técnicas de Raciocínio

**#29 — Iniciante: "Zero-shot, Few-shot, CoT não desempacotados"** (Alta)
> "Zero-shot" — zero o quê? "Few-shot" — poucos o quê? "Chain of Thought" — nome em inglês adiciona barreira.

**Parecer do juiz**: **Acolho.** Os nomes não são óbvios e a etimologia ajuda a fixar.
**Ação**: "Zero-shot = zero exemplos (instrução direta). Few-shot = poucos exemplos (mostra 2-3). Chain of Thought = cadeia de raciocínio (mostra o passo a passo)."

---

**#30 — Intermediário: "Demo de CoT sem exemplo no slide"** (Média)
> Se a demo falhar ou o tempo apertar, o conceito mais importante do módulo fica sem evidência.

**Parecer do juiz**: **Acolho.** Slides devem ser autossuficientes como referência futura, independentemente da demo ao vivo.
**Ação**: Incluir no slide um exemplo de problema de lógica com resposta errada (sem CoT) vs correta (com CoT).

---

#### Slide 3.5 — Cheat Sheet

**#31 — Intermediário: "Cheat sheet não integra frameworks com técnicas"** (Baixa)
> A árvore de decisão cobre frameworks mas não orienta quando usar Zero-shot vs Few-shot vs CoT.

**Parecer do juiz**: **Acolho.**
**Ação**: Adicionar segunda camada à árvore: "Tarefa analítica/diagnóstica? → Adicione CoT. Precisa de estilo/convenção específica? → Adicione Few-shot."

---

#### Laboratório Módulo 3

**#32 — Intermediário: "RISE+CoT é ordens de grandeza mais complexo"** (Média)
> SQL com RTF = 3-5 min. Migração com CARE = 10-15 min. Bug multi-arquivo com RISE+CoT = 30 min sozinho.

**Parecer do juiz**: **Acolho.** O terceiro cenário é desproporcionalmente mais complexo que os outros dois.
**Ação**: Fornecer o cenário RISE+CoT pré-mordido: repositório de exemplo com bug conhecido e template RISE parcialmente preenchido. O foco vai para a técnica, não para entender o código do zero.

---

### Módulo 4 — RAG, Embeddings e Engenharia de Contexto

#### Slide 4.2 — Pipeline RAG em 5 Etapas

**#33 — Intermediário: "Pipeline sem uma linha de código"** (Alta)
> Devs aprendem vendo código. Explicar "cosine similarity" sem mostrar a chamada de função é garantia de que o conceito não será retido.

**Parecer do juiz**: **Acolho com força.** Esta é a intervenção mais importante do Módulo 4. O workshop é para devs. Código é a língua materna deles.
**Ação**: Incluir mini-snippet de 8 linhas no slide:
```python
chunks = text_splitter.split(document)
embeddings = model.encode(chunks)
vector_db.add(embeddings, chunks)
results = vector_db.search(model.encode(query), top_k=3)
prompt = f"Context: {results}\n\nQuestion: {query}"
```

---

**#34 — Iniciante: "Embeddings chamados de mágica"** (Alta)
> Chamar de "mágica" sugere que é incompreensível. Mas embeddings são álgebra linear.

**Parecer do juiz**: **Acolho.** "Mágica" é a palavra errada para uma plateia de devs. Eles querem entender o mecanismo.
**Ação**: "Embeddings são o mecanismo que transforma texto em coordenadas numéricas. Pensa no GPS: 'cachorro' e 'gato' recebem coordenadas próximas."

---

**#35 — Iniciante: "Cosseno sem contexto matemático"** (Alta)
> "Cosseno" me remete a trigonometria do ensino médio. O que tem a ver com similaridade de textos?

**Parecer do juiz**: **Acolho.** A explicação visual resolve.
**Ação**: "Cada embedding é uma seta saindo da origem. Se duas setas apontam na mesma direção (ângulo pequeno), os textos são similares. Cosseno do ângulo mede isso: cos(0°)=1 (idêntico), cos(90°)=0 (não relacionado)."

---

**#38 — Avançado: "Estratégias de chunking e hybrid search omitidas"** (Alta)
> Chunking semântico > chunking por tamanho. Overlap 10-20%. Hybrid search (BM25 + embeddings) consistentemente outperform embeddings puros em benchmarks (BEIR).

**Parecer do juiz**: **Acolho como nota de rodapé.** Essas 3 técnicas separam um POC de um sistema de produção. Não precisam ser explicadas em profundidade, mas devem ser mencionadas.
**Ação**: Adicionar ao slide: "Avançado: chunking semântico (por parágrafo/seção), overlap 10-20% entre chunks, hybrid search (BM25 + embeddings)."

---

#### Slide 4.3 — Embeddings

**#39 — Iniciante: "PCA nunca explicado"** (Alta)
> PCA é uma sigla para Principal Component Analysis. Um dev que nunca fez dados não sabe o que é.

**Parecer do juiz**: **Acolho.** Mesmo padrão das intervenções #12, #17: siglas sem expansão.
**Ação**: "PCA (Principal Component Analysis) comprime 768 dimensões em 2, preservando distâncias relativas. É como tirar uma foto 3D e imprimir em 2D."

---

**#40 — Avançado: "768+ números desatualizado"** (Média)
> Em 2025: text-embedding-3-small (512 dim), text-embedding-3-large (3072 com Matryoshka), Cohere (1024), Jina, E5 Mistral. Matryoshka embeddings permitem truncar dimensionalidade.

**Parecer do juiz**: **Acolho.** A informação está factualmente desatualizada e Matryoshka embeddings são uma inovação relevante.
**Ação**: Atualizar: "Dimensões típicas: 512 a 4096. Modelos com Matryoshka embeddings (OpenAI 2024) permitem reduzir dimensionalidade sem perder qualidade proporcional."

---

#### Slide 4.4 — Graph RAG

**#42 — Intermediário + #43 — Avançado: "Graph RAG em 10 min é avançado demais e omite custo"** (Média)
> Intermediário: 10 minutos, sem lab, é garantia de esquecimento. Avançado: Custo de implementação é 5-10x maior que RAG tradicional.

**Parecer do juiz**: **Acolho.** Se é avançado demais para o escopo, que seja honesto sobre isso.
**Ação**: Reduzir para 2-3 minutos como "para onde ir depois": mencionar o paper do Microsoft GraphRAG (2024), linkar o repo, e alertar sobre o custo 5-10x maior. Não tentar ensinar o conceito.

---

#### Slide 4.5 — Engenharia de Contexto

**#44 — Intermediário: "Maior diferencial recebe só 10 minutos"** (Alta)
> Se contexto é o MAIOR diferencial, por que recebe 10 minutos?

**Parecer do juiz**: **Acolho.** Este slide deveria ser uma ponte explícita para o Módulo 6, não um aperitivo apressado.
**Ação**: Separar: regra dos 40% (5 min com demo: prompt com 80% vs 40% da janela) + teaser de progressive disclosure (5 min: "Vamos implementar isso com skills modulares no Módulo 6").

---

**#45 — Avançado: "Regra dos 40% sem suporte empírico"** (Média)
> É heurística do Waldemar, não tem respaldo em papers. Modelos 2025 mantêm performance até 50-70% (RULER benchmark).

**Parecer do juiz**: **Acolho como nota de rodapé.** O princípio é válido; o número exato é heurístico.
**Ação**: Nota: "40% é heurística conservadora baseada em experiência prática. O benchmark RULER mostra que modelos modernos mantêm performance até 50-70%. O princípio (não lotar a janela) é o que importa."

---

### Módulo 5 — MCP e Agentes

#### Slide 5.1 — MCP: A Tomada Universal

**#46 — Avançado: "Padrão da indústria ignora fragmentação real"** (Alta)
> Copilot usa protocolo próprio (Copilot Extensions), não MCP nativo. OpenAI tem function calling, Google tem A2A. Não é "padrão universal".

**Parecer do juiz**: **Acolho.** A afirmação "todos usam MCP" é factualmente imprecisa e um aluno que usa Copilot vai perceber.
**Ação**: "MCP é o protocolo mais adotado em 2026, criado pela Anthropic e suportado nativamente por Cursor, Claude Code, Cline. O Copilot suporta via adaptadores. OpenAI e Google têm protocolos próprios. Mas o MCP é o que tem ganhado mais tração na comunidade open-source."

---

#### Slide 5.3 — Agentes: Os 4 Componentes

**#47 — Avançado: "Frameworks de agentes omitidos"** (Alta)
> Nenhuma menção a LangGraph, CrewAI, AutoGen, Swarm, Mastra. O "modo agente" da IDE é um caso particular.

**Parecer do juiz**: **Acolho.** O aluno vai encontrar esses frameworks na primeira busca por "how to build AI agents".
**Ação**: Adicionar quadro "Frameworks em 2026": LangGraph (grafos de estado, melhor para workflows complexos), CrewAI (multi-agente com roles, prototipagem), AutoGen (Microsoft, conversação multi-agente). Mini-slide ou menção de 3 minutos.

---

**#48 — Avançado: "Segurança de agentes completamente omitida"** (Alta)
> Prompt injection via ferramentas, tool poisoning, excessive agency. Tópicos de pesquisa ativa. Essenciais para produção.

**Parecer do juiz**: **Acolho com força.** Esta é uma das omissões mais graves do workshop. Um dev que sai sem ouvir falar de prompt injection vai aprender da pior forma: em produção.
**Ação**: Adicionar slide/seção "Segurança de Agentes": (1) prompt injection via dados externos, (2) princípio de menor privilégio, (3) human-in-the-loop para ações destrutivas, (4) circuit breakers / rate limiting. Referenciar OWASP Top 10 for LLM Applications.

---

#### Slide 5.4 — O Loop do Agente

**#49 — Intermediário: "Loop sem trace concreto"** (Média)
> O dev que nunca viu agente não visualiza as 4 fases sem exemplo.

**Parecer do juiz**: **Acolho.**
**Ação**: Incluir trace real: "Corrija o bug no arquivo X. (1) PLAN: Vou ler X, identificar, editar, testar. (2) EXECUTE: [Read, Edit]. (3) OBSERVE: Teste falhou na linha Y. (4) REPLAN: Corrigir linha Y."

---

**#51 — Avançado: "Loops infinitos, custo explosivo, task drift não mencionados"** (Alta)
> Três problemas que todo dev encontra na primeira semana com agentes em produção.

**Parecer do juiz**: **Acolho.** Esses problemas são inevitáveis e os alunos precisam saber que existem e como mitigar.
**Ação**: Adicionar "O que pode dar errado": (1) loop infinito → max_iterations obrigatório, (2) custo explosivo → budget cap, (3) task drift → checkpoint a cada N iterações.

---

#### Slide 5.5 — MCP vs Skill vs API

**#52 — Iniciante: "Skill usado antes de ser definido"** (Alta)
> "Dado que MUDA → MCP. Conhecimento ESTÁVEL → Skill." Skill? O que é skill? Só é explicada no Módulo 6.

**Parecer do juiz**: **Acolho com força.** Este é o exemplo mais claro do problema transversal #72: "menciona cedo, explica tarde".
**Ação**: Opção A: Mover a comparação MCP vs Skill vs API para o Módulo 6. Opção B: Adicionar definição-relâmpago: "Skill = conhecimento encapsulado e estável (ex: como criar testes e2e). Detalhes no Módulo 6."

---

### Módulo 6 — Arquitetura de Contexto

#### Slide 6.1 — Evolução 2023-2026

**#54 — Avançado: "Narrativa linear não reflete realidade"** (Baixa)
> Em 2026, todos os 3 padrões ainda coexistem. Não é que a indústria "chegou" na Fase 3.

**Parecer do juiz**: **Acolho como nuance, não como correção.** A narrativa é didaticamente útil; a nuance é para o instrutor.
**Ação**: Nota: "Essa é a trajetória dos times mais avançados. Em 2026, os 3 padrões coexistem. A Fase 3 é onde você quer estar."

---

#### Slide 6.2-6.3 — Rules e Agents.md

**#55 — Iniciante: "Agents.md, CLAUDE.md, claude onboard sem contexto"** (Média)
> O que é Agents.md? Onde coloco? O nome é específico do Claude Code.

**Parecer do juiz**: **Acolho.**
**Ação**: "Ferramentas de IA leem um arquivo de configuração na raiz do projeto. No Claude Code: CLAUDE.md. No Cursor: .cursorrules. A ideia é a mesma: um README para IAs."

---

#### Slide 6.5 — Sub-agents

**#56 — Avançado: "Não crie sub-agents é dogmático"** (Alta)
> Existem casos legítimos: system prompt especializado, ferramentas restritas, modelos diferentes. A regra "NAO crie customizados" joga o bebê fora.

**Parecer do juiz**: **Acolho.** A regra absoluta é compreensível como reação ao trauma de super-agentes de 3000 linhas, mas é dogmática demais.
**Ação**: "Regra geral: comece com genéricos. Customize APENAS quando precisar de system prompt especializado, ferramentas restritas ou modelo diferente. 80% dos casos não precisam. Se você se vê criando 3000 linhas, pare e quebre em skills menores."

---

**#57 — Avançado: "Contradiz documentação do Claude Code"** (Média)
> O checklist diz "NAO crie customizados" mas o Claude Code suporta e incentiva `.claude/agents/*.md`.

**Parecer do juiz**: **Acolho.** A recomendação do workshop contradiz a ferramenta que ele recomenda.
**Ação**: Unificar com a reformulação da #56.

---

**#58 — Intermediário: "Sobreposição conceitual com Módulos 4 e 5"** (Média)
> "Progressive disclosure" (M4.5) = "skills modulares" (M6.4). "Contexto controlado" (SDD, M7) = "cada fase tem contexto reduzido" (M6).

**Parecer do juiz**: **Acolho.** A repetição pode ser reforço ou redundância — depende de pontes explícitas.
**Ação**: Mapear conexões no material do instrutor: "Slide 4.5 → Módulo 6", "Slide 7.4 → Módulo 5.4". Transformar repetições em reforço estruturado.

---

### Módulo 7 — SDD e Ferramentas

#### Slide 7.1 — Por que Prompt Direto Falha

**#60 — Intermediário: "Solução é 'use SDD' sem primeira ação"** (Média)
> Se o dev sair desse slide e tentar aplicar SDD, não sabe por onde começar.

**Parecer do juiz**: **Acolho.**
**Ação**: Adicionar ao rodapé: "Primeiro passo: `Escreva uma spec com user stories, metas e fora de escopo para [feature X]`."

---

#### Slide 7.2 — SDD: As 4 Fases

**#61 — Intermediário: "spec.md, design.md, tasks.md referenciados mas não mostrados"** (Alta)
> O slide referencia arquivos concretos mas não mostra o CONTEÚDO de nenhum deles.

**Parecer do juiz**: **Acolho com força.** Esta é a intervenção mais importante do Módulo 7. Os artefatos do SDD são a ponte entre teoria e prática e precisam existir como templates.
**Ação**: Criar 4 templates para o material do aluno: `spec.template.md`, `design.template.md`, `tasks.template.md`, `STATE.template.md`. Referenciá-los nos slides.

---

#### Slide 7.3 — STATE.md e Documentação

**#62 — Intermediário + #63 — Iniciante: "STATE.md sem exemplo concreto"** (Alta/Média)
> Dois agentes independentes: o STATE.md é explicado em abstrato mas nunca mostrado.

**Parecer do juiz**: **Acolho com força.** Um exemplo de 10 linhas no slide transformaria o conceito abstrato em ferramenta concreta.
**Ação**: Mostrar mini-exemplo no slide:
```markdown
# STATE.md — 2026-07-08
## Done
- [x] Auth refactor — extraído JWT middleware
## Doing
- [ ] Cache layer — investigando Redis vs Memcached
## Blockers
- Timeout no endpoint /users — aguardando DBA
```

---

#### Slide 7.5 — Ferramentas

**#66 — Intermediário + #67 — Avançado: "Ferramentas sem critérios objetivos"** (Média)
> Intermediário: Analogia de carros não ajuda na decisão real. Avançado: Omite categorias (CodeRabbit, Devi, Lovable, Zed) e info desatualizada sobre Copilot Agent Mode.

**Parecer do juiz**: **Acolho.** A tabela do conteúdo programático já tem critérios melhores que o slide.
**Ação**: Adicionar mini-tabela comparativa: Setup, Custo/mês, MCP nativo, Modo agente, Open-source. Atualizar info do Copilot (Agent Mode já existe em 2026).

---

#### Slide 7.6 / Laboratório — Workshop Prático Final

**#68 — Intermediário: "10 min para Specify é irrealista"** (Alta)
> 10 minutos para escrever spec de qualidade é extremamente agressivo. Risco: specs superficiais, exercício vira teatro.

**Parecer do juiz**: **Acolho.** Tempos muito apertados comprometem a qualidade do exercício.
**Ação**: Opção A: Reescalonar para 70 min (15/15/15/20/5). Opção B: Fornecer o requisito PRE-WORKSHOP para que cheguem ao Módulo 7 já tendo pensado no problema.

---

**#69 — Intermediário: "Resumo final omite Módulos 2, 3, 4, 5"** (Baixa)
> Três ideias centrais mencionam M1, M6, M7. Os módulos 2-5 desaparecem.

**Parecer do juiz**: **Acolho.**
**Ação**: Reescrever com 5 ideias: (1) LLMs = completadores (M1), (2) Frameworks + técnicas de prompt (M3), (3) RAG resolve 95% (M4), (4) MCP + Skills + Sub-agents (M5+M6), (5) SDD + RPI + STATE.md (M7).

---

## Melhorias Transversais

### 1. Templates e exemplos concretos são a maior carência (3/3 agentes)

**Evidência**: Intervenções #27, #28, #33, #61, #62, #74 — 6 intervenções de Alta gravidade sobre o mesmo tema.

**Diagnóstico**: Os slides explicam O QUE mas não mostram O COMO. Devs aprendem por exemplos e templates que possam adaptar. O material atual é rico em conceitos e analogias mas pobre em artefatos reutilizáveis.

**Ação sistêmica**:
- Criar templates para: prompt de 5 elementos, RTF/CARE/RISE preenchidos, spec.md, design.md, tasks.md, STATE.md
- Todo slide que introduz um artefato deve conter um exemplo real de 3-10 linhas
- Distribuir os templates como parte do material do aluno (não só como slide)

---

### 2. Conceitos mencionados antes de serem definidos (2/3 agentes)

**Evidência**: Intervenções #1, #3, #12, #17, #22, #24, #29, #39, #52 — 9 intervenções sobre menção precoce de termos.

**Diagnóstico**: O workshop tem estrutura em espiral (menciona cedo, explica tarde), mas as menções precoces não vêm com definições-relâmpago. Isso gera ansiedade no iniciante.

**Ação sistêmica**:
- Para todo termo mencionado antes do seu módulo: adicionar definição de 1 frase + "detalhes no Módulo X"
- Adicionar notas de rodapé visuais nos slides: "RAG → Módulo 4", "Embeddings → Módulo 4", "SDD → Módulo 7"
- Criar glossário de 1 página no material do aluno com todos os termos e o módulo onde são explicados

---

### 3. Desequilíbrio teoria/prática (2/3 agentes)

**Evidência**: Intervenções #73, #81 — 71% teoria / 29% prática.

**Diagnóstico**: Para um workshop que se propõe prático ("Da base à prática"), o balanço é desfavorável. Laboratórios são bem desenhados conceitualmente mas curtos demais para a complexidade.

**Ação sistêmica**:
- Meta: 60% teoria / 40% prática (ganho de ~1h50 de lab adicional)
- Transformar algumas explicações teóricas em "labs guiados" (instrutor faz ao vivo, alunos reproduzem)
- Oferecer notebooks/ambientes pré-configurados para eliminar tempo de setup
- Para labs mais complexos (RAG, SDD), fornecer templates e cenários pré-mordidos

---

### 4. Fontes 100% YouTube, zero documentação oficial ou papers (1 agente)

**Evidência**: Intervenção #76 — Todas as referências são vídeos dos mesmos 2 autores.

**Diagnóstico**: Para um workshop de 16h voltado a devs profissionais, a ausência de referências a documentação oficial, papers seminais e benchmarks reduz a credibilidade e deixa o aluno sem caminho de aprofundamento.

**Ação sistêmica**:
- Adicionar seção "Para se aprofundar" com: papers (Attention is All You Need, Lost in the Middle, GraphRAG, SWE-bench), documentação oficial (MCP spec, Ollama docs, OpenAI/Anthropic prompting guides), benchmarks (Chatbot Arena, SWE-bench, MTEB, BEIR)
- Manter os vídeos como referência primária (são bons), mas complementar com fontes diversas

---

### 5. Segurança de agentes completamente ausente (1 agente)

**Evidência**: Intervenção #48 — Prompt injection, tool poisoning, excessive agency nunca mencionados.

**Diagnóstico**: Esta é a omissão mais grave do workshop. Um aluno que sai sem conhecer esses riscos vai encontrá-los em produção, potencialmente com consequências sérias.

**Ação sistêmica**:
- Adicionar 15-20 minutos sobre segurança de agentes no Módulo 5
- Cobrir: prompt injection via ferramentas, princípio de menor privilégio, human-in-the-loop, circuit breakers
- Referenciar OWASP Top 10 for LLM Applications

---

### 6. OpenCode como dependência única (1 agente)

**Evidência**: Intervenção #2 — Potencial conflito de interesses e exclusão de usuários de outras ferramentas.

**Diagnóstico**: A escolha de uma ferramenta única para padronizar laboratórios é didaticamente válida. O problema é não oferecer caminhos alternativos.

**Ação sistêmica**:
- Criar apêndice de 1-2 páginas: "Equivalentes em outras ferramentas" (Cursor, Claude Code, Copilot)
- Para cada laboratório, adicionar 2-3 linhas: "Se você usa Cursor: faça X. Se usa Claude Code: faça Y."
- Declarar transparência: "OpenCode é a ferramenta do autor e tem suporte nativo aos conceitos. Os mesmos princípios se aplicam às demais."

---

### 7. Ausência de métricas e avaliação (1 agente)

**Evidência**: Intervenções #75, #79 — Nenhum módulo sobre como avaliar se a IA está gerando código bom.

**Diagnóstico**: O aluno sai capaz de construir com IA mas incapaz de medir se está melhorando ou piorando.

**Ação sistêmica**:
- Adicionar mini-seção de 20-30 min: "Avaliando o que a IA Gera"
- Cobrir: LLM-as-Judge, RAGAS (faithfulness, answer relevancy), benchmarks de código (HumanEval, SWE-bench)
- Integrar métricas nos laboratórios: "Além de executar, meça a qualidade com RAGAS"

---

### 8. Prompt Caching nunca mencionado (1 agente)

**Evidência**: Intervenção #78 — Técnica #1 para reduzir custos em 2025-2026 completamente ausente.

**Diagnóstico**: Prompt caching é a conexão direta entre "Arquitetura de Contexto" (M6) e "Custo" (M1) que o workshop perde. Explicar que Agents.md cacheado reduz custo em ~90% tornaria o Módulo 6 muito mais concreto.

**Ação sistêmica**:
- Adicionar 3-5 minutos no Módulo 6: "Prompt caching: o Agents.md é enviado como prefixo em toda conversa. As APIs (Anthropic, OpenAI, Google) cacheiam esse prefixo e cobram ~90% menos. Um Agents.md de 200 linhas cacheado custa centavos por sessão."
- Mencionar também no Módulo 1 (Slide 1.2) ao falar de custos

---

## Síntese Final

### O que está EXCELENTE (não mexer)

1. **Modelo mental "IA = autocomplete"** — base conceitual raramente ensinada e extremamente útil
2. **Ênfase em contexto como diferencial** — relevante, pragmática e bem posicionada
3. **Arquitetura dos 4 pilares** (Rules/Skills/MCPs/Sub-agents) — contribuição original e bem estruturada
4. **SDD + STATE.md** — resolve problema real de perda de contexto entre sessões
5. **Tom pragmático anti-hype** ("regex resolve, não use IA") — saudável e necessário
6. **Analogias principais** (autocomplete, chef, restaurante, casa) — eficazes para introduzir conceitos
7. **Estrutura modular** — permite que o aluno volte a módulos específicos como referência

### O que PRECISA ser corrigido (Alta gravidade, baixo esforço)

1. **Adicionar templates concretos em todos os slides de frameworks/artefatos** — 6 intervenções de Alta
2. **Inserir definições-relâmpago para termos mencionados antes do seu módulo** — 9 intervenções
3. **Trocar exemplos que usam conhecimento futuro** (RAG no M1, Skill no M5)
4. **Adicionar exemplos de código nos slides do pipeline RAG**
5. **Criar templates spec.md, design.md, tasks.md, STATE.md para o material do aluno**

### O que DEVE ser considerado (Alta gravidade, médio/esforço)

6. **Adicionar 15-20 min de segurança de agentes** (prompt injection, tool poisoning)
7. **Adicionar 20-30 min de avaliação e métricas** (RAGAS, LLM-as-Judge)
8. **Rebalancear teoria/prática para 60/40** (expandir labs ou encurtar teoria)
9. **Oferecer equivalentes de laboratório para Cursor/Claude Code/Copilot**
10. **Diversificar referências** (adicionar papers, docs oficiais, benchmarks)

### O que é recomendado (Média gravidade)

11. **Mencionar prompt caching** (conexão Arquitetura↔Custo)
12. **Atualizar informação de ferramentas** (Copilot Agent Mode, Matryoshka embeddings, dimensões)
13. **Mapear conexões entre módulos** (progressive disclosure↔skills, RPI↔loop do agente)
14. **Adicionar demo multimodal ao vivo** (print de wireframe → HTML/CSS)
15. **Revisar analogia do GPS** (substituir ou refinar)

---

## Nota do Juiz

Este relatório compila 83 intervenções de 3 perfis diferentes de alunos. Nem toda intervenção tem o mesmo peso, e algumas são contraditórias entre si (ex: o Avançado quer mais precisão técnica; o Iniciante quer mais explicações básicas). Como juiz, procurei:

- **Acolher** quando a intervenção identifica um problema real que prejudica a compreensão ou aplicabilidade, independentemente do perfil do agente
- **Acolher como nota de rodapé** quando a intervenção é tecnicamente correta mas adicioná-la ao slide principal prejudicaria os iniciantes — nestes casos, a informação vai para o guia do instrutor
- **Acolher parcialmente** quando a intervenção tem mérito mas precisa de nuance (ex: a regra dos 95% é dogmática, mas o dogma tem função didática)
- **Discordar** apenas quando a intervenção vai contra escolhas pedagógicas intencionais e bem fundamentadas

O workshop tem qualidades excepcionais: o modelo mental correto sobre LLMs, a ênfase em contexto, a arquitetura dos 4 pilares e o SDD com STATE.md são contribuições genuínas. As correções sugeridas aqui visam fortalecer esses pontos fortes, não substituí-los.

**Prioridade máxima para a próxima iteração**: templates concretos, definições-relâmpago, segurança de agentes e métricas de avaliação.
