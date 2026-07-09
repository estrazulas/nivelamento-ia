# LLM, Embeddings e Busca por Proximidade: Como funciona cada um

Entender a diferenca entre o que o LLM faz internamente e o que os sistemas de busca fazem e essencial para nao confundir as pecas do quebra-cabeca.

---

## 1. A pergunta que gerou este estudo

"O LLM usa embeddings para encontrar resultados por proximidade?"

**Resposta direta:** Nao. O LLM e um gerador de texto, nao um buscador. Quem usa embeddings para encontrar resultados por proximidade e um sistema separado chamado RAG (Retrieval-Augmented Generation).

---

## 2. Como o LLM realmente funciona

O LLM e um gerador, nao um buscador. Quando voce faz uma pergunta, ele nao vai ate um banco de conhecimento, procura o paragrafo mais parecido e te entrega. Ele **gera** a resposta token por token, com base nos padroes que aprendeu durante o treinamento.

### Analogia: o escritor que leu tudo

Pense no LLM como um escritor que leu milhares de livros, artigos e conversas. Se voce pergunta "qual a capital da Franca?", ele nao abre um atlas mental e procura "Franca" para achar "Paris". Ele simplesmente **sabe**, porque aprendeu que depois de "capital da Franca" vem "Paris" em praticamente tudo que leu.

O conhecimento dele esta **embutido nos pesos** (parametros), nao armazenado como texto que ele consulta. E como um musico que sabe tocar de memoria -- ele nao le a partitura, ele lembra o movimento dos dedos.

---

## 3. Onde entram os embeddings

Embeddings sao usados em **sistemas de busca** que sao acessorios ao LLM, nao o proprio LLM.

### O fluxo tipico (RAG)

```
Voce pergunta: "Qual a politica de reembolso?"
        |
        v
  [SISTEMA DE BUSCA]  <-- embeddings entram AQUI
  Pega sua pergunta, transforma em vetor
  Procura por proximidade (cosseno, etc.)
  nos documentos da empresa
        |
        v
  Encontra: "Reembolso em ate 30 dias..." (texto real)
        |
        v
  [LLM]  <-- recebe o texto encontrado + sua pergunta
  "Com base nesse documento, qual a politica?"
        |
        v
  Resposta: "A politica e reembolso em ate 30 dias"
```

O **sistema de busca** (que usa embeddings + similaridade por cosseno) encontra os documentos relevantes em um banco de dados. Depois, o **LLM** apenas le o que foi encontrado e escreve uma resposta coesa em cima disso.

### O que e um embedding na pratica

Embedding e uma representacao numerica do significado de um texto. Imagine que cada frase vira um ponto num espaco de centenas de dimensoes. Frases com significado parecido ficam proximas nesse espaco.

- "Gato comeu o peixe" vira o ponto A
- "O felino devorou o salmona" vira o ponto B (perto de A)
- "A economia cresceu 2%" vira o ponto Z (longe de A)

Quando voce faz uma busca, o sistema transforma sua pergunta em embedding e calcula: "qual documento tem o embedding mais proximo?" -- usando similaridade por cosseno (basicamente, o angulo entre os dois vetores).

---

## 4. Tabela: LLM generativo vs Sistema de busca por embeddings

| Caracteristica | LLM generativo (GPT, Claude, Llama) | Sistema de busca (embedding + vector DB) |
|---------------|-------------------------------------|------------------------------------------|
| O que faz | Gera texto novo | Encontra texto existente |
| Como funciona | Preve a proxima palavra baseado em padroes aprendidos | Transforma texto em vetor e calcula distancia |
| Responde com | Resposta original, criada na hora | Um trecho do documento original |
| Sabe a resposta? | Aprendeu durante o treinamento | Nao sabe nada, so encontra similaridade |
| Pode inventar? | Sim (alucinacao) | Nao (so retorna o que existe no banco) |
| Precisa de internet? | Depende (pode ser local) | So precisa do banco de vetores local |
| Tamanho do conhecimento | Fixo no treinamento (data de corte) | Ilimitado (cresce conforme voce adiciona documentos) |

---

## 5. E a "atencao" dentro do LLM?

Aqui tem uma sutiliza importante. Dentro do proprio LLM existe um mecanismo chamado **atencao** (self-attention) que tambem calcula "proximidade" entre as palavras do seu prompt. Mas e uma proximidade **dentro do contexto atual**, nao uma busca num banco de conhecimento externo.

### Atencao (mecanismo interno do LLM)

Enquanto o LLM esta gerando uma resposta, ele olha para todas as palavras do prompt e pergunta: "qual palavra e mais relevante para a palavra que vou escrever agora?"

Exemplo: na frase "O banco esta cheio de..." -- se a palavra anterior foi "sangue", a atencao da mais peso a "banco" como orgao do corpo. Se foi "dinheiro", a atencao prioriza "banco" como instituicao financeira.

Isso acontece **em tempo real**, durante a geracao de cada token. E interno ao modelo.

### Embedding + busca (sistema externo)

Antes mesmo de chamar o LLM, o sistema de busca transforma sua pergunta inteira em um vetor e procura num banco de vetores qual documento tem o embedding mais similar. Depois, o texto desse documento e colocado no prompt do LLM como contexto.

Isso acontece **antes** do LLM comecar a gerar. E externo ao modelo.

---

## 6. Tabela: Atencao (dentro do LLM) vs Embedding + busca (RAG)

| Caracteristica | Atencao (self-attention) | Embedding + busca por cosseno |
|---------------|-------------------------|------------------------------|
| Onde ocorre | Dentro do LLM, durante a geracao | Fora do LLM, antes de gerar |
| O que compara | Palavras do prompt atual | Sua pergunta vs documentos no banco |
| Alcance | So o que esta no contexto (janela) | Todo o banco de documentos disponivel |
| Finalidade | Entender o sentido dentro da frase | Encontrar informacao relevante externa |
| Resultado | Um peso para cada palavra influenciar a proxima | Um ranking de documentos similares |

---

## 7. Resumo para o dia a dia

- **LLM puro**: funciona com o que aprendeu no treinamento. Nao busca nada, ele gera. Bom para conhecimento geral, conversa, codigo.

- **LLM + RAG**: usa embeddings para buscar documentos relevantes, coloca no prompt, e o LLM responde com base neles. Bom para informacoes atualizadas, documentos da empresa, conhecimento privado.

- **Embedding sozinho**: e so um sistema de busca inteligente. Nao gera nada. Bom para encontrar o documento certo num mar de informacao.

Se seu LLM parece "nao saber" algo especifico da sua empresa, o problema nao e o tamanho do modelo -- e a falta de um sistema de busca (RAG) para alimentar ele com o contexto certo.

---

## Referencias

- [Understand LLM sizes - web.dev](https://web.dev/articles/llm-sizes)
- [O que sao embeddings - OpenAI](https://platform.openai.com/docs/guides/embeddings)
- [RAG (Retrieval-Augmented Generation) - Lewis et al.](https://arxiv.org/abs/2005.11401)
