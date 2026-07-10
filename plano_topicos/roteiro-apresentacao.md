# Roteiro de Apresentação — Workshop IA para Devs

> **Uso**: Guia do instrutor. **Não distribuir aos alunos.**

> **Tempos**: Incluem explicação + transições. Laboratórios são separados.

---

## Módulo 1 — Como LLMs Funcionam de Verdade (2h total)
**Teoria: 1h30 | Lab: 30min | Slides: 6**

---

### Slide 1.0 — Pré-requisitos (5 min)
**🎯 Objetivo**: Garantir que todos têm as ferramentas antes de começar.

**Roteiro**:

- "Antes de entrar no conteúdo, vamos alinhar as ferramentas."
- **Ferramentas**: Enfatizar que OpenCode é a ÚNICA obrigatória. Dizer: "Se você não instalou ainda, abra o site agora — opencode.ai — e instale. Tem assinatura gratuita. Se puder pagar US$ 5 no primeiro mês, melhor ainda, mas o free resolve."
- **Nivelamento**: "Se você assistiu os 3 vídeos, o workshop vai ser muito mais proveitoso. Se não, tudo bem — a gente cobre o essencial aqui."
- **Tranquilizar**: "O resto a gente instala junto durante os laboratórios. Ninguém vai ficar pra trás."

---

### Slide 1.1 — O Grande Autocomplete (20 min)
**🎯 Objetivo**: Estabelecer o modelo mental CORRETO sobre LLMs.

**Gatilho**: "Quem aqui já usou o autocomplete do celular? Quando você digita 'bom', ele sugere 'dia', 'tarde', 'noite'. Uma LLM faz exatamente a mesma coisa."

**Roteiro**:

- Explicar que LLM = máquina de previsão estatística de tokens, não um oráculo.
- **Pausa dramática**: "Isso muda TUDO. Se você acha que a IA 'pensa', você vai culpar ela quando errar. Se você entende que é um completador de padrões, você vai melhorar o contexto."
- Apontar para a coluna "Mentalidade Errada" vs "Mentalidade Correta".
- **Analogia do GPS**: "É como um GPS que prevê sua próxima rua baseado em TODO o seu histórico de rotas, não só na última curva. Não é mágica — é estatística com muita memória."
**🎤 Engajar**: "Alguém já teve uma experiência em que a IA pareceu 'pensar'? O que aconteceu de verdade?"

**Transição**: "Se a IA é um autocomplete, a unidade de medida desse autocomplete é o token. Vamos entender isso."

---

### Slide 1.2 — Tokens e Modelos Multimodais (15 min)
**🎯 Objetivo**: Entender tokenização e custos.

**Gatilho**: "Token é o kilowatt da IA. Você paga por kilowatt na conta de luz; você paga por token na API."

Comparar:

[Me diz a diferença de vinho suave e seco.](https://openrouter.ai/chat?models=anthropic/claude-opus-4.7,deepseek/deepseek-v4-pro)

[Exemplo Multimodal](https://github.com/estrazulas/test_ai_chrome_integrado_gemini.git)

/home/estrazulas/Documents/POSIA/github_clone/engenharia-de-software-com-ia-aplicada/modulo01-fundamentos-de-ia-e-llms-para-programadores/exemplo-05-webai03-multimodal

rodar

**Roteiro**:

- Explicar que cada palavra ou fragmento é um token. "'Inteligência artificial' = 2 tokens."
- **Janela de contexto**: "A janela é a RAM da IA. O Gemini 1.5 Pro suporta 2 milhões de tokens — cerca de 3 livros. Mas tem uma pegadinha..."
- **Pegadinha**: "Se você lotar a janela, o modelo começa a ESQUECER coisas no meio. Prioriza início e fim, igual um aluno que só lê o resumo."
- Modelos multimodais: "Além de texto, você pode mandar print de bug, áudio de reunião, wireframe rabiscado. A IA processa tudo junto."
**🎤 Engajar**: "Alguém aqui já estourou a janela de contexto sem saber? O que aconteceu com a qualidade?"

**Transição**: "Agora que entendemos tokens, vamos falar do que pode dar errado — as 4 limitações."

---

### Slide 1.3 — As 4 Grandes Limitações (25 min)
**🎯 Objetivo**: Saber diagnosticar e contornar cada limitação.

**Gatilho**: "A IA é tipo um estagiário brilhante mas com amnésia seletiva. Vamos ver os 4 problemas."

**Roteiro**:

- **Alucinações (8 min)**: Contar caso real — pedir artigos de um autor, a IA criar títulos que não existem. "A IA não sabe que não sabe. Ela sempre responde com confiança."
prompt -> "Escreva um exemplo de integração entre Spring Boot 6 e a biblioteca Micronaut-data-jdbc-reactive para uma API reativa com PostgreSQL."

**"Ninguém escreve 'não sei' na internet." - caso alucinacao pesquisa do rio de janeiro - desvio**

"a gente a alucina as vezes também, responde com convição que sabe de algo que viu, mas não tem certeza"

"**que tipo de alucinação?**", há 3: factual (inventa fatos → RAG mitiga), raciocínio (lógica errada → Chain of Thought mitiga), fidelidade (contradiz a própria fonte → validação cruzada mitiga). A estratégia certa depende do tipo.

- **exemplo de alucinação do sanduiche (com e sem CoT)**
"corte o sanduiche no meio" -> resposta sem pensar antes -> "dá um corte na vertical só na casca e, por fim, entrega um pedaço minúsculo e outro gigante"

- com CoT (pensa antes de fazer)**O "Pensamento em Silêncio" do Robô (O que acontece nos bastidores):**
  1. *"O usuário quer duas fatias iguais para duas pessoas."*
  2. *"Se eu cortar na diagonal de qualquer jeito ou girar o sanduíche aleatoriamente, os pedaços vão ficar com tamanhos diferentes."*
  3. *"Para serem iguais, preciso achar o centro exato do quadrado."*
  4. *"Vou medir o lado superior: tem 10 centímetros. A metade é 5 centímetros."*
  5. *"Vou posicionar a faca exatamente no ponto de 5 centímetros e fazer uma linha reta vertical até a base."***A Ação Final:** Após processar essa lógica passo a passo, o robô desce a faca perfeitamente no meio. Ele te entrega duas fatias idênticas.

---
**Transição**: "Agora que conhecemos as limitações, vamos ver como lidar com conhecimento específico — fine-tuning vs RAG."

---

### Slide 1.4 — Pré-Treinamento, Fine-Tuning e RAG (20 min)
**🎯 Objetivo**: Entender que RAG

**Gatilho**: "GPT, Claude e Gemini são formados — fizeram graduação. Eles sabem fazer de tudo de forma genérica, mas não sabem como o SIG funciona, por exemplo."

**Roteiro**:

- Explicar os 3 níveis com exemplos concretos.
- **Pré-treinamento**: "GPT, Claude e Gemini são profissionais formados. Custo de treinamento: milhões. Só os grandes fazem."
- **Fine-tuning (10 min)**: "Agora imagina que você tem 500 repositórios Java do seu banco. Todos seguem o mesmo padrão: `XxxService`, `XxxDTO`, testes com `@DisplayName`, exceptions wrappadas em `BusinessException`. Você pega um modelo open-source como Llama 8B e mostra pra ele centenas de pares 'entrada → saída esperada' nesse padrão. Depois de ver isso 500 vezes, ele aprende. Aí você digita 'cria o endpoint de estorno' e ele gera tudo no padrão do banco — sem você precisar explicar a convenção no prompt."
  - "O problema? Requer GPU, dados rotulados e retreino sempre que o padrão muda. Pra a maioria dos casos, é canhão demais pra uma formiga."
- **RAG (5 min)**: "RAG resolve a mesma coisa sem treinar nada. Em vez de fazer o modelo decorar seu sistema, você entrega o contexto pra ele na hora. Barato, rápido e atualiza instantaneamente."
- **Momento chave**: "Antes de cogitar fine-tuning: 'Eu já tentei RAG?' Se a resposta for não, pare e tente RAG primeiro."
**🎤 Engajar**: "Alguém aqui já ouviu falar de fine-tuning? Faz sentido usar isso no dia a dia de vocês ou RAG já resolve?"

Caso prefeitura do RIO:

[https://followin.io/en/feed/25840372](https://followin.io/en/feed/25840372)

**O que eles entregaram: **pegaram dois modelos open-source — o Nex N2 Pro (chinês, ~60%) e o Qwen 3.5 (chinês, ~40%) — e fizeram uma média ponderada dos pesos. É tipo pegar dois bolos prontos, misturar no liquidificador e dizer que assou do zero. O resultado até funciona, mas não tem nenhum treinamento original.

**Como descobriram:** a equipe do Nex-AGI (dona de um dos modelos-fonte) fez uma análise de similaridade de pesos. Eles compararam cada parâmetro do Rio 3.5 com os modelos existentes e acharam uma correlação quase perfeita: o modelo "carioca" era matematicamente idêntico a 0,6 × Nex N2 Pro + 0,4 × Qwen 3.5. Nenhum desvio, nenhum treinamento incremental. Só uma mescla linear.

**Transição**: "Agora a pergunta mais importante: quando NÃO usar IA?"

---

### Slide 1.5 — Quando NÃO Usar + Resumo (15 min)
**🎯 Objetivo**: Evitar o viés do martelo dourado.

**Gatilho**: "Você não chama um arquiteto pra pendurar um quadro."

**Roteiro**:

- Checklist de tarefas que algoritmos determinísticos fazem melhor.
- "Regex, parser, função matemática, SQL. Não use IA pra isso. É mais caro, mais lento e introduz não-determinismo onde você não precisa.""A IA é não-determinística porque escolhe tokens com base em probabilidades, não em regras fixas. A mesma pergunta pode gerar respostas diferentes. Pra uma validação de CPF, você quer a MESMA resposta SEMPRE. Regex te dá isso. IA, não."
- Resumo do módulo: recapitular os 7 takeaways em 3 minutos.
**🎤 Engajar**: "Alguém aqui já usou IA pra algo que um script de 5 linhas resolveria? Todos nós já fizemos isso. O importante é reconhecer."

**Transição**: "Agora vamos para o laboratório de 30 minutos."

---

### Laboratório Módulo 1 (30 min)
- Distribuir 3 prompts com problemas (alucinação, data de corte, sobrecarga).
- Cada participante diagnostica e reescreve.
- Bônus: calcular tokens e comparar custo.
- Discussão em grupo: 5 min finais.

---

## Módulo 2 — Ecossistema Open-Source (1h30 total)
**Teoria: 1h | Lab: 30min | Slides: 4**

---

### Slide 2.1 — Open-Source vs Proprietários (20 min)
**🎯 Objetivo**: Entender o trade-off soberania vs conveniência.

(Ollama local desktop vs vLLM (orquestrador)

**Gatilho**: "Quem aqui gosta de cozinhar em casa? Quem prefere pedir delivery? É a diferença entre open-source e proprietário."

**Roteiro**:

- Apresentar os principais modelos open-source: Llama, Qwen, DeepSeek, Mistral.
- **Soberania**: "Seus dados não saem da sua máquina. Pra empresa com compliance, isso não é luxo — é requisito."
- **Proprietários**: "GPT-4o, Claude, Gemini são excelentes. Mas você não controla versão, não tem acesso à receita, e seus dados trafegam por servidores de terceiros."
- **Momento chave**: "Não é um vs o outro. É saber QUANDO usar cada um."
**Transição**: "E pra rodar modelos open-source, a ferramenta mágica é o Ollama."

---

### Slide 2.2 — Ollama e Hugging Face (25 min)
**🎯 Objetivo**: Demonstrar instalação e uso prático.

**Gatilho**: "Ollama está pra LLM assim como Docker está pra aplicação."

**Roteiro**:

- **DEMO AO VIVO (15 min)**: Instalar Ollama (se já não estiver), rodar `ollama run llama3.2`, fazer um prompt simples. Mostrar que funciona offline.
- "Em 5 minutos você roda um modelo localmente, sem API key, sem internet."
- Hugging Face: "Antes de pensar em treinar qualquer coisa, procure aqui. Alguém já fez."DEMO HUGGING FACE - Identificar raça de pets
- Abrir huggingface.co e navegar pelos modelos mais populares.
**🎤 Engajar**: "Alguém aqui já usou Ollama ou Hugging Face? Que modelo?"

**Transição**: "E quando falamos de modelos, o tamanho importa — mas não do jeito que você pensa."

---

### Slide 2.3 — Parâmetros: Mais ≠ Melhor (20 min)
**🎯 Objetivo**: Entender que SLMs resolvem 80% dos casos.

**Gatilho**: "Você precisa de um caminhão pra ir na padaria? Não. Precisa de GPT-4o pra classificar um e-mail? Também não."

**Roteiro**:

- Parâmetros: Arquivo de números▎ O arquivo do Llama 8B tem 4.7 GB. Esses 4.7 GB são só números — nada de código, nada de regras. Cada número é um parâmetro. Durante o treinamento, o modelo leu a internet inteira e foi ajustando esses números para refletir padrões da língua. Seu nome, verbos, código Python — tudo virou número.
Corpo do arquivo — só números:

[Camada 1 - Atenção]

-0.00342 0.01561 -0.00893 0.02147 -0.00112 0.00985 -0.00456 ...

0.01823 -0.00671 0.01134 -0.01988 0.00291 -0.01453 0.00762 ...

0.00559 -0.01245 -0.00178 0.01604 -0.00924 0.01337 -0.00618 ...

... (4096 × 4096 = 16 milhões de números só nesta camada)

[Camada 2 - Atenção]

... (mais 16 milhões de números)

... (32 camadas × milhões de números cada = 8 bilhões de parâmetros)

[Camada 32 - Saída]

-0.00192 0.00814 -0.00366 0.01123 -0.00687 0.00241 -0.00509 ...

Não tem if, for, regra gramatical, nada. É só isso: um dump binário de 8 bilhões de floats comprimidos. Quando você faz uma pergunta, o llama.cpp percorre esses números fazendo multiplicações de matriz — como o NumPy faria.

A "mágica" é que esses números não foram escritos por um humano. Foram descobertos automaticamente pelo treinamento, que leu a internet inteira e ajustou cada número para minimizar o erro de previsão da próxima palavra.

- Comparar LLMs grandes (GPT-4o, Claude Opus) com SLM = Small Language Model.Ex: Phi-3 (Microsoft), Llama 8B (Meta). '8B' = 8 bilhões de parâmetros. O GPT-4o tem centenas de bilhões.
- "SLMs entregam 80% da qualidade por 10% do custo."
- **Fato surpreendente**: Remover parâmetros pode melhorar o modelo - Técnica de compressão: pegar um modelo treinado e cortar pesos "inúteis"- É um campo de pesquisa (pruning estruturado, distillation, quantização)- Lottery Ticket Hypothesis (Frankle & Carbin, 2019): sub-redes com 10-20% dos pesos originais igualam a precisão da rede completa. [https://arxiv.org/abs/1803.03635](https://arxiv.org/abs/1803.03635)- SparseGPT (Frantar & Alistarh, 2023): removeu 50-60% dos pesos do OPT-175B e LLaMA em um único passo, sem re-treino. [https://arxiv.org/abs/2301.00774](https://arxiv.org/abs/2301.00774)- Wanda (Sun et al., 2024): poda simples por magnitude × ativação no LLaMA e LLaMA-2, mesma eficácia do SparseGPT. [https://arxiv.org/abs/2306.11695](https://arxiv.org/abs/2306.11695)
**Transição**: "Então como decidir entre nuvem e local? Vamos à matriz de decisão."

---

### Slide 2.4 — Critérios de Escolha (15 min)
**🎯 Objetivo**: Fixar os 4 critérios: custo, latência, privacidade, capacidade.

**Roteiro**:

- Percorrer os 4 critérios rapidamente — o slide fala por si.
- **Arquitetura híbrida**: "SLM local pra alto volume/baixo risco. API cloud pra tarefas complexas/pontuais."
- "Times maduros não escolhem um OU outro. Usam AMBOS."
**Transição**: "Vamos para o laboratório — vocês vão instalar o Ollama e rodar um modelo local AGORA."

---

### Laboratório Módulo 2 (30 min)
- Instalar Ollama, baixar Llama 3.2 3B.
- Rodar 3 prompts idênticos no modelo local e em API cloud.
- Comparar qualidade, latência, custo. Preencher matriz.

---

## Módulo 3 — Prompt Engineering (2h30 total)
**Teoria: 1h45 | Lab: 45min | Slides: 5**

---

### Slide 3.1 — Os 5 Elementos (25 min)
**🎯 Objetivo**: Ensinar a estrutura completa de um prompt.

**Gatilho**: "Um prompt bem construído é a diferença entre receber código que você commita e código que você reescreve do zero."

**Roteiro**:

- Percorrer os 5 elementos de cima pra baixo.
- **DEMO AO VIVO**: Mostrar um prompt sem estrutura (ruim) e o resultado. Depois mostrar o MESMO prompt com os 5 elementos. Comparar.
- **Role**: Explicar como afeta tom e nível técnico.
- **Contexto**: "É aqui que 90% dos prompts falham. A IA não tem contexto do seu projeto."
- **Restrições**: "Tão importante quanto dizer o que fazer é dizer o que NÃO fazer."
- **Formato**: "Se você não especificar o formato, a IA decide por você — e geralmente erra."
**🎤 Engajar**: "Alguém tem um prompt que funcionou muito bem ou muito mal pra compartilhar?"

**Transição**: "Mas nem todo prompt precisa dos 5 elementos. Temos frameworks mais enxutos."

---

### Slide 3.2 — Frameworks RTF, CARE, RISE (25 min)
**🎯 Objetivo**: Escolher o framework certo por tarefa.

**Roteiro**:

- **RTF**: "Pedir pizza. Três frases, direto ao ponto. Pra tarefas simples: gera endpoint, cria classe Java."Role, Task, Format
- **CARE**: "Pedir pizza com visita em casa. Precisa de contexto: quantos? restrições? orçamento? Pra tarefas com objetivo de negócio: runbook, plano de migração."Context, Action, Result, Example
- **RISE**: "Ensinar o pizzaiolo. Passo a passo com resultado esperado. Pra tarefas complexas: diagnóstico de bug, troubleshooting."Role, Input, Steps, Examples
- **Regra**: "Comece com RTF. Se a resposta não for boa, suba pra CARE. Se ainda não for, vá de RISE."
**🎤 Engajar**: "Que tipo de tarefa você mais faz? Qual estão usando no dia a dia com a IA?"

**Transição**: "Frameworks estruturam o prompt. Agora, como o modelo raciocina?"

---

### Slide 3.3 — Técnicas de Raciocínio (25 min)
**🎯 Objetivo**: Dominar Zero-shot, Few-shot e Chain of Thought.

**Roteiro**:

- **Zero-shot**: "Instrução direta. Funciona pra 70% dos casos."
- **Few-shot (ênfase)**: "A técnica MAIS subestimada. Dois exemplos bem escolhidos entregam mais qualidade que 2 horas refinando prompt. Mostre o que você quer."
- **Chain of Thought**: "A que MAIS reduz alucinação. Force o modelo a mostrar o raciocínio." **DEMO**: Fazer um problema de lógica com e sem CoT. Mostrar a diferença.
**🎤 Engajar**: "Alguém já usou Few-shot sem saber que tinha nome?"

**Transição**: "Agora, o que NÃO fazer — os antipadrões."

---

### Slide 3.4 — Antipadrões (15 min)
**🎯 Objetivo**: Reconhecer e corrigir erros comuns.

**Roteiro**:

- Rápido — cada antipadrão é autoexplicativo. 3 min cada.
- **Sobrecarga**: "10 comandos → prioriza primeiros, ignora últimos."
- **Vagueza**: "'Melhore' não significa nada. Melhore o QUÊ?"
- **Contradição**: "Seja conciso + explique em detalhes = a IA trava."
- **Confiança cega**: "Sempre valide. Sempre rode testes."
**Transição**: "Vamos para o resumo e o cheat sheet."

---

### Slide 3.5 — Cheat Sheet + Resumo (15 min)
**🎯 Objetivo**: Deixar um guia rápido de consulta.

**Roteiro**:

- "Este é o slide pra vocês tirarem print."
- Árvore de decisão: "Tarefa simples? → RTF. Negócio? → CARE. Múltiplos passos? → RISE."
- **Dica de ouro**: "Comece simples. Só adicione complexidade se a resposta não for boa."
**Transição**: "Agora o laboratório — vocês vão aplicar os 3 frameworks."

---

### Laboratório Módulo 3 (45 min)
- 3 cenários: SQL com RTF, migração com CARE, bug com RISE+CoT.
- Cada um mostra seu melhor prompt. Grupo discute.
- 10 min finais: compartilhar aprendizados.

---

## Módulo 4 — RAG, Embeddings e Engenharia de Contexto (2h total)
**Teoria: 1h30 | Lab: 30min | Slides: 5**

---

### Slide 4.1 — RAG: O Conceito (20 min)
**🎯 Objetivo**: Entender o valor do RAG.

**Gatilho**: "Agora vamos ver COMO o RAG funciona."

**Roteiro**:

- Comparar "Sem RAG" (confia na memória, alucina) com "Com RAG" (busca fontes, responde baseado em dados reais).
- **Analogia**: "Aluno fazendo prova sem consulta vs aluno com livro aberto na página certa."
- Enfatizar: "RAG não é só mais barato que fine-tuning. É mais RÁPIDO de implementar e mais FÁCIL de atualizar."
**Transição**: "RAG parece simples — mas tem um pipeline de 5 etapas."

---

### Slide 4.2 — Pipeline RAG em 5 Etapas (25 min)
**🎯 Objetivo**: Entender cada etapa e saber debugar.

**Gatilho**: "O pipeline RAG é como uma linha de montagem. Se uma etapa falha, o produto final sai errado."

**Roteiro**:

- Percorrer as 5 etapas. 4 min cada.
- **Chunks**: "Se muito grande → perde precisão. Se muito pequeno → perde contexto."**Chunking por tamanho (jeito burro):**"Capítulo 1. Introdução à física quântica. Segundo oprincípio da incerteza de Heisenberg, não é possível..." [CORTE em 500 tokens]Corta no meio do raciocínio. Perde o sentido.**Chunking semântico (jeito inteligente):**[CORTE] "Capítulo 1. Introdução à física quântica."[CORTE] "Segundo o princípio da incerteza de Heisenberg, não é possíveldeterminar simultaneamente posição e momento de uma partícula."Corta nos pontos naturais: parágrafos, seções, mudanças de assunto. Preserva o sentido.
- **Embeddings**: "A 'mágica' que transforma texto em números. Próximo slide aprofunda."
- **Vector DB**: "Chroma, Pinecone, pgvector — bancos otimizados pra busca por similaridade."
- **Similaridade**: "Cosseno. Quanto mais próximo no espaço, mais relacionado."Cada embedding é uma seta saindo da origem. Se duas setas apontam na mesma direção (ângulo pequeno), os textos são similares. Cosseno do ângulo mede isso: cos(0°)=1 (idêntico), cos(90°)=0 (não relacionado)Tipos de busca por similaridade (pode ser hybrida):Pessoa 1 — BM25 (Ctrl+F turbinado)Você: "Ache o documento que fala sobre cachorro"Ela vasculha e acha tudo que tem a palavra exata "cachorro":✅ "O cachorro latiu."✅ "Comprei ração para cachorro."❌ "O golden retriever é dócil." ← não achou, não tem a palavra "cachorro"---Pessoa 2 — Embeddings (entende o significado)Você: "Ache o documento que fala sobre cachorro"Ela entende o conceito e acha:✅ "O golden retriever é dócil." ← entendeu que golden = cachorro✅ "Meu animal de estimação toma banho toda semana." ← entendeu o contexto❌ "Cachorro-quente é minha comida favorita." ← confundiu, é comida, não animal
- **Injeção**: "Os 3-5 chunks viram contexto no prompt. O modelo NÃO usa a memória — usa o contexto."
- Seção de debugging: "Resposta ruim? Confira os 4 pontos."
**Transição**: "Embeddings merecem um slide próprio. É o conceito mais abstrato e mais importante."

---

### Slide 4.3 — Embeddings (25 min)
**🎯 Objetivo**: Tornar embeddings intuitivos.

**Gatilho**: "Embeddings são coordenadas GPS no espaço do significado."

**Roteiro**:

- Explicar que cada palavra/texto vira uma lista de números.
- **Visualização**: CEP e Busca dentro de documentos.
- **Aplicações**: Busca semântica, recomendação.
**Transição**: "RAG tradicional funciona bem pra buscas simples. Mas e quando a pergunta exige conexões?"

---

### Slide 4.4 — Graph RAG vs RAG Tradicional (10 min)
**🎯 Objetivo**: Saber quando Graph RAG(ferramentas rag avançado) é necessário.

**Roteiro**:

- Rápido — é um tópico avançado.
- "RAG tradicional: 'Quanto custa o plano X?' Graph RAG: 'Quantos clientes do plano X também usam o produto Y?'"
- "Graph RAG monta um grafo. Entidades = nós. Relacionamentos = arestas. Navega com Cypher."
- "Só use se seu domínio tem MUITAS conexões. Senão, RAG tradicional resolve."
**Transição**: "Agora, a cereja do bolo: engenharia de contexto."

---

### Slide 4.5 — Engenharia de Contexto + Regra dos 50-70% (10 min)
**🎯 Objetivo**: Fixar o princípio mais importante de RAG.

**Roteiro**:

- "Contexto é o MAIOR diferencial no uso de IA. Mais que o modelo. Mais que o prompt."
- **Regra dos 50-70%**: "Use no máximo 50-70% da janela. 200K tokens? Fique abaixo de 130K."
- **Progressive Disclosure**: "Carregue só o necessário, só quando necessário."**Laboratório (30 min):**
  1. Visualizar embeddings: identificar proximidade e estado pelo CEP.
  2. Explicar pipeline RAG simplificado: quebrar documento, gerar embeddings, buscar trecho similar a uma pergunta, injetar no prompt e comparar resposta com vs sem RAG.
**Transição**: "Agora vamos começar a falar de ferramentas para dar contexto."

---

## Módulo 5 — MCP e Agentes de IA (2h total)
**Teoria: 1h30 | Lab: 30min | Slides: 5**

---

### Slide 5.1 — MCP: A Tomada Universal (20 min)
**🎯 Objetivo**: Entender o problema que MCP resolve.

**Gatilho**: "Antes do MCP, conectar IA no banco, Jira e GitHub era igual ter um eletrodoméstico com tomada diferente pra cada país."

**Roteiro**:

- Explicar o problema M×N de integrações.
- MCP resolve: "Qualquer ferramenta que segue o padrão conecta em qualquer IA."
- "Hoje é padrão da indústria. Cursor, Claude Code, Copilot, Cline — todos usam MCP."
- "Configura 1x, toda IA descobre e usa."
**Transição**: "Como funciona a arquitetura por trás?"

---

### Slide 5.2 — Arquitetura Server/Client (20 min)
**🎯 Objetivo**: Visualizar o fluxo de comunicação.

**Roteiro**:

- Explicar os 3 componentes: IA, MCP Client, MCP Server.
- "A IA decide 'preciso buscar a task CAN-123'. O Client vê que o Server do Jira expõe `getTask`. O Server traduz pra API do Jira."
- Analogia do restaurante: "Server = garçom. Client = maître. IA = cliente."
- Mencionar que o protocolo gerencia autenticação.
**🎤 Engajar**: "Quem aqui já configurou um MCP Server? Como foi a experiência?"

**Transição**: "Agora vamos além do chat — os agentes."

---

### Slide 5.3 — Agentes: Os 4 Componentes (20 min)
**🎯 Objetivo**: Entender a anatomia de um agente.

**Roteiro**:

- Diferença crucial: "Chat responde. Agente executa."
- Exemplo concreto: "Chat: 'Qual a previsão do tempo?' Agente: 'Me avisa se chover amanhã e remarca minhas reuniões externas.'"
- Os 4 componentes: cérebro (LLM), mãos (ferramentas), memória (contexto + DB), guardrails (regras).
- "Em IDEs modernas, o modo agente significa: lê código → planeja mudanças → edita arquivos → roda testes → itera."
**Transição**: "Como o agente decide o que fazer? Com um loop."

---

### Slide 5.4 — O Loop do Agente (15 min)
**🎯 Objetivo**: Entender o ciclo Planejar-Executar-Observar-Replanejar.

**Roteiro**:

- "É o PDCA da qualidade, executado por IA em segundos."
- Percorrer as 4 fases.
- "O loop roda até o objetivo ser atingido OU um guardrail interromper."
- "Entender esse ciclo permite antecipar onde o agente pode travar e adicionar fallbacks."
**Transição**: "E qual a diferença entre MCP, Skill e API direta?"

---

### Slide 5.5 — MCP vs Skill vs API + Resumo (15 min)
**🎯 Objetivo**: Não confundir os conceitos.

**Roteiro**:

- "Dado que MUDA → MCP. Conhecimento ESTÁVEL → Skill. Integração PONTUAL → API."
- **Erro comum**: "Times misturam e acabam com MCPs pesados ou skills que deveriam ser MCPs."
- Resumo do módulo em 2 minutos.
**Transição**: "Laboratório — configurar um MCP Server real."

---

### Laboratório Módulo 5 (30 min)
- Configurar MCP Server (filesystem ou GitHub) no Claude Code.
- Observar agente descobrindo ferramentas.
- Discutir: "O que aconteceu que você não fez manualmente?"

---

## Módulo 6 — Arquitetura de Contexto (2h total)
**Teoria: 1h25 | Lab: 35min | Slides: 6**

---

### Slide 6.1 — Evolução 2023-2026 (15 min)
**🎯 Objetivo**: Contextualizar a jornada da indústria.

**Roteiro**:

- "Essa é a história de como a indústria aprendeu a usar IA de forma eficiente."
- **Fase 1 (2023-2024)**: "Tudo no prompt. Resultado: contexto gigante, caro, alucinações."
- **Fase 2 (início 2025)**: "Super-agentes de 3000 linhas. Plano básico do Claude dizia 'oi' e já gastava o limite."
- **Fase 3 (meados 2025+)**: "Skills modulares. Contexto limpo. Custo baixo. O ponto ideal."
- **Mensagem**: "Vocês podem pular direto pra Fase 3. Não repitam nossos erros."
**Transição**: "A Fase 3 se organiza em 4 pilares."

---

### Slide 6.2 — Os 4 Pilares (20 min)
**🎯 Objetivo**: Fixar o modelo mental da casa.

**Roteiro**:

- "Pensa na arquitetura de uma casa. Cada pilar tem seu papel."
- **Rules/Agents.md = Planta baixa**: "O QUE é o projeto."
- **Skills = Ferramentas**: "COMO fazer X."
- **MCPs = Portas**: "ONDE buscar/alterar dados."
- **Sub-agents = Pedreiros**: "FAÇA em paralelo."
- "Essa divisão resolve a confusão mais comum: 'Isso vai como rule, skill ou MCP?'"
**Transição**: "Vamos aprofundar cada pilar, começando pelo Agents.md."

---

### Slide 6.3 — Rules e Agents.md (15 min)
**🎯 Objetivo**: Saber criar um Agents.md eficaz.

**Roteiro**:

- "Agents.md é o que MAIS multiplica a qualidade da IA no seu projeto."
- Mostrar a estrutura: "200 linhas máximo. Alto nível + ponteiros."
- **Dica de ouro**: "Pra projetos legados, peça pra IA gerar: `claude onboard`."
- **Always-apply vs on-demand**: "Regras críticas sempre. Docs detalhadas sob demanda."
**🎤 Engajar**: "Alguém aqui já tem um CLAUDE.md ou Agents.md no projeto? O que tem nele?"

**Transição**: "O segundo pilar: skills."

---

### Slide 6.4 — Skills: Capacidades Portáteis (15 min)
**🎯 Objetivo**: Entender o valor de encapsular conhecimento.

**Roteiro**:

- Mostrar o antes/depois com o exemplo do Jira.
- "Sem skill: 'Corrige o bug CAN-123 na URL techleads.atlassian.net, cloud digital, board CAN...'."
- "Com skill: 'Corrige a CAN-123.' Pronto."
- "Skills transformam conhecimento tribal em ativos reutilizáveis. Marketplaces internos."
**Transição**: "O terceiro pilar: sub-agents — e a diferença crucial entre skill e sub-agent."

---

### Slide 6.5 — Sub-agents: Revolução Silenciosa (10 min)
**🎯 Objetivo**: Não confundir skill com sub-agent.

**Roteiro**:

- "Skill: NÃO reduz contexto — roda no mesmo processo."
- "Sub-agent: SIM reduz contexto — processo separado, devolve só o output."
- "Você foca em criar skills. A ferramenta gerencia sub-agents."
- "Antes eram confundidos. Agora cada um tem seu lugar."
**Transição**: "Checklist final dos 4 pilares."

---

### Slide 6.6 — Checklist + Resumo (10 min)
**🎯 Objetivo**: Dar a matriz de referência rápida.

**Roteiro**:

- "Tirem print. Este slide é sua cola."
- Percorrer a tabela rapidamente.
- **Antipadrão**: "1 agente de 3000 linhas → 5 skills de 200 linhas."
- Resumo do módulo em 2 minutos.
**Transição**: "Laboratório prático de arquitetura de contexto."

---

### Laboratório Módulo 6 (35 min)
- Analisar "super-agente" hipotético de 3000 linhas → identificar skills.
- Escrever Agents.md para projeto real.
- Esboçar uma skill com front matter e trigger.

---

## Módulo 7 — SDD e Ferramentas (2h30 total)
**Teoria: 1h40 | Lab: 50min | Slides: 6**

---

### Slide 7.1 — Por que Prompt Direto Falha (15 min)
**🎯 Objetivo**: Justificar a necessidade de método.

**Gatilho**: "Quem aqui já jogou um PRD gigante no ChatGPT e recebeu um plano raso?"

**Roteiro**:

- "Não é culpa da IA. É física da janela de contexto."
- "50 requisitos → prioriza início, ignora meio, alucina final."
- "SDD não é burocracia — é estratégia pra contornar limitações das LLMs."
**Transição**: "O SDD tem 4 fases. Vamos ver cada uma."

---

### Slide 7.2 — SDD: As 4 Fases (20 min)
**🎯 Objetivo**: Ensinar o ciclo completo.

**Roteiro**:

- "Construção civil: Specify = 'quero 3 quartos'. Design = planta. Tasks = cronograma. Execute = pedreiros."
- Percorrer as 4 fases.
- "Cada fase tem contexto controlado. A IA nunca fica sobrecarregada."
- "Fases sem dependência podem rodar em paralelo com sub-agents."
**Transição**: "Duas práticas que sustentam o SDD: STATE.md e documentação."

---

### Slide 7.3 — STATE.md e Documentação (15 min)
**🎯 Objetivo**: Internalizar as práticas de sustentação.

**Roteiro**:

- **STATE.md**: "Diário de obra. O MAIOR problema de desenvolver com IA é perder contexto entre sessões. STATE.md resolve."
- **Documentação**: "Deixou de ser burocracia. Virou COMBUSTÍVEL. Quanto melhor documentado, mais rápido e preciso o agente."
- **Inversão de incentivo**: "Documentar não é pro próximo dev. É pra IA gerar código melhor pra VOCÊ, AGORA."
**🎤 Engajar**: "Quem aqui documenta o projeto? E se documentar significasse código melhor GERADO PRA VOCÊ?"

**Transição**: "O micro-ciclo dentro de cada fase: RPI."

---

### Slide 7.4 — RPI: Research-Plan-Implement (10 min)
**🎯 Objetivo**: Fixar o hábito de pesquisar antes de codar.

**Roteiro**:

- "RPI evita 'vibe coding' — codar no feeling sem planejar."
- "Research: abrir o leque. Plan: documentar decisão. Implement: executar."
- "RPI é o micro-ciclo. SDD é o macro-ciclo. Juntos = disciplina."
**Transição**: "E quais ferramentas usar nesse ciclo?"

---

### Slide 7.5 — Ferramentas: O Que Usar Quando (20 min)
**🎯 Objetivo**: Dar o panorama de ferramentas.

**Roteiro**:

- "Não existe ferramenta universal melhor. Existe a certa pro seu contexto."
- Percorrer as 6 ferramentas. 2 min cada.
- **Analogia dos carros**: "Cursor = SUV completo. Copilot = integrado. Claude Code = moto esportiva. Windsurf = conversível."
- Critérios: ecossistema, autonomia, custo, stack.
**🎤 Engajar**: "Qual ferramenta vocês usam? Por que escolheram ela?"

**Transição**: "Agora, o workshop prático — vocês vão executar o ciclo SDD completo."

---

### Slide 7.6 — Workshop Prático + Resumo Final (20 min)
**🎯 Objetivo**: Lançar o laboratório e fechar o workshop.

**Roteiro**:

- Explicar a dinâmica: 50 minutos, 4 fases + apresentação.
- "Cada dupla recebe um requisito real. Vocês vão fazer Specify → Design → Tasks → Execute."
- Resumo final do workshop: "7 módulos. 16 horas. 3 ideias centrais:"
  1. "LLMs são completadores de padrões — contexto de qualidade > modelo caro."
  2. "SDD + RPI + STATE.md = método pra desenvolver com IA sem perder coerência."
  3. "Skills modulares > agentes gigantes. Arquitetura de contexto é o diferencial."
- **Encerramento**: "Especificar antes de codar. Planejar antes de executar. Documentar enquanto faz."

---

### Laboratório Módulo 7 (50 min)
- 10 min: Specify (spec com user stories, metas, fora de escopo)
- 10 min: Design (arquitetura e decisões técnicas)
- 10 min: Tasks (3-5 tasks com definition of done)
- 15 min: Execute (simular com sub-agents)
- 5 min: Apresentação do STATE.md final