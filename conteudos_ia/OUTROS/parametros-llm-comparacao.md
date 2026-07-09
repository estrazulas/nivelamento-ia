# Parametros em LLMs: O que sao, como influenciam e comparacao entre tamanhos
Entender o que sao os parametros de um LLM e como eles impactam o resultado e essencial para escolher o modelo certo para cada tarefa -- sem pagar mais do que precisa nem esperar mais do que o necessario.

---

## 1. O que sao parametros?
Imagine que um LLM e uma receita de bolo. Os **parametros** sao os ingredientes e as instrucoes que o modelo aprendeu durante o treinamento: quanta farinha, quanto acucar, em que ordem misturar, por quanto tempo assar.

Tecnicamente, parametros sao **pesos numericos** (valores que o modelo ajusta durante o treinamento) que determinam como o modelo processa e gera texto. Cada parametro e um numero que representa a "forca" de uma conexao entre duas partes do modelo.

Um modelo com 7 bilhoes de parametros tem 7 bilhoes desses numeros internos que trabalham juntos para entender sua pergunta e gerar uma resposta.

---

## 2. Como os parametros influenciam o resultado?
Mais parametros nao significa automaticamente um modelo melhor -- mas da mais **capacidade** para o modelo aprender padroes complexos.

### O que mais parametros permite:
- **Memorizar mais padroes**: um modelo maior consegue aprender relacoes mais sutis entre palavras, contextos mais longos e topics mais especializados
- **Raciocinio mais profundo**: consegue seguir cadeias de logica mais complexas sem se perder
- **Mais conhecimento factual**: absorve mais informacao durante o treinamento
- **Melhor em multilinguas**: consegue manter qualidade em mais idiomas simultaneamente

### O que mais parametros NAO garante:
- Nao substitui qualidade dos dados de treino
- Nao compensa uma arquitetura mal desenhada
- Nao e linear -- depois de um certo ponto, cada parametro extra traz menos ganho

### Analogia: a equipe de estagiarios
Pense em cada parametro como um estagiario que sabe fazer uma coisa especifica.

- **Modelo pequeno (3B)**: 3 estagiarios. Cada um faz varias coisas, mas raso. Se voce pedir algo complexo, eles tentam mas podem errar.
- **Modelo medio (8B)**: 8 estagiarios. Mais especializados. Um entende de matematica, outro de codigo, outro de lingua portuguesa. Eles se ajudam e produzem um resultado melhor.
- **Modelo grande (70B)**: 70 estagiarios super especializados. Voce tem experts em cada area. O resultado e de altissima qualidade -- mas coordenar 70 pessoas custa caro e demora mais.

---

## 3. Tabela de tamanhos: pequeno, medio e grande
| Categoria | Parametros | Exemplos de modelos | RAM/VRAM necessaria (FP16) | Custo por inferencia |
| --- | --- | --- | --- | --- |
| Pequeno | 1B - 8B | Phi-3 (3.8B), Gemma 2 (2B/9B), Llama 3.2 (3B), Mistral 7B | 2 GB - 16 GB | Baixo (centavos por milhoes de tokens) |
| Medio | 8B - 30B | Llama 3.1 (8B), Gemma 2 (27B), Mixtral 8x7B (ativa 12.9B) | 16 GB - 60 GB | Moderado |
| Grande | 30B - 70B | Llama 3.1 (70B), Command R+ (104B), DeepSeek V2 (67B) | 60 GB - 140 GB | Alto (dolares por milhao de tokens) |
| Muito Grande | 100B+ | GPT-4 (est. 1T+), Claude 3 Opus, Gemini Ultra | Centenas de GB | Muito alto |

### Como calcular o tamanho em GB:
A formula e simples: parametros x bytes por parametro (precisao).

| Precisao | Bytes por parametro | Exemplo: 7B (Mistral) | Exemplo: 70B (Llama 3) |
| --- | --- | --- | --- |
| FP32 (precisao total) | 4 bytes | 28 GB | 280 GB |
| FP16 (meia precisao) | 2 bytes | 14 GB | 140 GB |
| INT8 (quantizado) | 1 byte | 7 GB | 70 GB |
| INT4 (alta compressao) | 0.5 byte | 3.5 GB | 35 GB |

Na pratica, a maioria dos modelos roda em FP16 ou INT8. Um modelo de 7B cabe em uma GPU de 16 GB (com espaco para contexto). Um modelo de 70B precisa de varias GPUs ou versao quantizada.

---

## 4. Comparacao pratica: exemplos de tres tamanhos

### Pequeno (3B-8B) - Exemplo: Phi-3 Mini (3.8B)
**Onde roda:** notebook, celular, Raspberry Pi, GPU de 8 GB

**Exemplo de uso:** chatbot de atendimento ao cliente para uma loja pequena

- Pergunta: "Qual o horario de funcionamento?"
- Resposta: rapida (< 1 segundo), correta, direta
- Custo: praticamente zero (roda local)
**O que ele faz bem:** tarefas simples, respostas diretas, classificacao de texto, extracao de informacao basica

**Onde ele falha:** raciocinio matematico complexo, codigo multi-etapas, analise de sentimento sutil, contextos muito longos

**Benchmark comparativo:** Phi-3 Mini acerta cerca de 69% no MMLU (teste de conhecimento geral), enquanto versoes maiores passam de 80%

### Medio (8B-13B) - Exemplo: Llama 3.1 (8B), Mistral 7B
**Onde roda:** GPU de 16-24 GB (quantizado)

**Exemplo de uso:** assistente de codigo para programador freelancer

- Pergunta: "Refatore esta funcao para usar async/await e adicione tratamento de erros"
- Resposta: leva 2-3 segundos, codigo funcional, explicacao do que mudou
- Custo: alguns centavos por chamada via API
**O que ele faz bem:** chatbot geral, resumo de textos, traducao, codigo simples a moderado, perguntas e respostas, RAG (busca em documentos)

**Onde ele falha:** problemas de matematica avancada, raciocinio logico multi-etapas muito longo, codigo muito complexo

**Benchmark:** Mistral 7B acerta cerca de 64% no MMLU, Llama 3.1 8B chega a 66%

### Grande (70B+) - Exemplo: Llama 3.1 (70B)
**Onde roda:** cluster de GPUs (2-8x A100/H100) ou via API na nuvem

**Exemplo de uso:** analise juridica de contratos complexos

- Pergunta: "Identifique todas as clausulas abusivas neste contrato de 50 paginas, compare com a legislacao vigente e aponte riscos"
- Resposta: leva 5-10 segundos, analise detalhada com citacoes, identificacao correta de riscos legais, sugestoes de alteracao
- Custo: varios centavos a alguns dolares por chamada
**O que ele faz bem:** raciocinio complexo, analise de documentos longos, codigo avancado, matematica, planejamento multi-etapas, tarefas que exigem conhecimento especializado profundo

**Onde ele falha:** custo alto, latencia maior, nao roda localmente (so nuvem ou servidores dedicados)

**Benchmark:** Llama 3.1 70B acerta cerca de 79% no MMLU, chegando perto de GPT-4 em varias tarefas

---

## 5. Tabela comparativa final: quando usar cada tamanho
| Caracteristica | Pequeno (1B-8B) | Medio (8B-30B) | Grande (70B+) |
| --- | --- | --- | --- |
| Velocidade | Muito rapido | Rapido | Moderado a lento |
| Custo por token | Baixissimo | Baixo | Alto |
| Roda localmente | Sim (CPU ou GPU basica) | GPU media (16-24 GB) | Nao (cluster/API) |
| Qualidade de raciocinio | Basico | Bom | Excelente |
| Ideal para | Automacao, edge, mobile, tarefas simples | Chat, APIs, uso geral | Pesquisa, analise complexa, juridico, medicina |
| Consumo de energia | 5-50W | 100-300W | 1000W+ |
| Analogia | Um estagiario | Um profissional experiente | Um comite de especialistas |

---

## 6. Mas tamanho nao e tudo
Aqui vai o ponto mais importante: **parametros sao apenas um dos fatores**.

Dois modelos com o mesmo numero de parametros podem ter performances muito diferentes por causa de:

- **Qualidade dos dados de treino**: um modelo treinado com dados limpos e curados pode superar outro com o dobro de parametros treinado com dados ruidosos
- **Arquitetura**: modelos mais modernos (como Mixtral MoE ou DeepSeek) conseguem mais com menos parametros ativos
- **Quantizacao**: um modelo de 9B em INT4 pode rodar onde um de 2B em FP32 nao caberia, e performar melhor
- **Fine-tuning**: um modelo pequeno ajustado para uma tarefa especifica pode superar um modelo grande generico

### Exemplo real: Mixtral 8x7B
O Mixtral tem 46 bilhoes de parametros no total, mas usa apenas **12.9 bilhoes ativos** por inferencia (arquitetura MoE - Mixture of Experts). Ele compete de igual para igual com modelos de 30B-70B, mas custa muito menos:

| Modelo | Parametros totais | Parametros ativos | MMLU | Custo relativo |
| --- | --- | --- | --- | --- |
| Llama 2 13B | 13B | 13B | 54% | 1x |
| Mixtral 8x7B | 46B | 12.9B | 70% | 1.2x |
| Llama 2 70B | 70B | 70B | 69% | 5x |

O Mixtral entrega performance de modelo grande com custo de modelo medio.

---

## 7. Resumo para o dia a dia
- **Para uso pessoal / automacao**: modelos de 3B-8B (Phi-3, Gemma, Llama 3.2 3B) sao otimos e rodam no seu notebook
- **Para API geral / chatbot**: modelos de 8B-13B (Llama 3.1 8B, Mistral) oferecem o melhor custo-beneficio
- **Para tarefas complexas / analise profunda**: modelos de 70B+ (Llama 3.1 70B, GPT-4) valem o custo extra
- **Nao julgue so pelo numero de parametros**: arquitetura, dados de treino e fine-tuning importam tanto quanto tamanho
- **Parametros sao como cilindradas de um motor**: um motor 1.0 bem projetado pode ser mais eficiente que um 2.0 mal feito, mas para carregar carga pesada o 2.0 ainda ganha

---

## 8. O que sao os pesos de uma LLM?
A secao 1 falou rapidamente que parametros sao "pesos numericos", mas vamos aprofundar com exemplos concretos.

### A analogia do professor que da notas
Imagine que voce esta aprendendo a identificar animais. Um professor te mostra uma foto e pergunta: "O que e isso?"

- Se voce chuta "cachorro" e era um gato, o professor anota mentalmente: "prestar mais atencao em orelhas pontudas"
- Se voce acerta "gato", o professor anota: "orelhas pontudas foi um bom indicio, continuar assim"
Os **pesos** de uma LLM funcionam como as anotacoes mentais desse professor - mas em vez de algumas dezenas de anotacoes, sao **bilhoes** delas.

Tecnicamente, um peso e um numero (como 0.73, -1.2, 8.45) que controla a forca de uma conexao entre dois neuronios artificiais. Quando o modelo ve a palavra "gato", cada peso decide:

- **Peso positivo grande** (+8.5): "essa palavra ativa fortemente a ideia de 'animal peludo'"
- **Peso negativo grande** (-6.2): "essa palavra **nao** tem nada a ver com 'veiculo'"
- **Peso proximo de zero** (+0.07): "essa palavra e meio irrelevante pra esta conexao"

### Exemplo pratico: montando uma frase
Pense numa rede neural miniaturizada com apenas 3 pesos que decide a proxima palavra depois de "O ceu esta":

| Palavra possivel | Peso do contexto "ceu" | Peso do contexto "esta" | Soma | Resultado |
| --- | --- | --- | --- | --- |
| azul | +9.2 | +0.3 | 9.5 | MAIS PROVAVEL |
| chovendo | +1.1 | +7.8 | 8.9 | TAMBEM PROVAVEL |
| vermelho | -3.5 | +0.1 | -3.4 | IMPROVAVEL |
| bicicleta | -8.0 | -2.0 | -10.0 | QUASE IMPOSSIVEL |

Os pesos (+9.2, +0.3, -8.0) sao os numeros que o modelo aprendeu durante o treinamento. Eles determinam que "azul" combina fortemente com "ceu", enquanto "bicicleta" nao combina com nada ai.

Uma LLM real tem bilhoes desses pesos organizados em camadas. Cada camada examina um aspecto diferente: a primeira camada olha letras isoladas, a segunda olha combinacoes de letras, a terceira olha palavras, a quarta olha frases, e assim por diante.

### O olhar do desenvolvedor: pesos como parametros de uma funcao
Se voce ja programou, a melhor forma de entender pesos e pensar neles como **parametros de uma funcao matematica gigante** que o modelo vai ajustando.

Imagine a funcao mais simples possivel para prever o preco de uma casa:

```python
preco = (peso1 * tamanho) + (peso2 * quartos) + (peso3 * localizacao) + vies

```
Onde `peso1`, `peso2`, `peso3` e `vies` sao os **parametros** que o modelo precisa descobrir. No inicio, eles sao aleatorios:

- peso1 = 0.5, peso2 = 0.3, peso3 = 0.1, vies = 0
O modelo chuta o preco de uma casa de 100m2, 3 quartos, boa localizacao:

```plaintext
preco = (0.5 * 100) + (0.3 * 3) + (0.1 * 10) + 0 = 50 + 0.9 + 1 = 51.9

```
O preco real era 350. O erro e enorme. O modelo entao **ajusta os pesos**:

- peso1 sobe de 0.5 para 2.8 (tamanho importa mais do que ele pensava)
- peso3 sobe de 0.1 para 8.0 (localizacao importa MUITO)
- peso2 desce de 0.3 para 0.2 (numero de quartos nem tanto)
Depois de milhares de ajustes, os pesos convergem para valores que funcionam. Uma LLM e exatamente a mesma ideia, mas em vez de 4 pesos, sao **bilhoes** deles, organizados em matrizes multidimensionais, processando tokens em vez de precos de casa.

```python
# Versao ultra-simplificada do que acontece dentro de uma LLM
# Cada "neuronio" e uma multiplicacao de matrizes

# embedding da palavra de entrada
token = embed("gato")  # vira um vetor de 4096 numeros

# camada 1: atencao - em quais palavras prestar atencao
# peso_atencao e uma matriz 4096x4096 (16 milhoes de pesos)
atencao = matmul(peso_atencao, token)

# camada 2: processamento - o que essa combinacao significa
# peso_processamento e outra matriz 4096x4096
processado = matmul(peso_processamento, atencao)

# resultado final: probabilidade de cada palavra do vocabulario
# peso_saida e uma matriz 32000x4096 (128 milhoes de pesos)
probabilidades = matmul(peso_saida, processado)
# "gato" -> 0.0001, "animal" -> 0.3, "felino" -> 0.15, "mamifero" -> 0.08 ...

```
Cada uma dessas matrizes (`peso_atencao`, `peso_processamento`, `peso_saida`) e composta de pesos numericos que foram aprendidos durante o treinamento. Um modelo de 7B tem cerca de 7 bilhoes desses numeros espalhados por dezenas de camadas e milhares de matrizes.

### A sopa de letrinhas
Outra analogia: imagine que o modelo e uma sopa de letrinhas. Cada peso e um palito que conecta duas letrinhas na sopa. Quando voce pergunta algo, os palitos vibram em uma sequencia especifica - e a sopa inteira se reorganiza para formar a resposta.

O que chamamos de "modelo de 7 bilhoes de parametros" e uma sopa com 7 bilhoes de palitos conectando bilhoes de letrinhas. Cada palito tem uma "tensao" diferente (o peso numerico) que determina o quanto aquela conexao influencia o resultado final.

---

## 9. Como funciona o treinamento de uma LLM?

### O basico: aprender errando
Treinar uma LLM e como ensinar uma crianca a falar - mas em velocidade altissima e com uma quantidade absurda de exemplos.

A crianca (o modelo) comeca sabendo zero. Ela ve frases, tenta adivinhar a proxima palavra, erra, ajusta, tenta de novo, ate acertar. Esse ciclo de "tentar, errar, ajustar" e repetido bilhoes de vezes.

### Passo a passo com um exemplo concreto
Vamos treinar um modelo MINIATURA para completar a frase: "O cafe esta ___".

**Passo 1: o modelo chuta**

O modelo, recem-nascido, tem pesos aleatorios. Ele chuta qualquer palavra: "O cafe esta bicicleta."

**Passo 2: comparar com o certo**

O professor (um algoritmo chamado **funcao de perda** ou loss) compara: o modelo disse "bicicleta", mas a resposta correta no texto de treino era "quente". A diferenca entre "bicicleta" e "quente" gera um numero: o erro.

**Passo 3: calcular o ajuste**

O algoritmo **backpropagation** (propagacao reversa) pergunta: "qual peso foi o mais culpado por esse erro?" O peso que ligava "cafe" a "bicicleta" era muito forte - entao ele e reduzido. O peso que ligava "cafe" a "quente" era muito fraco - entao ele e aumentado.

**Passo 4: ajustar os pesos**

Cada um dos bilhoes de pesos e ajustado um pouquinho. O ajuste e controlado por um numero chamado **taxa de aprendizado** (learning rate). Se a taxa e 0.001, o peso 8.5 vira 8.499 - uma mudanca microscopica. Mas com bilhoes de pesos e trilhoes de exemplos, essas microscopias se acumulam em conhecimento real.

**Passo 5: repetir**

O modelo tenta de novo com uma frase diferente: "O cafe esta quente." Agora o erro e menor. Ele continua tentando, ajustando, tentando de novo, por semanas ou meses.

### Exemplo pratico: treinar para entender "frio" vs "quente"
Imagine ensinar o modelo a diferença entre "frio" e "quente". O modelo ve milhares de frases:

- "O cafe esta quente"
- "O sorvete esta frio"
- "O cha esta quente"
- "A agua esta fria"
Cada vez que o modelo erra "quente" quando deveria ser "frio", os pesos da conexao entre "sorvete" e "quente" diminuem, e os pesos entre "sorvete" e "frio" aumentam. Depois de milhares de exemplos, o modelo forma uma "regiao" no espaco de pesos onde "sorvete", "gelo", "inverno" ficam perto de "frio", enquanto "cafe", "forno", "verao" ficam perto de "quente".

### O olhar do desenvolvedor: treinar e como treinar um modelo de machine learning
Se voce ja treinou um modelo de machine learning (regressao linear, random forest, ate mesmo uma rede neural simples no Keras/TensorFlow/PyTorch), o principio e o MESMO. A diferenca e que uma LLM e um modelo de machine learning com **bilhoes de parametros** em vez de centenas.

Eis um codigo que captura a essencia do treinamento - do ML classico ate a LLM:

```python
# === NIVEL 1: Regressao linear classica (3 parametros) ===
# Isso e o mais simples possivel. O modelo tem 3 pesos.

from sklearn.linear_model import LinearRegression

# Dados: tamanho da casa em m2, preco
X = [[50], [80], [120], [200]]
y = [150000, 240000, 360000, 600000]

modelo = LinearRegression()
modelo.fit(X, y)  # <-- aqui o sklearn ajusta os pesos internos

# O modelo aprendeu: preco = (peso * tamanho) + vies
# peso ≈ 3000, vies ≈ 0
print(modelo.predict([[100]]))  # ~300000

# === NIVEL 2: Rede neural simples no PyTorch (alguns milhares de parametros) ===
# Mesma ideia, mas com mais camadas e mais pesos

import torch
import torch.nn as nn

class RedeNeural(nn.Module):
    def __init__(self):
        super().__init__()
        # Cada nn.Linear cria uma matriz de pesos
        # camada1: 100 entradas -> 64 saidas = 100*64 + 64 = 6464 parametros
        self.camada1 = nn.Linear(100, 64)
        # camada2: 64 entradas -> 32 saidas = 64*32 + 32 = 2080 parametros
        self.camada2 = nn.Linear(64, 32)
        # saida: 32 entradas -> 10 classes = 32*10 + 10 = 330 parametros
        self.saida = nn.Linear(32, 10)

    def forward(self, x):
        x = torch.relu(self.camada1(x))
        x = torch.relu(self.camada2(x))
        return self.saida(x)

modelo = RedeNeural()  # ~8874 parametros no total

# O CICLO DE TREINAMENTO e o mesmo de uma LLM:
otimizador = torch.optim.SGD(modelo.parameters(), lr=0.01)
funcao_perda = nn.CrossEntropyLoss()

for epoca in range(100):
    # Passo 1-2: modelo chuta, calcula erro
    chute = modelo(dados_entrada)
    erro = funcao_perda(chute, resposta_certa)

    # Passo 3-4: backpropagation + ajuste dos pesos
    otimizador.zero_grad()
    erro.backward()     # calcula quanto cada peso contribuiu pro erro
    otimizador.step()   # ajusta cada peso um pouquinho (lr=0.01)

    # Passo 5: repetir
    # Cada epoca = uma passada completa pelos dados

print(f"Erro final: {erro.item():.4f}")

# === NIVEL 3: LLM (bilhoes de parametros) ===
# Exatamente a mesma estrutura do nivel 2, mas:
# - Em vez de nn.Linear(100, 64), sao centenas de camadas com milhares de entradas
# - Em vez de SGD, usa AdamW com schedules complexos
# - Em vez de 100 epocas em 1000 amostras, sao semanas em trilhoes de tokens
# - Em vez de 8874 parametros, sao 7 bilhoes ou mais
# - A "funcao de perda" e a cross-entropy de prever a proxima palavra

```
O loop de treinamento - tentar, calcular erro, voltar ajustando pesos, repetir - e identico em todos os tres niveis. O que muda e a escala:

| Aspecto | Regressao Linear | Rede Neural sua | LLM (ex: Llama 3.1 8B) |
| --- | --- | --- | --- |
| Numero de pesos | 2-100 | 8.874 | 8.000.000.000 |
| Dados de treino | 4 casas | 10.000 imagens | 15 trilhoes de tokens |
| Tempo de treino | 0.001 segundo | 5 minutos | 30 dias em 16.000 GPUs |
| Custo | CPU do notebook | GPU de US$ 500 | US$ 10-15 milhoes |
| Onde roda o resultado | Notebook | Notebook | Precisa de datacenter |

A matematica e a mesma. A escala e que e absurda.

### Como uma LLM realmente aprende codigo
Durante o pre-treinamento, a LLM le bilhoes de exemplos de codigo-fonte do GitHub. Cada vez que ela ve:

```python
def soma(a, b):
    return a + _

```
Ela tenta adivinhar o `_` (que seria `b`). Se erra e chuta `a`, o backpropagation ajusta os pesos para que da proxima vez ela perceba que depois de `a + `o mais provavel e o segundo parametro.

Depois de ver esse padrao milhoes de vezes em milhares de repositorios, os pesos formam uma representacao interna do que e "somar dois numeros em Python". Nao e uma copia de codigo - e um entendimento estatistico de como a sintaxe de Python funciona.

E por isso que uma LLM consegue escrever codigo que ela nunca viu antes: ela nao esta copiando, esta **aplicando os pesos que aprendeu** para gerar a sequencia mais provavel de tokens.

### As tres fases do treinamento
| Fase | O que acontece | Analogia | Duração |
| --- | --- | --- | --- |
| Pre-treinamento | O modelo le bilhoes de textos da internet e aprende a lingua: gramatica, fatos basicos, padroes | Uma crianca lendo enciclopedia durante meses | Semanas a meses, milhares de GPUs |
| Fine-tuning (ajuste fino) | O modelo e treinado com exemplos curados de pergunta-resposta, seguindo instrucoes | Um estagiario fazendo treinamento especifico para o cargo | Dias, dezenas de GPUs |
| RLHF (reforco com feedback humano) | Humanos avaliam as respostas do modelo, e ele aprende a preferir o que agrada mais | Um chef provando a comida do cozinheiro e dando notas | Semanas |

### O que NAO acontece no treinamento
Muita gente pensa que treinar um modelo e como instalar um programa - voce baixa e pronto. Na verdade:

- **Nao** e copiar conhecimento de um banco de dados. O modelo nao "armazena" frases.
- **Nao** e decorar respostas. O modelo nao tem um arquivo de perguntas frequentes.
- **Nao** e ligar um interruptor. O modelo comeca sabendo zero e vai melhorando gradualmente.
O que realmente acontece: o modelo ajusta bilhoes de pesos numericos ate que, estatisticamente, ele consiga prever a proxima palavra com alta precisao. O conhecimento "emerge" desse processo - nao e inserido explicitamente em lugar nenhum.

### O custo do treinamento
Treinar uma LLM grande e absurdamente caro:

| Modelo | Parametros | Custo estimado de treino | Energia | Data |
| --- | --- | --- | --- | --- |
| GPT-3 | 175B | ~US$ 4.6 milhoes | Equivalente a 100 casas por mes | 2020 |
| Llama 3.1 70B | 70B | ~US$ 10-15 milhoes | 30.000 horas de GPU H100 | 2024 |
| GPT-4 (estimado) | ~1.8T | ~US$ 100-200 milhoes | Centenas de milhares de horas GPU | 2023 |

Por isso que modelos prontos sao alugados via API em vez de cada empresa treinar o seu. E como construir uma usina nuclear so pra fazer cafe - tecnicamente possivel, mas completamente sem sentido para a maioria dos usos.

---

## 10. Especializacao: modelos que sao bons em coisas diferentes

### Porque um modelo e melhor em codigo e outro em criatividade?
Imagine dois cozinheiros. Ambos fizeram a mesma escola de culinaria (pre-treinamento), mas depois cada um fez um estagio diferente:

- **Cozinheiro A** estagiou 1 ano em uma cozinha industrial, servindo 1000 marmitas por dia. Ele e rapido, preciso, segue receitas a risca.
- **Cozinheiro B** estagiou em um restaurante estrelado, criando pratos novos toda semana. Ele e criativo, inovador, mas as vezes demora mais.
A **base** dos dois e a mesma (sabem cortar legumes, fazer molhos, assar). A **especializacao** veio do estagio (fine-tuning) que cada um fez.

Com LLMs acontece a mesma coisa. O pre-treinamento da a base (lingua, gramatica, raciocinio basico). O fine-tuning direciona o modelo para uma area especifica.

### E sim: a especializacao e feita na etapa de fine-tuning
O fine-tuning e o processo de pegar um modelo pre-treinado generico e treina-lo COM MAIS EXEMPLOS de um dominio especifico. E como pegar um recem-formado em medicina e fazer ele estagiar 2 anos em cardiologia.

Tecnicamente, o fine-tuning funciona assim:

```plaintext
1. Pega o modelo pre-treinado (ex: Llama 3.1 8B, que "sabe" lingua mas nao segue instrucoes)
2. Cria um dataset de milhares de pares pergunta-resposta de um dominio especifico
   - Ex: 100.000 pares de (bug em Python, correcao) para codigo
   - Ex: 100.000 pares de (roteiro de video, sugestao criativa) para criatividade
3. Continua o treinamento: o modelo ve os pares, tenta responder, calcula erro, ajusta pesos
4. Depois de algumas epocas, os pesos do modelo se "especializam" naquele dominio

```
O que muda nos pesos durante o fine-tuning:

- Os pesos que eram uteis para o dominio alvo sao **reforcados** (ficam mais extremos, mais precisos)
- Os pesos que eram para outras areas sao **enfraquecidos** ou mantidos
- O modelo inteiro nao "reescreve" - ele apenas ajusta os pesos que importam para a nova tarefa
Tecnicamente, o fine-tuning pode ser feito de duas formas:

| Tecnica | O que faz | Custo | Exemplo de uso |
| --- | --- | --- | --- |
| Full fine-tuning | Ajusta TODOS os bilhoes de pesos | Muito caro (GPU days) | Criar um modelo especializado do zero |
| LoRA / QLoRA | Congela os pesos originais e adiciona "adaptadores" pequenos (milhoes de pesos extras) | Barato (GPU horas) | Ajustar um modelo para sua empresa sem perder a base generica |

Na pratica, LoRA e a tecnica mais usada: voce mantem o modelo original intacto e adiciona um "adesivo" de alguns milhoes de pesos que so ativam para a sua tarefa. Da pra ter varios adesivos no mesmo modelo base.

### Tabela: especializacao dos modelos mais conhecidos (2024-2025)
| Modelo | Parametros | Especialidade | O que faz de melhor | Onde peca |
| --- | --- | --- | --- | --- |
| DeepSeek V4 | ~600B (MoE) | Raciocinio e exatas | Matematica, logica, ciencia, resolucao de problemas complexos | Custa caro, pesado para tarefas simples |
| Claude Sonnet 4 | ~200B (est.) | Codigo e analise | Programacao multi-arquivo, refatoracao, analise de codigo legado | Criatividade literaria, textos muito abertos |
| Claude Haiku 3.5 | ~15B | Velocidade e baixo custo | Respostas rapidas, chatbot, classificacao | Raciocinio complexo, tarefas multi-etapas |
| Gemini 2.5 Pro | ~500B (est.) | Multimodal e contexto longo | Processar videos, imagens, audio, documentos de 1M+ tokens | Custo alto, latencia maior |
| GPT-4o | ~1T (est.) | Generalista versatil | Faz tudo razoavelmente bem: codigo, texto, analise, criatividade | Nao e o melhor em nada especifico, mas o mais equilibrado |
| Llama 3.1 70B | 70B | Custo-beneficio geral | Aberto, roda localmente (com GPU forte), comparavel a GPT-4 em muitas tarefas | Precisa de infra, versao base requer fine-tuning |
| Llama 3.2 90B (Vision) | 90B | Visao + texto | Analisar imagens, documentos escaneados, diagramas | Nao processa video, so imagens estaticas |
| Mistral Large 2 | 123B | Multilingue e codigo | Excelente em portugues e outras linguas menos comuns, bom em codigo | Menos conhecido, ecossistema menor |
| Phi-3 / 4 | 3.8B - 14B | Mobile e edge | Roda no celular, respostas instantaneas, tarefas simples e rapidas | Nao faz raciocinio complexo, contexto limitado |
| Command R+ | 104B | RAG e empresarial | Busca em documentos grandes, citacao de fontes, conversas com contexto | Codigo sofrivel, nao recomendado para programacao |
| Grok 3 | ~300B (est.) | Analise de dados em tempo real | Acesso ao X/Twitter, noticias frescas, analise de trendings | Conhecimento superficial, viesse politico |
| GLM-5.2 | — | Codigo e raciocinio | Flagship da Z.AI, 1M de contexto, melhor modelo open-source em SWE-bench e Terminal-Bench, modo thinking integrado | So texto (nao processa imagens), pesado para tarefas simples |
| GLM-5V-Turbo | — | Codigo multimodal | Primeiro modelo multimodal de codigo da Z.AI, entende imagem/video/texto, 200K contexto, recria front-end a partir de mockups | Limitado a 200K de contexto (vs 1M do 5.2), nao gera video |
| GLM-Image | — | Imagem (text-to-image) | Geracao de imagens, SOTA em cenas complexas | So imagem, nao processa texto |
| CogVideoX-3 | — | Video (text-to-video) | Geracao de video com estabilidade melhorada | Qualidade ainda inferior a Hailuo/Midjourney video |
| MiniMax-M3 | — | Codigo multimodal | Modelo frontier com 1M de contexto, multimodal (texto + imagem), melhor da MiniMax para codigo | Novo, ecossistema menor que DeepSeek/Claude |
| MiniMax-M2.7 | — | Engenharia geral | Top em tarefas reais de engenharia, refinamento recursivo, interacao com personalidade | Versao normal (sem highspeed) pode ser mais lenta |
| MiniMax-M2.7-highspeed | — | Codigo e velocidade | Mesma qualidade do M2.7 com inferencia muito mais rapida, refatoracao precisa | Mesmo que o M2.7, so que mais rapido |
| MiniMax Hailuo 2.3 | — | Video (text-to-video) | SOTA em geracao de video, 1080p ate 10s, fisica realista, instruction following | Custo por video ainda alto para uso intensivo |
| DeepSeek V4 Flash | ~80B (MoE ativo) | Raciocinio rapido e barato | Quase a qualidade do V4 Pro mas muito mais barato e rapido | Menos profundo que o V4 Pro em problemas extremamente complexos |
| DeepSeek V4 Pro | ~600B (MoE) | Raciocinio profundo | Problemas de altissima complexidade, pesquisa, matematica avancada | Custa 10x mais que o Flash |

### Por que o DeepSeek V4 tem versao Flash e Pro?
O DeepSeek V4 e um exemplo perfeito de especializacao via fine-tuning:

- **Pre-treinamento**: um modelo unico de ~600B parametros (MoE) treinado com dados genericos
- **Fine-tuning 1**: criaram o **V4 Pro** — fine-tuning para raciocinio profundo, pensamento lento e elaborado
- **Fine-tuning 2**: criaram o **V4 Flash** — fine-tuning para eficiencia, pensamento rapido, priorizando velocidade e baixo custo
O mesmo modelo base, dois fine-tunings diferentes, dois produtos completamente diferentes. O Flash nao e uma versao "pior" do Pro — e uma versao **otimizada para um cenario diferente**.

E como ter o mesmo engenheiro em dois modos: o modo "vou fazer uma planilha detalhada com todas as variaveis" (Pro) vs o modo "vou te dar uma estimativa rapida em 10 segundos" (Flash).

### Como escolher o modelo certo
| Se voce precisa de... | Melhor escolha | Por que |
| --- | --- | --- |
| Codigo e refatoracao multi-arquivo | Claude Sonnet 4 ou GLM-5.2 | Sonnet 4 e o padrão ouro em codigo; GLM-5.2 e o melhor open-source, lidera SWE-bench e Terminal-Bench com 1M de contexto |
| Codigo multimodal (front-end a partir de mockups) | GLM-5V-Turbo | Primeiro modelo multimodal de codigo, entende imagem + texto, recria paginas a partir de design |
| Matematica e raciocinio profundo | DeepSeek V4 Pro | Fine-tuning pesado em raciocinio logico e cadeias de pensamento |
| Raciocinio rapido e barato | DeepSeek V4 Flash | Qualidade proxima do Pro por uma fracao do custo, ideal para automacao |
| Atendimento ao cliente | Claude Haiku 3.5 ou DeepSeek V4 Flash | Rapido, barato, responde em milissegundos |
| Criatividade e escrita | GPT-4o | Fine-tuning com dados literarios, mais versatil em tom de voz |
| Processar videos e audio | Gemini 2.5 Pro | Treinado multimodal desde o inicio, processa video/audio/imagem/texto |
| Geracao de video | MiniMax Hailuo 2.3 | SOTA em text-to-video, 1080p ate 10s, fisica realista |
| RAG em documentos grandes | Command R+ | Fine-tuning especifico para citacao de fontes e buscas |
| Rodar local / offline (GPU forte) | Llama 3.1 70B ou Phi-4 | Modelos abertos, rodam na sua maquina |
| Rodar local / edge (GPU modesta) | MiniMax-M3 via API ou Phi-4 | 1M de contexto, multimodal, mas via API; Phi-4 roda local |
| Automacao barata (API) | DeepSeek V4 Flash | Centavos por milhao de tokens, qualidade alta |
| Pesquisa academica | DeepSeek V4 Pro ou GLM-5.2 | Raciocinio profundo, menos alucinacao, contexto longo |
| Engenharia geral de software | MiniMax-M2.7 | Top em tarefas reais de engenharia, refinamento recursivo |
| Multilingue (Portugues, etc.) | Mistral Large 2 | Excelente em linguas menos comuns, ecossistema europeu forte |
| Processar documentos 1M+ tokens | Gemini 2.5 Pro ou GLM-5.2 | Gemini 1M+ nativo; GLM-5.2 com 1M de contexto e function calling |
| Agente de codigo autonomo (longa duracao) | MiniMax M3 | Rodou 12h sozinho, 147 submissoes de benchmark, 18 commits autonomos |
| Tool calling em automacao | MiniMax M2.7 | Comunidade elogia: "MiniMax e muito bom em tool calling" |
| Claude planeja + MiniMax executa | MiniMax M3 ou M2.7 | Estrategia comum: Claude pra arquitetura, MiniMax pra codigo |

### Onde a MiniMax se destaca (M3 e M2.7)

A MiniMax virou referencia em custo-beneficio para codigo, especialmente depois do M3. Dados de benchmarks e comunidades:

**MiniMax M3 — agente de codigo autonomo e multimodal**

Lancado em meados de 2026, o M3 e o primeiro modelo open-weight a combinar codigo frontier, 1M de contexto e multimodalidade nativa. Usa uma arquitetura propria chamada MiniMax Sparse Attention (MSA) que reduz o custo por token em contextos longos para 1/20 da geracao anterior.

Benchmarks (fonte: VentureBeat e MiniMax oficial):

| Benchmark | M3 | vs GPT-5.5 | vs Opus 4.8 | vs DeepSeek V4 Pro |
|-----------|-----|-----------|-------------|-------------------|
| SWE-Bench Pro | 59.0% | A frente | Atras (69.2%) | A frente (55.4%) |
| Terminal-Bench 2.1 | 66.0% | - | Atras (74.6%) | Emparelhado (67.9%) |
| BrowseComp | 83.5% | - | A frente Opus 4.7 (79.3%) | Emparelhado (83.4%) |
| MCP Atlas | 74.2% | - | - | A frente (73.6%) |

Custo: $0.30 / $1.20 por milhao de tokens (preco de lancamento) — de 5 a 10x mais barato que GPT-5.5 ($5/$30) ou Opus 4.8 ($5/$25).

**Cenarios onde o M3 e a melhor escolha:**

- Agente de codigo que roda por horas autonomo: demonstracao oficial mostra o M3 rodando 12h sozinho, produzindo 18 commits, 23 figuras experimentais, e reproduzindo um paper vencedor do ICLR 2025
- Refatoracao de repositorios grandes: 1M de contexto com MSA, le o projeto inteiro de uma vez
- Codigo que envolve screenshot/imagem (front-end, UI testing): multimodal nativo desde o treino
- Automacao com ferramentas (MCP, function calling): 74.2% no MCP Atlas
- Custo-beneficio em codigo: performance proxima de Opus 4.8 por 5-10% do custo

**Onde o M3 nao e a melhor escolha:**
- Raciocinio hiper-complexo (SWE-Bench Pro 59% vs Opus 4.8 69.2%)
- Matematica avancada (DeepSeek V4 Pro lidera)
- Chat generico / conversacao — a propria comunidade do r/LocalLLaMA reporta: "MiniMax e muito bom em tool calling mas nao se segura bem em conversa geral"

**MiniMax M2.7 — tool calling e producao com custo baixo**

O M2.7 tem ~230B parametros (SMoE, ~10B ativos por token). Review do Thomas Wiegold (teste cego com 3 codebases TypeScript):

> "M2.7 entregou ~90% da qualidade do Claude Opus 4.6 por ~7% do custo total da tarefa."

Ambos encontraram todos os 6 bugs e 10 vulnerabilidades. O M2.7 ofereceu uma correcao Tecnicamente superior (matematica inteira para moeda em vez de float). Custo: M2.7 $0.27 vs Opus $3.67 na mesma tarefa.

**Cenarios ideais para o M2.7:**
- Automacao com function calling e MCP em producao
- Tarefas de codigo bem escopadas (bug em parte conhecida, testes, refatoracao pequena)
- Fallback para o M3 quando o custo do M3 nao compensar
- Estrategia "Claude planeja + MiniMax executa" — muito comum na comunidade

**Pontos de atencao no M2.7:**
- Verborragico: gera ~4x mais tokens de saida que a media (87M vs 20M). Testadores reportaram 16.000 tokens de "thinking" para prompts simples
- Velocidade: ~46 TPS no modo standard (lento em contextos longos)
- So texto: nao processa imagens nativamente

### A regra de ouro
Nao existe "melhor modelo". Existe o **modelo certo para a tarefa certa**.

Usar DeepSeek V4 Pro para responder "qual o horario de funcionamento" e como chamar um neurocirurgiao para cortar seu pao. Usar Phi-3 para analisar um contrato juridico de 50 paginas e como pedir para um estagiario de 17 anos fazer uma cirurgia cardiaca.

A especializacao via fine-tuning e o que permite essa divisao de trabalho — e o motivo pelo qual nao precisamos de um modelo "super inteligente" para tudo. Cada modelo e fine-tunado para brilhar no seu nicho.

---

## 11. Exemplo pratico: como os pesos e o treinamento funcionam com dados reais de modelos atuais

### Cenário: voce quer criar um assistente de codigo para sua empresa
Vamos pegar tudo que aprendemos e aplicar num caso real.

**Passo 1 — escolher o modelo base**

Voce precisa de um modelo que entenda codigo. Olhando a tabela de especializacao, o **GLM-5.2** e o melhor modelo open-source em benchmarks de codigo (SWE-bench, Terminal-Bench). Ele tem 1M de contexto e modo thinking.

Mas voce nao vai treinar um GLM-5.2 do zero — isso custaria milhoes de dolares. Voce vai pegar o modelo **pre-treinado** e fazer fine-tuning com os dados da sua empresa.

**Passo 2 — o que sao os pesos do GLM-5.2**

O GLM-5.2 tem aproximadamente 355 bilhoes de parametros (MoE). Isso significa 355 bilhoes de numeros como estes:

```plaintext
matriz_atencao_camada_1[0][0] = 0.8732
matriz_atencao_camada_1[0][1] = -0.4419
matriz_atencao_camada_1[0][2] = 1.2756
...
matriz_ffn_camada_17[4095][4095] = -0.0034

```
No inicio do treinamento, esses numeros sao aleatorios (ou proximos de zero). Depois de ler 15 trilhoes de tokens, eles convergem para valores que fazem o modelo entender linguagem e codigo.

**Passo 3 — fine-tuning com LoRA na pratica**

Em vez de ajustar todos os 355B pesos (que custaria uma fortuna), voce usa LoRA. O LoRA adiciona **adaptadores** — matrizes pequenas de uns 10-100 milhoes de pesos extras.

```python
# Exemplo conceitual do que acontece no fine-tuning com LoRA
# Os pesos originais congelam. So os adaptadores mudam.

# Antes do fine-tuning:
peso_original = 0.8732  # congelado, nao mexe

# Depois do LoRA:
peso_efetivo = peso_original + (adaptador_A * adaptador_B)
# adaptador_A e adaptador_B sao os "adesivos" treinados com seus dados
# Seus ~50 milhoes de novos pesos sao ajustados, nao os 355B originais

```
Resultado: voce gasta algumas horas de GPU em vez de semanas, e o modelo continua sabendo tudo que ja sabia — mas agora tambem entende o codigo especifico da sua empresa.

**Passo 4 — o dataset de treino**

Para o fine-tuning, voce cria milhares de exemplos no formato pergunta-resposta:

```plaintext
Pergunta: "Refatore esta funcao para seguir o padrao de naming da empresa: [codigo]"
Resposta: [codigo refatorado seguindo o padrao]

Pergunta: "Explique o que este componente React faz: [codigo]"
Resposta: "Este componente renderiza uma tabela de dados filtrada por..."

Pergunta: "Corrija o bug de performance neste SQL: [codigo]"
Resposta: "O problema e o SELECT * sem WHERE. Correcao: [codigo]"

```
Cada par pergunta-resposta gera um ciclo de ajuste:

1. O modelo tenta responder
2. A funcao de perda (cross-entropy) compara a resposta do modelo com a resposta correta
3. O erro volta pelos pesos (backpropagation)
4. Os adaptadores LoRA sao ajustados microscopicamente (learning rate = 0.0001)
5. Repete 10.000 vezes
Depois de algumas epocas, os adaptadores LoRA "aprendem" os padroes de codigo da sua empresa. Os pesos originais do GLM-5.2 continuam intactos — o que mudou foram so os adesivos.

### Como funciona a atualizacao de versoes (DeepSeek V2 -> V3 -> V4)
**A resposta direta: nao, nao e "adicionar dados novos em cima dos ja treinados".**

Essa e a duvida mais comum sobre LLMs. A maioria das pessoas imagina que atualizar um modelo e como atualizar um app — voce baixa um patch com os dados novos e pronto. Nao funciona assim.

Vamos pegar o DeepSeek como exemplo concreto:

#### DeepSeek V2 -> V3: um modelo NOVO do zero
| O que as pessoas pensam | O que realmente acontece |
| --- | --- |
| "Pegaram o V2 e adicionaram mais dados de treino" | Jogaram TODO o V2 no lixo e comecaram do zero |
| "Atualizaram os pesos do V2 com as novas info" | Inicializaram pesos ALEATORIOS e treinaram de novo |
| "O V3 sabe o que o V2 sabia + coisas novas" | O V3 nunca "viu" os pesos do V2. Ele aprendeu TUDO do zero |

O DeepSeek V2 tinha pesos que foram aprendidos durante o treinamento dele. Quando a equipe decidiu fazer o V3, eles:

1. **Descartaram** todos os pesos do V2 (bilhoes de numeros, pro lixo)
2. **Criaram um dataset novo** — mais livros, mais codigo, mais internet, dados mais recentes (ate o final de 2023, por exemplo)
3. **Inicializaram pesos aleatorios** do zero
4. **Treinaram do comeco** — o modelo V3 passou por meses de treinamento, viu trilhoes de tokens, e aprendeu TUDO novamente, incluindo o que o V2 ja sabia
**Por que jogar tudo fora e comecar de novo?**

Porque os pesos do V2 foram otimizados para os dados que o V2 viu. Se voce tentar "continuar treinando" o V2 com dados novos:

```python
# O que NINGUEM faz (e por que):
pesos_v2 = carregar("deepseek-v2.pth")
# Tenta "atualizar" adicionando dados novos:
for dado_novo in dataset_2024:
    treinar(pesos_v2, dado_novo)  # <-- PROBLEMA!

```
O problema e que os pesos do V2 ja estavam **estabilizados** para os dados antigos. Forcar dados novos neles faz com que:

- O modelo **aprenda o dado novo** mas comeca a **esquecer o dado velho** (catastrophic forgetting)
- Os pesos precisam se "reorganizar" para acomodar os novos padroes, e nessa reorganizacao perdem precisao no que ja sabiam
- Depois de algumas rodadas, o modelo fica num estado "nem la nem ca" — pior que o V2 nos topicos antigos e mediano nos novos
**E por isso que uma versao major (V2 -> V3 -> V4) sempre comeca do zero.** O custo e altissimo (dezenas de milhoes de dolares), mas e a unica forma de garantir que o modelo seja consistente.

#### A excecao: "continued pre-training" (que quase ninguem usa para versoes major)
Existe uma tecnica chamada **continued pre-training** onde voce PEGA o modelo pronto e continua treinando com dados novos de um dominio especifico. Mas:

- So funciona se o **dominio novo for pequeno e bem especifico** (ex: continuar treinando um modelo generico com 50GB de artigos medicos)
- Precisa de uma **taxa de aprendizado menor** e tecnicas especiais (learning rate decay, re-weighting) para nao esquecer o que ja sabia
- Mesmo assim, depois de algumas epocas, o modelo comeca a perder performance geral
A DeepSeek NAO usa isso para ir do V2 ao V3 ou do V3 ao V4. Eles treinam do zero.

#### E as versoes menores (V3 -> V3.1, V4 Flash -> V4 Pro)?
Essas sim sao "atualizacoes em cima". Mas nao no sentido de "adicionar dados novos ao treinamento original". No fine-tuning:

1. **O modelo base nao muda** — os pesos do V3 continuam congelados
2. **O que muda sao os pesos do fine-tuning** — uma etapa separada que acontece DEPOIS do pre-treinamento
3. O fine-tuning nao "adiciona conhecimento novo" no sentido de fatos do mundo. Ele **ensina o modelo a se comportar** — seguir instrucoes, responder em formato especifico, raciocinar passo a passo
Pense na diferenca:

| Tipo de atualizacao | O que ensina | Exemplo |
| --- | --- | --- |
| Pre-treinamento (do zero) | Fatos do mundo: quem ganhou a copa de 2022, como funciona um for loop, o que e DNA | DeepSeek V2 -> V3 |
| Fine-tuning | Comportamento: como responder, formato, tom, quando dizer "nao sei" | V3 -> V3.1, V4 Flash -> V4 Pro |
| RAG (busca externa) | Informacao factual recente sem mexer nos pesos | Pesquisar no Google/docs antes de responder |

O RAG (Retrieval-Augmented Generation) e a forma MAIS COMUM de "atualizar" o conhecimento de um LLM sem retreinar: em vez de enfiar os dados novos nos pesos, voce **busca num banco externo** e coloca no contexto da pergunta. E o que eu fiz hoje: em vez de ter os modelos da Z.AI e MiniMax "na minha cabeca", fui buscar nos sites oficiais e coloquei no contexto.

#### Resumindo com o DeepSeek
| Versao | Treinado do zero? | O que mudou |
| --- | --- | --- |
| V2 | Sim (aleatorio) | Primeiro modelo MoE da DeepSeek |
| V2.5 | Nao (fine-tuning do V2) | Aprendeu a seguir instrucoes melhor |
| V3 | SIM (aleatorio, V2 descartado) | Nova arquitetura, mais dados, qualidade muito superior |
| V3.1 | Nao (fine-tuning do V3) | Ajustes de seguranca e performance |
| V4 Flash | SIM (aleatorio, V3 descartado) | Modelo novo otimizado para velocidade |
| V4 Pro | Nao (fine-tuning do V4 base) | Mesmo modelo base do Flash, mas especializado em raciocinio |

**Nenhuma versao "adiciona dados novos em cima" da anterior.** Cada versao major descarta os pesos e comeca do zero. E so assim que se garante que o modelo novo e realmente superior — porque ele foi otimizado desde o primeiro token para o dataset completo e a nova arquitetura.

### E como voce, dev, pode atualizar seu conhecimento sobre modelos?
Minha data de corte fixa e uma limitacao. As formas de manter a tabela atualizada:

1. **Consultar as docs oficias** — como fizemos hoje com docs.z.ai e platform.minimax.io
2. **Criar um script periodico** que baixa as info dos provedores que voce usa e salva num arquivo local
3. **Pedir pra mim buscar** — "pesquise os modelos mais recentes da DeepSeek" e eu busco na web
4. **Skills curators** — alguem (voce ou uma automacao) mantem um arquivo de referencia curada

---

## Referencias
- [Understand LLM sizes - web.dev](https://web.dev/articles/llm-sizes)
- [LLM Model Size: Comparison Chart - Label Your Data](https://labelyourdata.com/articles/llm-fine-tuning/llm-model-size)
- [Phi-3 Technical Report - arXiv](https://arxiv.org/html/2404.14219v4)
- [LLM Size and Performance - Codingscape](https://codingscape.com/blog/most-powerful-llms-large-language-models)