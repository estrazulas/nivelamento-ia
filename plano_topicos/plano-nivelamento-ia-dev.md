# Plano de Nivelamento: IA para Desenvolvimento de Software
**3 vídeos · ~1h30 total · Do básico ao avançado**

---

## Visão Geral
Este plano organiza o aprendizado em 3 níveis progressivos, combinando 3 vídeos:

**Nota sobre os autores:**
- Fabrício Veronez é muito bom na didática dos conceitos básicos, mas fala bastante sobre DevOps e infra. Os conceitos se aplicam também a desenvolvimento de software.
- Waldemar Neto (TLC) tem o foco em desenvolvimento, mas não é tão didático nos conceitos mais básicos. O material dele entra na parte de SDD com aplicação real.
- Ambos têm produtos, cursos, workshops e pós-graduação — essa parte pode ser pulada.

A recomendação é assistir os 3 vídeos antes de entrar em workshops ou cursos aplicados de IA, para não ficar perdido nos conceitos básicos e nas sopas de letrinhas que vão surgir. Abaixo estão todos os pontos identificados nos vídeos com os links diretos para os trechos.

| # | Vídeo | Canal | Duração | Foco |
| --- | --- | --- | --- | --- |
| 1 | [Roadmap de IA para DevOps](https://youtu.be/03-nB_KMm44) | Fabrício Veronez | 20 min | Fundamentos teóricos |
| 2 | [Prompt Engineering - Guia Prático](https://youtu.be/Qf_QHxuc8J8) | Fabrício Veronez | 2h | Prompt Engineering |
| 3 | [SDD: Habilidade #1 para Devs](https://youtu.be/YFDp-smGYqQ) | Waldemar Neto | 12 min | SDD teoria + prática |

---

## Ordem Recomendada

```plaintext
Nível 1 (Modelos + Contexto) → Nível 2 (Prompt Eng) → Nível 3 (SDD)

```

---

## Tópicos abordados
- **Nível 1** — aquecimento (6 min): Modelos e Contexto, a base antes de tudo
- **Nível 2** — a maior parte dos conceitos (1h10): Prompt Engineering, o que mais entrega resultado imediato
- **Nível 3** — SDD completo (12 min): teoria e prática na mesma sentada

---

## Nível 1 — Modelos e Contexto: A Base
**~6 minutos**

**Vídeo 1 — [Roadmap de IA para DevOps](https://youtu.be/03-nB_KMm44)**

Antes de prompt engineering ou SDD, dois fundamentos que fazem toda diferença: entender os modelos que você está usando e aprender a fornecer contexto de qualidade.

### Modelos (LLMs)

| Tópico | Timestamp | Link |
| --- | --- | --- |
| O que são LLMs (GPT, Claude, Gemini, DeepSeek, Llama) | 3:51 | [link](https://youtu.be/03-nB_KMm44?t=231) |
| Parâmetros: o que são e por que mais = maior capacidade | 4:16 | [link](https://youtu.be/03-nB_KMm44?t=256) |
| Como funciona: input → processamento → output | 4:43 | [link](https://youtu.be/03-nB_KMm44?t=283) |
| Trade-off: qualidade, especialização e custo | 5:06 | [link](https://youtu.be/03-nB_KMm44?t=306) |
| SLMs: modelos menores e especializados | 5:55 | [link](https://youtu.be/03-nB_KMm44?t=355) |

### Contexto

| Tópico | Timestamp | Link |
| --- | --- | --- |
| O que é contexto e por que ele é o maior diferencial | 10:10 | [link](https://youtu.be/03-nB_KMm44?t=610) |
| Como fornecer contexto: direto no prompt ou via agentes | 11:18 | [link](https://youtu.be/03-nB_KMm44?t=678) |
| Context Engineering: a disciplina de coletar e inserir contexto | 11:42 | [link](https://youtu.be/03-nB_KMm44?t=702) |

---

## Nível 2 — Prompt Engineering: Como Conversar com IA
**~1h10**

**Vídeo 2 — [Prompt Engineering - Guia Prático](https://www.youtube.com/live/Qf_QHxuc8J8?t=1167)**

O Fabrício explica o que é engenharia de prompt: a área que estuda como você interage com a IA, como criar inputs e como escolher a técnica certa pra cada tarefa. Essa é a seção mais longa do plano porque prompt engineering é a habilidade que mais impacta resultado no dia a dia.

### Os 5 Elementos de um Prompt

| Elemento | Timestamp | Link |
| --- | --- | --- |
| O que é engenharia de prompt e por que importa | 19:27 | [link](https://www.youtube.com/live/Qf_QHxuc8J8?t=1167) |
| Os 5 elementos de um prompt eficiente | 21:28 | [link](https://www.youtube.com/live/Qf_QHxuc8J8?t=1288) |
| Elemento 1: Role (direcionamento, persona) | 23:20 | [link](https://www.youtube.com/live/Qf_QHxuc8J8?t=1400) |
| Elemento 2: Contexto | 28:06 | [link](https://www.youtube.com/live/Qf_QHxuc8J8?t=1686) |
| Elemento 3: Instrução (a tarefa em si) | 31:48 | [link](https://www.youtube.com/live/Qf_QHxuc8J8?t=1908) |
| Elemento 4: Restrições | 34:37 | [link](https://www.youtube.com/live/Qf_QHxuc8J8?t=2077) |
| Elemento 5: Formato de saída (output) | 39:09 | [link](https://www.youtube.com/live/Qf_QHxuc8J8?t=2349) |
| Exemplo real juntando os 5 elementos | 43:25 | [link](https://www.youtube.com/live/Qf_QHxuc8J8?t=2605) |

### Frameworks de Prompt

Nem toda tarefa precisa dos 5 elementos. O Fabrício mostra frameworks mais enxutos pra cenários específicos:

| Framework | Quando usar | Timestamp | Link |
| --- | --- | --- | --- |
| RTF (Role, Task, Format) | Tarefas simples, padrão conhecido (Dockerfile, JSON) | 47:01 | [link](https://www.youtube.com/live/Qf_QHxuc8J8?t=2821) |
| CARE (Context, Action, Result, Example) | Tarefas com objetivo de negócio, migrações, runbooks | 52:40 | [link](https://www.youtube.com/live/Qf_QHxuc8J8?t=3160) |
| RISE (Role, Input, Steps, Example) | Tarefas com múltiplos passos, chain of thought | 55:10 | [link](https://www.youtube.com/live/Qf_QHxuc8J8?t=3310) |
| Demo RTF gerando Dockerfile | | 58:00 | [link](https://www.youtube.com/live/Qf_QHxuc8J8?t=3480) |
| Demo CARE gerando runbook de incidente | | 60:35 | [link](https://www.youtube.com/live/Qf_QHxuc8J8?t=3635) |

### Técnicas de Prompt

Frameworks estruturam o prompt. Técnicas definem como o modelo vai pensar:

| Técnica | O que é | Timestamp | Link |
| --- | --- | --- | --- |
| Zero-shot | Instrução direta, sem exemplo. Use pra tarefas comuns. | 70:34 | [link](https://www.youtube.com/live/Qf_QHxuc8J8?t=4234) |
| Few-shot / One-shot | Você dá 1 ou mais exemplos de resposta. Use pra formato específico da sua empresa. | 75:49 | [link](https://www.youtube.com/live/Qf_QHxuc8J8?t=4549) |
| Chain of Thought | Força o modelo a raciocinar passo a passo. Use pra análise, troubleshooting, decisões. | 85:16 | [link](https://www.youtube.com/live/Qf_QHxuc8J8?t=5116) |

---

## Nível 3 — SDD na Prática: Teoria e Mão no Código
**12 minutos**

**Vídeo 3 — [Waldemar Neto: SDD para devs](https://youtu.be/YFDp-smGYqQ)**

O Waldemar explica o SDD completo em 12 minutos, usando um projeto real (sistema de streaming com recomendação). Ele mostra por que prompt direto falha em projetos grandes e como as 4 fases resolvem: especificar, desenhar arquitetura, quebrar em tasks e executar com subagents em paralelo.

| Trecho | Timestamp | Link |
| --- | --- | --- |
| O problema: PRD gigante, prompt direto = plano raso, perde contexto | 0:32 | [link](https://youtu.be/YFDp-smGYqQ?t=32) |
| Por que spec driven resolve: breakdown de tasks, ordem, paralelização | 1:49 | [link](https://youtu.be/YFDp-smGYqQ?t=109) |
| Context Engineering: janela de contexto limitada, risco de alucinação | 2:08 | [link](https://youtu.be/YFDp-smGYqQ?t=128) |
| RPI: Research (abre leque, pesquisa) → Plan (salva em markdown) → Implement (tasks) | 3:12 | [link](https://youtu.be/YFDp-smGYqQ?t=192) |
| A skill TLC Spec-Driven e as 4 fases | 5:28 | [link](https://youtu.be/YFDp-smGYqQ?t=328) |
| Fase 1: Specify — problema, metas, user stories, fora de escopo | 5:50 | [link](https://youtu.be/YFDp-smGYqQ?t=350) |
| Fase 2: Design — diagramas, arquitetura, decisões (opcional, projetos grandes) | 6:37 | [link](https://youtu.be/YFDp-smGYqQ?t=397) |
| Fase 3: Tasks — breakdown, sequencial vs paralelo, cada task é autossuficiente | 7:21 | [link](https://youtu.be/YFDp-smGYqQ?t=441) |
| O que uma task precisa: o que fazer, onde, pré-requisitos, definition of done | 8:01 | [link](https://youtu.be/YFDp-smGYqQ?t=481) |
| Fase 4: Execute — subagents rodando tasks em paralelo, cada um com contexto limpo | 8:55 | [link](https://youtu.be/YFDp-smGYqQ?t=535) |
| STATE.md: memória entre sessões, guarda decisões do agente, permite continuar depois | 9:54 | [link](https://youtu.be/YFDp-smGYqQ?t=594) |
| Demo real: PRD → spec → design → tasks → 4 subagents em paralelo | 10:40 | [link](https://youtu.be/YFDp-smGYqQ?t=640) |
| Como instalar a skill e flexibilidade: design opcional pra projetos pequenos | 11:44 | [link](https://youtu.be/YFDp-smGYqQ?t=704) |
