# Capacitacao IA para Devs

Workshop de IA para desenvolvimento de software, 16 horas, 2 dias, 7 modulos.

## plano_topicos

| Arquivo / Pasta | Resumo |
| --- | --- |
| [workshop-ia-para-devs.md](plano_topicos/workshop-ia-para-devs.md) | Conteudo programatico completo do workshop, modulos 1 a 7, com topicos, laboratorios e glossario com 109 termos. |
| [roteiro-apresentacao.md](plano_topicos/roteiro-apresentacao.md) | Roteiro linha a linha do instrutor com falas, analogias e transicoes entre slides. |
| [links.md](plano_topicos/links.md) | Todos os links do projeto organizados por modulo (clicaveis nos slides e referencias externas). |
| modelo_apresentacao.md | Especificacao visual dos slides: grid, dimensoes, cores, tipografia e checklist de exportacao. |
| labs/ | Estrutura dos 7 laboratorios praticos, um por modulo, com materiais recomendados para preparacao. |
| roteiro-revisao-juiz.md | Relatorio de revisao com 83 intervencoes de 3 perfis de alunos e parecer do juiz. |

## excalidraw

| Arquivo | Resumo |
| --- | --- |
| modulo-01-llms-fundamentos.excalidraw | Fundamentos, tokens, janela de contexto, limitacoes, pre-treinamento vs fine-tuning vs RAG. |
| modulo-02-open-source.excalidraw | Modelos locais com Ollama, comparacao nuvem vs local, SLMs, matriz de decisao. |
| modulo-03-prompt-engineering.excalidraw | 5 elementos do prompt, frameworks RTF/CARE/RISE, tecnicas zero-shot, few-shot, chain of thought. |
| modulo-04-rag-embeddings.excalidraw | Pipeline RAG, embeddings, chunking, buscas semantica e hibrida, PCA, graph RAG. |
| modulo-05-mcp-agentes.excalidraw | MCP, agentes, ferramentas, seguranca, sub-agentes e skills. |
| modulo-06-arquitetura-contexto.excalidraw | Arquitetura de contexto, STATE.md, evolucao de prompts ate skills, loope de agente. |
| modulo-07-sdd-ferramentas.excalidraw | SDD, spec.md, design.md, tasks.md, ferramentas e avaliacao LLM-as-Judge. |

## scripts

| Arquivo | Resumo |
| --- | --- |
| gerar_slide.py | Helpers Python (Slide, save, add_card) para gerar apresentacoes Excalidraw programaticamente. |
| COMO_USAR.md | Documentacao da API com grid de slides, cores do tema e exemplos de uso. |

## CLAUDE.md

| Instrucao | Resumo |
| --- | --- |
| Criacao de slides | Leia modelo_apresentacao.md antes de criar slides. Use script gerar_slide.py ou MCP Excalidraw. Exporte para .excalidraw imediatamente apos criar. |
| Formato .excalidraw | Todos os campos sao obrigatorios nos elementos (angle, opacity, roundness, boundElements, groupIds, frameId, isDeleted, locked, seed, versionNonce, updated). Dimensoes de texto precisam ser calculadas. |
| Validacao | Verifique se textos cabem nos containers e se nao ha overlap entre elementos consecutivos. Valide abrindo em excalidraw.com. |
| Efeito cascata | Ao redimensionar um container, valide a cadeia inteira: texto cabe no card, card cabe na secao, secao cabe no slide, labels e navegacao nao foram soterrados. |
| appState minimo | viewBackgroundColor, gridSize, scrollX, scrollY, zoom, activeTool. |
