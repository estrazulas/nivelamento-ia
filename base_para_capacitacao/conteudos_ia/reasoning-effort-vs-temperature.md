# Aula: Reasoning Effort vs Temperature
Entender a diferenca entre essas duas configuracoes e essencial para extrair o maximo de um LLM sem desperdicar tokens nem qualidade.

---

## 1. O Básico - Duas Camadas Diferentes

```plaintext
PROMPT (sua pergunta)
       |
       v
  [RASCUNHO INTERNO]  <-- reasoning_effort controla AQUI
  O modelo pensa, raciocina,
  explora caminhos, se corrige
       |
       v
  [ESCRITA DA RESPOSTA]  <-- temperature controla AQUI
  O modelo escreve a versao final
       |
       v
RESPOSTA (o que voce ve)

```
**Eixo X (effort) = profundidade do pensamento**

**Eixo Y (temperature) = estilo da escrita**

Sao independentes. Voce pode ter qualquer combinacao dos dois.

---

## 2. Reasoning Effort (profundidade)
Controla **quanto o modelo "pensa antes de falar"**. E como se ele tivesse uma area de rascunho onde escreve seu raciocinio interno antes de te entregar a resposta final.

### Níveis principais:
| Nivel | O que muda | Quando usar |
| --- | --- | --- |
| low | Rascunho minimo. Responde quase instantaneamente com o primeiro palpite. | Perguntas simples, acoes diretas, comandos de ferramenta. |
| medium | Rascunho moderado. Faz uma cadeia de raciocinio basica, verifica a logica uma vez. | Uso geral, dia a dia. Equilibrio entre velocidade e qualidade. |
| high | Rascunho profundo. Explora caminhos alternativos, verifica contradicoes, corrige erros antes de responder. | Problemas complexos, matematica, debugging, codigo multi-etapas. |

### Exemplo pratico com cada nivel:
**Cenário A: O Detetive com Reasoning BAIXO (Por Instinto)**

O detetive com **Reasoning Baixo** é aquele policial de filme de ação que quer resolver tudo em dois minutos para ir almoçar. Ele não gasta tempo analisando os detalhes escondidos.

- **Como ele age:** Ele lê as pistas e, instantaneamente, puxa da memória o palpite mais óbvio e comum que ele já viu em outras histórias.
- **A Resposta dele:** *"Com certeza foi o mordomo! Ele tinha a chave da cópia, entrou, pegou o vaso e saiu. O cabelo loiro é da esposa do dono da casa para despistar."*
- **O Problema:** Ele ignorou o fato de a sala estar trancada *por dentro* e a grade da janela. Ele deu uma resposta rápida, que parece fazer sentido à primeira vista, mas que tem furos na lógica se você pensar um pouco mais.

> **Quando o Reasoning Baixo é bom?** Para tarefas que não exigem investigação profunda. Se você pedir para ele *"Escreva um e-mail cobrando um cliente"*, ele não precisa investigar nada, ele só puxa o modelo padrão da memória e te entrega o texto na hora.

---
**Cenário B: O Detetive com Reasoning ALTO (Investigação Passo a Passo)**

O detetive com **Reasoning Alto** é o Sherlock Holmes. Quando você dá as pistas, ele não responde na hora. Ele acende o cachimbo, senta na cadeira e começa a falar sozinho, eliminando hipóteses na frente de uma lousa.

- **Como ele age (Os bastidores da IA):** Antes de te dar o veredito, ele cria uma linha de raciocínio interna:
  1. *"Se a porta estava trancada por dentro, ninguém entrou pela porta."*
  2. *"Se a janela tem grade, um humano não passa por ela."*
  3. *"Mas a janela estava aberta... algo menor que as grades passou por ali."*
  4. *"O fio de cabelo loiro não é humano, pode ser pelo de um animal... um macaco treinado?"*
- **A Resposta dele (Após alguns segundos pensando):** *"O culpado não foi um humano. O dono do circo local tem um sagui de pelos loiros. O animal passou pelas grades da janela aberta, pegou o vaso e voltou para o tutor, explicando por que a porta continuou trancada por dentro e o chão sem pegadas humanas."*

> **Quando o Reasoning Alto é bom?** Para problemas onde um erro bobo arruína tudo. Se você pedir para ele resolver um problema de física, programar um sistema de segurança ou desvendar um enigma, ele precisa desse tempo para checar se a própria lógica dele faz sentido.

---
**Resumo Visual no mesmo Mistério**

- **Reasoning Baixo:** Olha para o mistério \(\rightarrow \) cospe a primeira resposta padrão que vem à cabeça (Rápido, mas pode ser superficial ou errado).
- **Reasoning Alto:** Olha para o mistério \(\rightarrow \) monta um quebra-cabeça na mente \(\rightarrow \) testa se as peças se encaixam \(\rightarrow \) te entrega a solução refinada (Demorado, mas logicamente impecável).

---

## 3. Temperature (estilo)
Controla **como o modelo escreve a resposta final** depois que o raciocinio ja foi feito. Afeta criatividade, variacao, "personalidade" do texto.

### Níveis principais:
| Nivel | Efeito | Quando usar |
| --- | --- | --- |
| 0.0 - 0.3 (baixa) | Respostas deterministicas, consistentes, repetiveis. Mesmo prompt = mesma resposta. | Codigo, comandos, fatos, respostas tecnicas. |
| 0.4 - 0.6 (media) | Equilibrio entre precisao e naturalidade. Variacao leve. | Chat geral, explicacoes, uso diario. |
| 0.7 - 1.0 (alta) | Criativo, variado, imprevisivel. Mesmo prompt pode dar respostas bem diferentes. | Brainstorming, textos criativos, humor, historias. |

### Exemplo pratico com temperaturas diferentes:
**Pergunta:** "2+2"

Rascunho interno (medium effort): "2+2 = 4"

**Temperature 0.1:**

> 4

Seco, direto, certo. Zero enfeite.

**Temperature 0.9:**

> 2 + 2 e igual a 4! Sabia que essa e uma das primeiras contas que aprendemos na escolinha? Curiosidade: em binario, 2+2 nao existe, seria 10+10 = 100. Mas em decimal classico, resposta e 4 mesmo! :)

Mais "personalidade", mas abre espaco pra firula desnecessaria.

---
**Pergunta:** "Tem 3 galinhas e 2 cachorros. Quantas patas?"

Rascunho interno (medium effort): "3x2=6, 2x4=8, total 14"

**Temperature 0.1:**

> 14 patas.

**Temperature 0.9:**

> Vamos la! 3 galinhas com 2 patinhas cada = 6 patinhas. 2 cachorros com 4 patas cada = 8 patas. Somando tudo: 6 + 8 = 14 patas no total! Ou, se preferir, 7 pares de patas :)

---

## 4. Tabela Comparativa Final
| Caracteristica | Reasoning Effort | Temperature |
| --- | --- | --- |
| O que controla | Profundidade do pensamento interno | Estilo da escrita final |
| Analogia | Quanto tempo voce reflete antes de falar | O tom que voce usa ao falar |
| Impacto em custo | Gasta MAIS tokens internos (rascunho) | Gasta praticamente os mesmos tokens |
| Impacto em velocidade | High = mais lento | Quase nenhum |
| Afeta qualidade? | Sim - pode evitar erros de raciocinio | Nao - o raciocinio ja foi feito |
| Afeta consistencia? | High tende a ser mais consistente (verifica mais) | Baixa = muito consistente. Alta = variado. |
| Bom para codigo? | High ajuda em logica complexa | Baixa (0.0-0.2) para codigo |

---

## 5. Combinacoes comuns no dia a dia
| Uso | Effort | Temperature | Efeito |
| --- | --- | --- | --- |
| Chat rapido, comandos | low | 0.5 | Rapido e natural |
| Uso geral, explicacoes | medium | 0.5-0.7 | Equilibrio, som do Hermes |
| Codigo, debugging | medium-high | 0.0-0.2 | Pensamento profundo + respostas deterministicas |
| Brainstorm criativo | low-medium | 0.8-1.0 | Pensamento leve + escrita criativa |
| Matematica complexa | high | 0.0 | Maxima verificacao, zero criatividade |

---

## Resumão
**reasoning_effort = quanto o modelo pensa (profundidade)**

**temperature = como o modelo escreve (estilo)**

Um nao substitui o outro. Sao dialetos independentes que controlam aspectos diferentes da geracao. Voce pode (e deve) ajustar os dois separadamente dependendo da tarefa.