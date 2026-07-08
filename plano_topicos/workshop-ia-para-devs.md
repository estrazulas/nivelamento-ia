# Workshop: IA pra Desenvolvimento de Software

## Da base à prática com agentes

**Carga horária:** ~16 horas (2 dias)
**Pra quem:** Desenvolvedores com experiência profissional
**Pra começar:** Assistir os 3 vídeos do [Plano de Nivelamento](plano-nivelamento-ia-dev.md) (Fundamentos de LLMs, Prompt Engineering, SDD)
**Formato:** Teoria + laboratórios práticos (30-45 min por módulo)

### Pré-requisitos

**Ferramenta obrigatória:**
- **[OpenCode](https://opencode.ai)** instalado — use a assinatura **FREE** (gratuita) ou o **Plano Básico de US$ 5 no primeiro mês** para ter acesso a mais recursos. O OpenCode será usado como ferramenta principal durante todos os laboratórios do workshop.

**Ferramentas recomendadas (instalamos juntos durante o workshop):**
- **Ollama** — para execução local de modelos open-source (Módulo 2)
- **Git e Docker** — para laboratórios de MCP e SDD
- **Conta no GitHub** — para laboratórios de integração com MCP
- **Uma IDE com suporte a IA** — Cursor, VS Code + GitHub Copilot, ou Claude Code

**Nivelamento recomendado (não obrigatório):**
- Assistir os 3 vídeos do [Plano de Nivelamento](plano-nivelamento-ia-dev.md) (~1h30 total):
  1. Roadmap de IA para DevOps (20 min)
  2. Prompt Engineering — Guia Prático (1h10)
  3. SDD: Habilidade #1 para Devs (12 min)

### O objetivo

Dar a devs o que precisam pra usar IA generativa com segurança e produtividade no ciclo completo de desenvolvimento — entendendo os fundamentos técnicos, dominando as técnicas de interação e orquestrando agentes em projetos reais.

---

## Dia 1 — Fundamentos e Técnicas (~8h)

---

### Módulo 1 — Como LLMs Funcionam de Verdade (2h)

**O que você vai aprender:**
- Explicar LLMs usando o modelo mental do autocomplete
- Calcular tokens em cenários reais
- Identificar e mitigar os 4 tipos de limitação
- Decidir entre modelo pronto, fine-tuning ou RAG
- Saber quando uma LLM é a ferramenta certa — e quando não é

**Tópicos:**

#### 1.1 O Grande Autocomplete
**A ideia:** Uma LLM não "pensa" — ela completa padrões. Pensa no autocomplete do celular: você digita "bom..." e ele sugere "dia", "tarde", "noite" baseado no que já escreveu. A LLM faz a mesma coisa, mas em vez de 3 opções, escolhe entre milhões, calculando o token mais provável dado o que veio antes. Não tem intenção, opinião, nem "saber" coisas — é uma máquina de previsão estatística de tokens.
**Por que isso importa:** Muda como você escreve prompts e interpreta respostas. Você para de tratar a IA como oráculo e passa a tratar como um completador de padrões que precisa de contexto de qualidade.
**Pra visualizar:** Autocomplete turbinado — milhões de opções em vez de 3, e ele lembra de tudo na conversa.
**Fonte:** [Mini Curso IA para Devs — 08:00](https://youtu.be/90lGnXnMqgo?t=480)

#### 1.2 Modelos Multimodais
**A ideia:** Modelos multimodais entendem texto, imagem, áudio e vídeo. Dá pra enviar um print de bug, um diagrama rabiscado ou um áudio com sua dúvida, e o modelo processa tudo junto. GPT-4o, Gemini e Claude fazem isso.
**Por que isso importa:** Expande o que você pode delegar — explicar um erro a partir de um screenshot, gerar código de um wireframe, transcrever e analisar uma reunião.
**Pra visualizar:** Um dev que recebia specs só por texto agora recebe fotos do problema, áudios do cliente e vídeos do comportamento.
**Fonte:** [Mini Curso IA para Devs — 08:00](https://youtu.be/90lGnXnMqgo?t=480)

#### 1.3 Tokens: A Moeda da IA
**A ideia:** Token é a unidade de processamento — cada palavra ou fragmento que o modelo lê ou gera. "Inteligência artificial" pode ser 2 tokens. Toda API cobra por token (input + output). Uma conversa típica de desenvolvimento consome entre 2 mil e 20 mil tokens. Modelos maiores têm janelas maiores (Gemini 1.5 Pro: 2M tokens ≈ 3 livros). Mas tem uma pegadinha: se você lotar a janela, o modelo começa a "esquecer" coisas no meio.
**Por que isso importa:** Token = custo. Quem entende tokenização consegue estimar gastos, otimizar prompts e evitar desperdício com contexto redundante. Também ajuda a não estourar a janela e degradar a qualidade.
**Pra visualizar:** Token é que nem kilowatt — a moeda de consumo. A janela de contexto é a RAM: você pode encher, mas o desempenho piora antes do limite.
**Fonte:** [Mini Curso IA para Devs — 10:00](https://youtu.be/90lGnXnMqgo?t=600)

#### 1.4 As 4 Grandes Limitações
**A ideia:**
1. **Alucinações:** a IA inventa resposta com toda confiança, mas ela é falsa. Tipo pedir artigos de um autor e ela criar títulos que não existem.
2. **Data de corte:** a IA é uma enciclopédia impressa em 2023 — não sabe nada depois, a menos que você dê acesso à internet ou alimente com documentos recentes.
3. **Sensibilidade ao prompt:** mudar uma palavra na pergunta pode gerar resposta completamente diferente. "Explique RAG" vs "Explique RAG pra uma criança de 10 anos" — resultados totalmente diferentes.
4. **Degradação com contexto cheio:** quanto mais informação você joga de uma vez, mais a IA se perde no meio.

**Por que isso importa:** Conhecer essas limitações separa quem culpa a IA ("não presta") de quem contorna com estratégia ("vou quebrar em partes", "vou validar", "vou usar RAG").
**Pra visualizar:** A IA é tipo um estagiário brilhante mas com amnésia seletiva. Inventa coisas com convicção (alucina), não sabe o que aconteceu depois que foi contratado (corte), responde diferente dependendo de como você pergunta (sensibilidade) e se perde com instruções demais (sobrecarga).
**Fonte:** [Mini Curso IA para Devs — 12:00](https://youtu.be/90lGnXnMqgo?t=720)

#### 1.5 Pré-Treinamento, Fine-Tuning e a Regra dos 95%
**A ideia:** GPT, Claude e Gemini são chefs que já fizeram curso de culinária completo. Fine-tuning é mandar esse chef fazer um curso específico de sushi — caro, trabalhoso e, pra 95% dos casos, desnecessário. RAG resolve: em vez de retreinar o modelo, você entrega uma "cola" com os ingredientes do seu restaurante.
**Por que isso importa:** Fine-tuning é o primeiro impulso de todo dev quando a IA erra no domínio específico — mas quase sempre é a solução errada (cara e lenta). RAG é mais barato, mais rápido e mais fácil de atualizar.
**Pra visualizar:** Pré-treinamento = chef formado. Fine-tuning = especialização cara em sushi. RAG = entregar a receita pro chef na hora.
**Fonte:** [Mini Curso IA para Devs — 15:00](https://youtu.be/90lGnXnMqgo?t=900)

#### 1.6 Quando NÃO Usar uma LLM
**A ideia:** Nem tudo precisa de IA. Um algoritmo determinístico resolve melhor e mais barato em muitos cenários: validação de formato, parsing, cálculos, ordenação, filtros simples. Saber quando NÃO usar LLM é tão importante quanto saber usar.
**Por que isso importa:** Evita o viés do martelo dourado — usar LLM pra tudo é caro, lento e introduz não-determinismo onde você não precisa.
**Pra visualizar:** Você não chama um arquiteto pra pendurar um quadro. Às vezes um prego e um martelo resolvem.
**Fonte:** [Mini Curso IA para Devs — 00:00](https://youtu.be/90lGnXnMqgo?t=0)

**Laboratório (30 min):** Cada participante recebe 3 prompts com problemas diferentes — alucinação, data de corte, sobrecarga de contexto. A tarefa: diagnosticar qual limitação está rolando em cada caso e reescrever o prompt pra mitigar. Bônus: calcular os tokens de cada versão e comparar o custo.

---

### Módulo 2 — Ecossistema Open-Source e Execução Local (1h30)

**O que você vai aprender:**
- Instalar e rodar um modelo open-source localmente via Ollama
- Navegar no Hugging Face pra encontrar modelos adequados
- Comparar modelos por custo, latência, privacidade e capacidade
- Decidir entre execução local vs API na nuvem

**Tópicos:**

#### 2.1 Modelos Open-Source: As Receitas Públicas
**A ideia:** Modelos open-source (Llama da Meta, Qwen da Alibaba, DeepSeek, Mistral) são receitas de bolo publicadas de graça — você pode usar, modificar e rodar na sua cozinha sem pagar royalties. Já os proprietários (GPT, Claude, Gemini) são restaurantes: a comida é ótima, mas você não tem acesso à receita nem controle sobre a cozinha.
**Por que isso importa:** Open-source é soberania — você não depende de fornecedor, seus dados não trafegam por APIs de terceiros e pode customizar o modelo. Pra empresas com restrições de compliance, é muitas vezes a única opção.
**Pra visualizar:** Proprietário = restaurante. Open-source = receita que você cozinha em casa.
**Fonte:** [Mini Curso IA para Devs — 17:00](https://youtu.be/90lGnXnMqgo?t=1020)

#### 2.2 Ollama: O Eletrodoméstico
**A ideia:** Ollama faz execução local de LLMs ser trivial — parecido com Docker pra modelos de IA. Instala, escolhe o modelo (`ollama run llama3.2`), e roda na sua máquina. Sem depender de internet, sem pagar API, sem enviar dados pra lugar nenhum.
**Por que isso importa:** Elimina a barreira de entrada pra testar modelos open-source. Em 5 minutos você roda um modelo localmente, compara com APIs e decide com dados reais.
**Pra visualizar:** Ollama tá pra LLM assim como Docker tá pra aplicação — baixa e roda com um comando.
**Fonte:** [Mini Curso IA para Devs — 17:00](https://youtu.be/90lGnXnMqgo?t=1020)

#### 2.3 Hugging Face: O GitHub dos Modelos
**A ideia:** Hugging Face é o maior repositório de modelos de IA — milhares de modelos pré-treinados, datasets e versões modificadas pela comunidade. É onde você encontra modelos especializados (um treinado pra SQL, outro pra revisão de contratos) e benchmarks.
**Por que isso importa:** Antes de pensar em treinar qualquer coisa, procure no Hugging Face. Provavelmente alguém já fez algo similar. Economiza semanas.
**Pra visualizar:** Hugging Face tá pra modelo de IA assim como GitHub tá pra código — repositório público, comunidade ativa, versões, forks.
**Fonte:** [Mini Curso IA para Devs — 17:00](https://youtu.be/90lGnXnMqgo?t=1020)

#### 2.4 Parâmetros: Mais Nem Sempre é Melhor
**A ideia:** Parâmetros são tipo os "neurônios" da rede — quanto mais, maior a capacidade teórica. Mas a correlação não é linear. Pesquisas recentes mostram que remover parâmetros às vezes melhora o modelo (tipo tirar "sujeira" do cérebro). Modelos menores e especializados (Phi-3, Llama 8B) entregam 80% da qualidade de um modelo grande por 10% do custo.
**Por que isso importa:** Nem toda tarefa precisa de GPT-4o. Pra sumarização, classificação, parsing e código simples, um SLM local resolve — com latência menor e custo zero de API.
**Pra visualizar:** Você não precisa de um caminhão pra ir na padaria. SLM = moto. LLM gigante = caminhão.
**Fonte:** [Mini Curso IA para Devs — 17:00](https://youtu.be/90lGnXnMqgo?t=1020) | [Roadmap IA para DevOps — 5:55](https://youtu.be/03-nB_KMm44?t=355)

#### 2.5 Critérios de Escolha: Nuvem vs Local
**A ideia:** A decisão entre API na nuvem e execução local depende de 4 coisas: **custo** (API cobra por token, local sai de graça depois do setup), **latência** (local é mais rápido pra tarefas simples), **privacidade** (local = dados não saem da máquina) e **capacidade** (nuvem tem modelos maiores pra raciocínio complexo).
**Por que isso importa:** Times que entendem esse trade-off montam arquiteturas híbridas — SLM local pra tarefas de alto volume e baixo risco (autocomplete, linting), API na nuvem pra tarefas complexas e pontuais (design de arquitetura, debugging multi-arquivo).
**Pra visualizar:** Processamento local = cozinha em casa. API na nuvem = pedir delivery.
**Fonte:** [Mini Curso IA para Devs — 17:00](https://youtu.be/90lGnXnMqgo?t=1020)

**Laboratório (30 min):** Instalar Ollama, baixar um modelo pequeno (Llama 3.2 3B ou Qwen 2.5 7B), executar 3 prompts idênticos no modelo local e em uma API na nuvem (Claude ou GPT). Comparar qualidade, latência e custo estimado. Preencher uma matriz de decisão.

---

### Módulo 3 — Prompt Engineering na Prática (2h30)

**O que você vai aprender:**
- Construir prompts com os 5 elementos (Role, Contexto, Instrução, Restrições, Formato)
- Escolher o framework certo (RTF, CARE, RISE) pra cada tarefa
- Aplicar Zero-shot, Few-shot e Chain of Thought no contexto certo
- Depurar e iterar prompts ineficazes

**Tópicos:**

#### 3.1 Os 5 Elementos de um Prompt Eficiente
**A ideia:** Um prompt bem construído tem 5 camadas:
1. **Role:** "Você é um dev sênior especialista em refatoração de código legado" — direciona tom e nível técnico.
2. **Contexto:** "Este projeto é uma API Go 1.22 com arquitetura hexagonal" — o background que a IA não tem.
3. **Instrução:** "Refatore a função extraindo a validação pra outra função" — a ação, clara e direta.
4. **Restrições:** "Mantenha os nomes de função. Não use generics." — limites e o que não fazer.
5. **Formato de saída:** "Retorne só o código em markdown com o nome do arquivo." — estrutura esperada.

**Por que isso importa:** Um prompt com os 5 elementos produz respostas melhores que um prompt na base do achismo. A diferença não é pequena — é entre receber código que você pode commitar e código que você reescreve do zero.
**Pra visualizar:** Pedir sem estrutura = "conserta minha casa". Com os 5 elementos = entregar planta baixa, materiais, normas e prazo.
**Fonte:** [Prompt Engineering — 21:28](https://www.youtube.com/live/Qf_QHxuc8J8?t=1288)

#### 3.2 Frameworks de Prompt: RTF, CARE, RISE
**A ideia:** Nem todo prompt precisa dos 5 elementos. Dá pra usar frameworks mais enxutos:
- **RTF (Role, Task, Format):** pra tarefas simples e de padrão conhecido. Gerar Dockerfile, JSON schema, script SQL.
- **CARE (Context, Action, Result, Example):** pra tarefas com objetivo de negócio. Runbook de incidente, plano de migração.
- **RISE (Role, Input, Steps, Example):** pra tarefas com múltiplos passos (Chain of Thought implícito). Análise de vulnerabilidade, troubleshooting.
**Por que isso importa:** Economiza tokens e tempo. Você não precisa dos 5 elementos pra gerar um Dockerfile — RTF resolve com 3 linhas.
**Pra visualizar:** RTF = post-it. CARE = e-mail formal. RISE = documentação técnica passo a passo.
**Fonte:** [Prompt Engineering — 47:01](https://www.youtube.com/live/Qf_QHxuc8J8?t=2821)

#### 3.3 Técnicas de Raciocínio
**A ideia:** Os frameworks estruturam o prompt; as técnicas definem como o modelo raciocina:
- **Zero-shot:** instrução direta, sem exemplo. Pra tarefas comuns que o modelo já conhece (CRUD, explicar erro, traduzir código).
- **Few-shot:** você dá 1-3 exemplos de input → output. Pra formato muito específico ou convenção interna que o modelo não conhece.
- **Chain of Thought:** força o modelo a mostrar o raciocínio passo a passo antes da resposta final. Pra análise, troubleshooting, decisões com trade-off.
**Por que isso importa:** Few-shot é a técnica mais subestimada — 2 exemplos bem escolhidos entregam mais qualidade que 2 horas refinando prompt. Chain of Thought é a que mais reduz alucinação em tarefas analíticas.
**Pra visualizar:** Zero-shot = "faz um bolo". Few-shot = "faz um bolo igual a este" (mostra foto). Chain of Thought = "me explica como você vai fazer antes de começar".
**Fonte:** [Prompt Engineering — 70:34](https://www.youtube.com/live/Qf_QHxuc8J8?t=4234)

#### 3.4 Antipadrões e Erros Comuns
**A ideia:** Os erros mais frequentes:
- **Sobrecarga de instruções:** 10 comandos num prompt só — o modelo prioriza os primeiros e ignora os últimos.
- **Prompt vago demais:** "melhore esse código" — o modelo não sabe se é performance, legibilidade ou segurança.
- **Restrições contraditórias:** "seja conciso" + "explique em detalhes" — o modelo trava.
- **Confiar cegamente:** não validar saídas, especialmente código e dados estruturados.
**Por que isso importa:** Conhecer os antipadrões reduz o tempo de iteração. A maioria dos prompts ruins sofre de um desses 4 problemas.
**Fonte:** [Mini Curso IA para Devs — 12:00](https://youtu.be/90lGnXnMqgo?t=720) | [Prompt Engineering — 19:27](https://www.youtube.com/live/Qf_QHxuc8J8?t=1167)

**Laboratório (45 min):** Oficina de prompt engineering. Cada participante recebe 3 cenários reais:
1. Gerar query SQL complexa com joins e agregações (usar RTF)
2. Criar plano de migração de biblioteca com breaking changes (usar CARE)
3. Analisar bug multi-arquivo e propor correção (usar RISE + Chain of Thought)

Comparação coletiva: cada um mostra seu melhor prompt e o grupo discute o que funcionou.

---

### Módulo 4 — RAG, Embeddings e Engenharia de Contexto (2h)

**O que você vai aprender:**
- Explicar cada etapa do pipeline RAG e seu propósito
- Entender embeddings como representação vetorial de similaridade semântica
- Diferenciar RAG tradicional de Graph RAG e escolher a abordagem certa
- Aplicar a regra dos 40% e o princípio de progressive disclosure

**Tópicos:**

#### 4.1 RAG: A Cola na Prova
**A ideia:** RAG (Retrieval-Augmented Generation) resolve 95% dos casos em que a IA precisa de conhecimento específico do seu domínio — sem retreinar nada. Em vez de confiar na memória da IA (que alucina, falha, desatualiza), você entrega os trechos relevantes do seu material junto com a pergunta. Tipo dar uma "cola" pra IA durante a prova.
**Por que isso importa:** RAG é mais barato, mais rápido e mais fácil de atualizar que fine-tuning. Mudou a documentação? Reindexa. Não precisa retreinar nada. Pra 95% dos usos corporativos (FAQ, docs internas, base de conhecimento), RAG resolve.
**Pra visualizar:** Fine-tuning = mandar o aluno estudar o livro inteiro antes da prova. RAG = deixar o livro aberto na página certa.
**Fonte:** [Mini Curso IA para Devs — 23:00](https://youtu.be/90lGnXnMqgo?t=1380)

#### 4.2 O Pipeline RAG em 5 Etapas
**A ideia:** O pipeline RAG completo:
1. **Chunks:** quebrar documentos grandes em pedaços menores e coerentes. Um manual de 500 páginas vira centenas de blocos de 500-1000 tokens.
2. **Embeddings:** transformar cada chunk num vetor numérico — uma lista de números que representa a posição daquele texto no espaço semântico.
3. **Vector Database:** armazenar esses vetores num banco otimizado pra busca por proximidade (Chroma, Pinecone, pgvector).
4. **Busca por similaridade:** quando o usuário pergunta algo, a pergunta vira embedding também. O banco encontra os 3-5 chunks mais próximos (cosseno).
5. **Injeção no prompt:** esses chunks viram contexto no prompt junto com a pergunta. O modelo responde baseado nesse contexto, não na memória.
**Por que isso importa:** Entender o pipeline permite debugar quando o RAG falha. Resposta ruim? Pode ser chunk mal dimensionado, embedding de baixa qualidade, threshold errado ou chunk irrelevante sendo injetado.
**Pra visualizar:** É uma biblioteca. Chunks = fichas. Embeddings = coordenadas da estante. Vector DB = sistema de busca. Similaridade = encontrar livros na mesma estante. Injeção = colocar os livros abertos na mesa do aluno.
**Fonte:** [Mini Curso IA para Devs — 23:00](https://youtu.be/90lGnXnMqgo?t=1380)

#### 4.3 Embeddings: Como a IA "Entende" Palavras
**A ideia:** Embeddings transformam palavras em listas de números — tipo coordenadas GPS no espaço do significado. "Cachorro" e "gato" ficam perto (são pets). "Cachorro" e "carro" ficam longe. Num mapa 2D: "rei" e "rainha" estariam próximos; "homem" e "mulher" também, mas em outra região. Sem embeddings, a IA trataria "automóvel" e "carro" como palavras diferentes.
**Por que isso importa:** Embeddings são a base invisível de quase toda aplicação prática de IA — busca semântica em código, recomendação de docs, detecção de duplicatas.
**Pra visualizar:** Coordenadas GPS do significado.
**Fonte:** [Mini Curso IA para Devs — 32:00](https://youtu.be/90lGnXnMqgo?t=1920)

#### 4.4 Graph RAG: Quando Similaridade Não Basta
**A ideia:** RAG tradicional busca por similaridade de texto — funciona pra perguntas factuais ("quanto custa o plano X?"). Mas falha em perguntas que exigem conexões entre entidades ("quantos clientes do plano X também usam o produto Y?"). Graph RAG resolve montando um grafo de conhecimento (entidades como nós, relacionamentos como arestas) e navegando por ele com consultas tipo Cypher (Neo4j).
**Por que isso importa:** Graph RAG é a abordagem certa pra domínios com muitas conexões: catálogos de produtos com dependências, APIs com compatibilidade, bases de conhecimento com cross-references.
**Pra visualizar:** RAG tradicional = buscar "restaurante italiano" no Google. Graph RAG = "restaurantes italianos a menos de 1 km, abertos agora, nota acima de 4.5" — cada condição é uma aresta no grafo.
**Fonte:** [Mini Curso IA para Devs — 23:00](https://youtu.be/90lGnXnMqgo?t=1380)

#### 4.5 Engenharia de Contexto e a Regra dos 40%
**A ideia:** Contexto é o maior diferencial no uso de IA — mais que o modelo escolhido. Mas tem um limite: a **regra dos 40%** diz pra usar no máximo 40% da janela de contexto. Se o modelo suporta 200 mil tokens, mantenha abaixo de 80 mil. Acima disso, o modelo degrada. **Progressive disclosure** resolve isso: carrega só o necessário, só quando necessário — como um garçom que traz só o prato, não o cardápio inteiro.
**Por que isso importa:** É a diferença entre uma IA que acerta e uma que alucina, com os mesmos modelo e pergunta. A qualidade do contexto impacta mais que o modelo ou o prompt.
**Pra visualizar:** Sua mesa de trabalho. 50 documentos = caos. 3 documentos = foco total.
**Fonte:** [Rules, Skills, MCPs and Subagents — 04:00](https://youtu.be/omkEi4GTCj8?t=240)

**Laboratório (30 min):**
1. Visualizar embeddings: notebook pra gerar embeddings de 20 palavras, reduzir dimensionalidade com PCA e plotar em 2D — observar os agrupamentos.
2. Simular pipeline RAG simplificado: quebrar documento, gerar embeddings (via API), buscar trecho similar a uma pergunta, injetar no prompt e comparar resposta com vs sem RAG.

---

## Dia 2 — Arquitetura e Prática (~8h)

---

### Módulo 5 — MCP e Agentes de IA (2h)

**O que você vai aprender:**
- Explicar a arquitetura MCP Server/Client e seu papel como padrão de integração
- Identificar os 4 componentes de um agente de IA
- Descrever o loop de execução de um agente e como ele difere de um chat
- Configurar um MCP Server e ver o agente descobrindo ferramentas

**Tópicos:**

#### 5.1 MCP: A Tomada Universal
**A ideia:** MCP (Model Context Protocol, da Anthropic) resolveu um problema real: antes, conectar uma IA no banco de dados, Jira e GitHub era um pesadelo — cada combinação de ferramenta + modelo exigia código customizado. MCP é tipo tomada universal: qualquer ferramenta que segue o padrão conecta em qualquer IA que também segue. Hoje é padrão da indústria — Cursor, Claude Code, Copilot.
**Por que isso importa:** Elimina o trabalho de integração. Configura um MCP Server pro Jira uma vez, e toda IA compatível descobre e usa. O protocolo gerencia autenticação e descoberta de capacidades.
**Pra visualizar:** Antes do MCP = cada eletrodoméstico com sua tomada. Depois = tomada universal de 3 pinos.
**Fonte:** [Mini Curso IA para Devs — 34:00](https://youtu.be/90lGnXnMqgo?t=2040)

#### 5.2 Arquitetura Server/Client
**A ideia:** O ecossistema MCP tem dois lados:
- **MCP Server:** expõe capacidades — "sei buscar e-mails", "sei criar tasks no Jira", "sei consultar logs". É um adaptador entre uma API externa e o protocolo.
- **MCP Client:** descobre as capacidades dos servidores e gerencia as chamadas. É o intermediário entre o modelo e os servidores. Exemplos: Claude Code, Cursor, Copilot.

O fluxo: a IA decide "preciso buscar a task CAN-123" → o Client vê que o servidor do Jira expõe `getTask` → o servidor traduz pra API do Jira → o resultado volta.
**Por que isso importa:** Entender a arquitetura permite depurar problemas de integração e decidir quando usar MCP vs API direta.
**Pra visualizar:** MCP Server = garçom. MCP Client = maître que sabe quem tá disponível. IA = cliente.
**Fonte:** [Mini Curso IA para Devs — 34:00](https://youtu.be/90lGnXnMqgo?t=2040) | [Rules, Skills, MCPs and Subagents — 24:00](https://youtu.be/omkEi4GTCj8?t=1440)

#### 5.3 Agentes de IA: Além do Chat
**A ideia:** A diferença entre chat e agente: no chat você pergunta "qual a previsão do tempo?", a IA responde. Um agente recebe "me avisa se chover amanhã e remarca minhas reuniões externas" — ele planeja, executa (consulta previsão → verifica agenda → identifica reuniões → remarca → notifica) e verifica se atingiu o resultado.

Um agente tem 4 componentes:
1. **Cérebro:** a LLM que raciocina e decide.
2. **Mãos:** ferramentas (MCPs, APIs) que executam ações.
3. **Memória:** contexto da conversa + banco externo pra persistência.
4. **Guardrails:** regras de segurança — "nunca delete sem confirmar".
**Por que isso importa:** Agentes são o próximo salto de produtividade. Um chat responde; um agente executa. Em IDEs modernas, o modo agente significa que a IA lê código, planeja mudanças, edita arquivos, roda testes e itera — tudo de uma vez.
**Pra visualizar:** Chat = perguntar as horas. Agente = assistente que olha sua agenda, calcula o trânsito, te avisa e já adianta o café.
**Fonte:** [Mini Curso IA para Devs — 36:00](https://youtu.be/90lGnXnMqgo?t=2160)

#### 5.4 O Loop do Agente
**A ideia:** O ciclo de execução de um agente:
1. **Planejar:** a LLM analisa o objetivo e define os passos.
2. **Executar:** chama as ferramentas (MCPs) pra cada passo.
3. **Observar:** coleta e analisa os resultados.
4. **Replanejar:** se algo falhou, ajusta o plano e continua.

Esse loop roda até o objetivo ser atingido ou um guardrail interromper.
**Por que isso importa:** Entender o loop permite criar agentes mais eficazes — você antecipa onde ele pode travar e adiciona fallbacks.
**Pra visualizar:** É o PDCA da qualidade, executado por IA em segundos em vez de humanos em semanas.
**Fonte:** [Mini Curso IA para Devs — 36:00](https://youtu.be/90lGnXnMqgo?t=2160)

#### 5.5 MCP vs Skill vs API Direta
**A ideia:** Qual usar pra cada tipo de integração:
- **MCP:** dados que MUDAM (status de tasks, páginas do Confluence, PRs). O protocolo gerencia autenticação. Ideal pra sistemas corporativos.
- **Skill:** conhecimento ESTÁVEL (como criar teste e2e, template de tarefa, convenção de commit). Encapsula conhecimento, não dados.
- **API direta:** pra integrações pontuais ou quando não existe MCP Server. Mais trabalho, mais controle.
**Por que isso importa:** Times que misturam esses conceitos acabam com MCPs pesados ou skills que deveriam ser MCPs. A regra: dado mutável → MCP; conhecimento estável → Skill; integração pontual → API direta.
**Pra visualizar:** MCP = porta giratória pro mundo externo. Skill = manual na gaveta. API direta = construir uma porta nova.
**Fonte:** [Rules, Skills, MCPs and Subagents — 24:00](https://youtu.be/omkEi4GTCj8?t=1440)

**Laboratório (30 min):** Configurar um MCP Server simples (filesystem ou GitHub) no Claude Code. Observar o agente descobrindo ferramentas, usando a ferramenta certa e reportando o resultado. Discutir: o que aconteceu que você não fez manualmente?

---

### Módulo 6 — Arquitetura de Contexto: Rules, Skills e Sub-agents (2h)

**O que você vai aprender:**
- Desenhar a arquitetura de contexto de um projeto com os 4 pilares
- Escrever um Agents.md eficaz (máximo 200 linhas)
- Criar uma skill com front matter e triggers claros
- Explicar por que agentes customizados enormes são um antipadrão

**Tópicos:**

#### 6.1 A Evolução 2023-2026: De Tudo no Prompt às Skills Modulares
**A ideia:** A forma como devs interagem com IA passou por 3 fases:
1. **2023-2024 — "Tudo no prompt":** documentação, regras, MCPs, workflows num prompt só. Resultado: contexto gigante, tokens caros, alucinações.
2. **Início de 2025 — Super-agentes:** agentes customizados de 3000+ linhas que faziam tudo. Problema: cada conversa já começava com metade do contexto ocupado.
3. **Meados de 2025 em diante — Skills modulares:** capacidades pequenas, focadas, carregadas sob demanda.
**Por que isso importa:** Se você tá começando agora, pode pular pra fase 3 direto. Não crie agentes enormes. Crie skills pequenas e modulares.
**Pra visualizar:** Fase 1 = todos os ingredientes na panela de uma vez. Fase 2 = robô gigante que gasta metade da energia só pra ligar. Fase 3 = mise en place — cada ingrediente no seu potinho.
**Fonte:** [Rules, Skills, MCPs and Subagents — 14:00](https://youtu.be/omkEi4GTCj8?t=840)

#### 6.2 Os 4 Pilares da Arquitetura de Contexto
**A ideia:** Pensa na arquitetura de uma casa:
1. **Rules / Agents.md = Planta baixa:** o QUE é o projeto — estrutura, convenções, arquitetura.
2. **Skills = Cômodos funcionais:** COMO fazer X — capacidades reutilizáveis e independentes.
3. **MCPs = Portas pro mundo externo:** ONDE buscar/alterar dados — Jira, GitHub, bancos.
4. **Sub-agents = Trabalhadores isolados:** FAÇA isso em paralelo sem poluir meu contexto.
**Por que isso importa:** Essa divisão resolve a confusão mais comum: "isso vai como rule, skill ou MCP?"
**Pra visualizar:** Rules = planta baixa. Skills = ferramentas na caixa. MCPs = portas e janelas. Sub-agents = pedreiros em cômodos diferentes.
**Fonte:** [Rules, Skills, MCPs and Subagents — 09:00](https://youtu.be/omkEi4GTCj8?t=540)

#### 6.3 Rules e Agents.md: A Planta Baixa
**A ideia:** Agents.md (ou CLAUDE.md) é o padrão — um arquivo na raiz do projeto que toda IA lê ao iniciar. Regras:
- **Máximo 200 linhas:** só estrutura de alto nível + ponteiros pra docs detalhadas.
- **Conteúdo típico:** estrutura de diretórios, convenções de código, padrões de commit, links pra docs.
- **Always-apply vs on-demand:** regras críticas sempre carregadas; docs detalhadas sob demanda.
- **Dica pra legados:** peça pra IA analisar o repositório e gerar o Agents.md — Claude Code tem comando `onboard`.
**Por que isso importa:** Um Agents.md bem escrito é o que mais multiplica a qualidade das respostas da IA no seu projeto. Sem ele, a IA erra todas as convenções do time.
**Pra visualizar:** Agents.md = README pra humanos, mas otimizado pra IAs.
**Fonte:** [Rules, Skills, MCPs and Subagents — 10:30](https://youtu.be/omkEi4GTCj8?t=630)

#### 6.4 Skills: Capacidades Portáteis
**A ideia:** Skill é tipo uma classe abstrata — encapsula complexidade e expõe interface simples:
- **Front matter curto:** descrição clara e triggers pra carregamento automático.
- **Portátil:** cria uma vez, usa no Cursor, Claude Code, Copilot. Compartilhável entre times.
- **Exemplo real — Skill Jira Assistant:** encapsula projeto, cloud ID, instância. O dev só diz "corrige CAN-123" e a skill resolve. Sem ela: "corrige CAN-123 na URL techleads.atlassian.net, cloud digital, board CAN..."
- **Trigger automático:** o agente detecta que você mencionou uma task do Jira e carrega a skill.
**Por que isso importa:** Skills transformam conhecimento tribal em ativos reutilizáveis. Em vez de cada dev reinventar a roda, o time compartilha skills. Empresas têm criado "marketplaces internos de skills".
**Pra visualizar:** Skill = classe. MCP = API REST. Sem a classe: você escreve headers, tokens e query params toda vez. Com a classe: `jiraClient.getTask("CAN-123")`.
**Fonte:** [Rules, Skills, MCPs and Subagents — 21:00](https://youtu.be/omkEi4GTCj8?t=1260)

#### 6.5 Sub-agents Genéricos: A Revolução Silenciosa
**A ideia:** A novidade de 2025: você NÃO precisa mais criar sub-agents customizados. Ferramentas modernas (Cursor, Claude Code) têm agentes genéricos que:
- Detectam automaticamente quando paralelizar.
- Iniciam processos isolados com contexto limpo.
- Cada sub-agent pode usar skills disponíveis.
- Só o resultado final volta pro contexto principal.

**Diferença:**
- **Skill:** NÃO reduz contexto — roda no mesmo processo.
- **Sub-agent:** SIM reduz contexto — processo separado, devolve só o output final.
**Por que isso importa:** Antes, sub-agents eram usados pra duas coisas ao mesmo tempo (isolamento + habilidade especializada). Agora cada conceito tem seu lugar: skill = capacidade, sub-agent = isolamento. Você foca em criar boas skills; a ferramenta gerencia os agentes.
**Pra visualizar:** Skill = manual na sua mesa. Sub-agent = assistente que vai pra outra sala e volta só com a resposta.
**Fonte:** [Rules, Skills, MCPs and Subagents — 33:00](https://youtu.be/omkEi4GTCj8?t=1980)

#### 6.6 Da Teoria à Prática: Checklist dos 4 Pilares
**A ideia:**
| Pilar | O que colocar | Máximo | Quando carrega |
|-------|--------------|--------|----------------|
| **Rules / Agents.md** | Estrutura, convenções, ponteiros pra docs | 200 linhas | Always ou on-demand |
| **Skills** | Como criar testes, buscar tasks, gerar release | 500 linhas | On-demand (triggers) |
| **MCPs** | APIs corporativas: Jira, GitHub, bancos | — | Always (conectados) |
| **Sub-agents** | Não crie customizados — ferramentas gerenciam | — | Automático |
**Por que isso importa:** Esse checklist evita o erro clássico: criar um agente de 3000 linhas quando você deveria criar 5 skills de 200 linhas.
**Pra visualizar:** Canivete suíço que faz tudo mal vs kit de ferramentas especializadas.
**Fonte:** [Rules, Skills, MCPs and Subagents — 36:00](https://youtu.be/omkEi4GTCj8?t=2160)

**Laboratório (35 min):**
1. Analisar um "super-agente" hipotético de 3000 linhas e identificar o que deveria virar skills independentes.
2. Escrever um Agents.md pra um projeto real dos participantes.
3. Esboçar uma skill simples (ex.: "gerar changelog a partir de commits") com front matter e trigger.

---

### Módulo 7 — SDD e Ferramentas na Prática (2h30)

**O que você vai aprender:**
- Executar o ciclo SDD completo num cenário real
- Escrever uma spec com user stories, metas e fora de escopo
- Quebrar uma spec em tasks autossuficientes com pré-requisitos
- Comparar ferramentas de IA e selecionar a mais adequada
- Estabelecer um fluxo de documentação viva mantida por IA

**Tópicos:**

#### 7.1 Por que Prompt Direto Falha em Projetos Grandes
**A ideia:** Quando você joga um PRD gigante num prompt e pede "implementa isso", o resultado é um plano raso que perde contexto. A IA não processa 50 requisitos mantendo coerência — prioriza o início, ignora o meio e alucina no final. É o mesmo problema da janela de contexto cheia, aplicado a desenvolvimento de software.
**Por que isso importa:** Explica por que times que tentam "codar tudo com IA" sem método falham. SDD não é burocracia — é estratégia pra contornar limitações das LLMs.
**Pra visualizar:** Prompt direto com PRD gigante = pedir pra um dev implementar 50 features sem dividir em tasks, sem critério de aceite, sem definição de pronto.
**Fonte:** [SDD para Devs — 0:32](https://youtu.be/YFDp-smGYqQ?t=32)

#### 7.2 SDD: As 4 Fases
**A ideia:** Spec-Driven Development em 4 fases:

**Fase 1 — Specify:** definir problema, metas, user stories, fora de escopo. Alinhamento antes de tudo.

**Fase 2 — Design:** diagramas, arquitetura, decisões técnicas. Opcional pra projetos pequenos; essencial pra sistemas com múltiplos módulos ou integrações.

**Fase 3 — Tasks:** quebrar a spec em tarefas autossuficientes. Cada task precisa de: o que fazer, onde (arquivos), pré-requisitos, definition of done. Tasks sem dependências podem rodar em paralelo.

**Fase 4 — Execute:** sub-agents executando tasks em paralelo, cada um com contexto limpo e isolado — só a task específica mais o contexto relevante.
**Por que isso importa:** Cada fase tem contexto reduzido e focado. A IA não precisa "lembrar" de tudo.
**Pra visualizar:** Construção civil. Specify = "quero 3 quartos". Design = planta. Tasks = cronograma. Execute = pedreiros em paralelo.
**Fonte:** [SDD para Devs — 5:28](https://youtu.be/YFDp-smGYqQ?t=328)

#### 7.3 STATE.md: Memória Entre Sessões
**A ideia:** STATE.md persiste o estado do desenvolvimento entre sessões. Guarda decisões e por quê, tasks concluídas, pendentes, blockers e aprendizados. Quando você volta (5 minutos ou 5 dias depois), o agente lê o STATE.md e continua de onde parou.
**Por que isso importa:** Resolve o maior problema de desenvolver com IA: a perda de contexto entre sessões. Sem STATE.md, cada nova conversa começa do zero.
**Pra visualizar:** STATE.md = diário de obra. O pedreiro do turno seguinte lê e sabe exatamente o que foi feito.
**Fonte:** [SDD para Devs — 9:54](https://youtu.be/YFDp-smGYqQ?t=594)

#### 7.4 Documentação Como Combustível
**A ideia:** Na era da IA, documentação deixou de ser burocracia e virou combustível. Quanto melhor documentado seu projeto, mais rápido e preciso o agente trabalha. A dica do Waldemar: a cada feature nova, peça pra IA atualizar as guidelines do projeto. Assim a documentação cresce organicamente.
**Por que isso importa:** Inverte o incentivo: documentar não é mais "perda de tempo que o próximo dev vai aproveitar". É investimento que volta imediatamente na qualidade do código que a IA gera.
**Pra visualizar:** Documentação = gasolina do motor de IA. Sem gasolina, o motor rateia. Com gasolina de qualidade, roda liso.
**Fonte:** [Mini Curso IA para Devs — 41:00](https://youtu.be/90lGnXnMqgo?t=2460)

#### 7.5 Ferramentas: O Que Usar e Quando
**A ideia:** O ecossistema de ferramentas de IA pra desenvolvimento em 2025:

| Ferramenta | Diferencial | Ideal pra |
|-----------|-------------|-----------|
| **Cursor** | Multi-agentes, plan mode, skills e MCPs | Experiência mais completa |
| **GitHub Copilot** | Funciona em qualquer IDE, ecossistema GitHub | Times no GitHub |
| **Claude Code** | Terminal, modelos Claude de alta qualidade, `onboard` nativo | Quem prefere terminal |
| **Windsurf** | Browser interno embutido | Devs frontend |
| **Cline / Roo Code** | Extensões VS Code gratuitas com MCP | Quem não quer pagar |
| **Continue / Aider** | Open-source, foco em planejamento | Quer controle total |

**Critérios de escolha:** ecossistema (usa GitHub? → Copilot), autonomia (modo agente? → Cursor ou Claude Code), custo (orçamento zero? → Cline/Continue), stack (frontend pesado? → Windsurf).
**Por que isso importa:** Não existe ferramenta universal melhor. Existe a certa pro seu contexto. Conhecer o panorama evita o viés de "uso a primeira que vi e nunca testei outras".
**Pra visualizar:** Escolher IDE com IA é que nem carro: SUV completo (Cursor), integrado (Copilot), moto esportiva (Claude Code), conversível (Windsurf).
**Fonte:** [Mini Curso IA para Devs — 66:00](https://youtu.be/90lGnXnMqgo?t=3960)

#### 7.6 RPI: O Ciclo que Alimenta Cada Fase
**A ideia:** RPI (Research → Plan → Implement) é o micro-ciclo dentro de cada fase do SDD:
- **Research:** abrir o leque — pesquisar abordagens, bibliotecas, patterns.
- **Plan:** salvar o plano em markdown — documentar decisão e racional.
- **Implement:** executar as tasks conforme o plano.
**Por que isso importa:** RPI evita o "vibe coding" — codar no feeling sem planejar. Cada decisão tem racional documentado que pode ser revisado depois.
**Pra visualizar:** RPI = método científico no desenvolvimento: formular hipótese → documentar experimento → executar e observar.
**Fonte:** [SDD para Devs — 3:12](https://youtu.be/YFDp-smGYqQ?t=192)

**Laboratório — Workshop Prático Final (50 min):**
Cada participante (ou dupla) recebe um requisito de funcionalidade e executa as 4 fases do SDD com IA:
1. **Specify (10 min):** escrever spec com user stories, metas e fora de escopo.
2. **Design (10 min):** esboçar arquitetura e decisões técnicas.
3. **Tasks (10 min):** quebrar em 3-5 tasks com definition of done.
4. **Execute (15 min):** simular execução com sub-agents (ferramenta à escolha).
5. **Apresentação (5 min):** cada dupla apresenta o STATE.md final. Discussão coletiva.

---

## Referências e Ferramentas

### Vídeos Base (Plano de Nivelamento)
- [Roadmap de IA para DevOps](https://youtu.be/03-nB_KMm44) — Fabrício Veronez (20 min)
- [Prompt Engineering — Guia Prático](https://www.youtube.com/live/Qf_QHxuc8J8) — Fabrício Veronez (2h)
- [SDD: Habilidade #1 para Devs](https://youtu.be/YFDp-smGYqQ) — Waldemar Neto (12 min)

### Vídeos de Expansão
- [Mini Curso IA para Devs](https://youtu.be/90lGnXnMqgo) — Waldemar Neto (1h30)
- [Rules, Skills, MCPs and Subagents](https://youtu.be/omkEi4GTCj8) — Waldemar Neto (50 min)

### Modelos e Execução Local
- `Ollama` — execução local de LLMs open-source
- `Hugging Face` — repositório de modelos, datasets e fine-tunings

### IDEs e Assistentes com IA
- `Cursor` — IDE com multi-agentes, plan mode, skills e MCPs
- `GitHub Copilot` — assistente multi-IDE com CLI
- `Claude Code` — assistente terminal da Anthropic (comando `onboard`)
- `Windsurf` — IDE com browser interno, foco em frontend
- `Cline / Roo Code` — extensões VS Code gratuitas com MCP
- `Continue / Aider` — open-source com foco em planejamento

### Protocolos e Qualidade
- `MCP (Model Context Protocol)` — padrão Anthropic pra integração IA ↔ ferramentas
- `RAGAS` — biblioteca pra métricas de qualidade de pipelines RAG
