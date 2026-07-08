# Scripts de Geração das Apresentações Excalidraw

## Pré-requisito

Python 3.6+ (só usa `json` e `uuid` da stdlib).

## Gerar uma apresentação

```bash
cd /home/estrazulas/git/docs_capacitacao_ia
python3 scripts/gerar_modulo_0X.py
```

Substitua `X` por 1 a 7 conforme o módulo desejado.

## Gerar todas de uma vez

```bash
cd /home/estrazulas/git/docs_capacitacao_ia
for script in scripts/gerar_modulo_0*.py; do python3 "$script"; done
```

## Arquivos gerados

| Script | Saída |
|--------|-------|
| `gerar_modulo_01.py` | `excalidraw/modulo-01-llms-fundamentos.excalidraw` |
| `gerar_modulo_02.py` | `excalidraw/modulo-02-open-source.excalidraw` |
| `gerar_modulo_03.py` | `excalidraw/modulo-03-prompt-engineering.excalidraw` |
| `gerar_modulo_04.py` | `excalidraw/modulo-04-rag-embeddings.excalidraw` |
| `gerar_modulo_05.py` | `excalidraw/modulo-05-mcp-agentes.excalidraw` |
| `gerar_modulo_06.py` | `excalidraw/modulo-06-arquitetura-contexto.excalidraw` |
| `gerar_modulo_07.py` | `excalidraw/modulo-07-sdd-ferramentas.excalidraw` |

## Como ajustar o conteúdo

1. Edite o script do módulo (`scripts/gerar_modulo_0X.py`)
2. Rode `python3 scripts/gerar_modulo_0X.py`
3. Abra o `.excalidraw` em [excalidraw.com](https://excalidraw.com) para verificar

### O que editar

- **Textos**: procure as chamadas `text(x, y, "conteúdo", fontSize, cor)` e altere a string
- **Cores**: hex codes nos parâmetros `bg`, `color`, `stroke`
- **Posições**: `x` e `y` nos elementos. Use as variáveis `R1=20`, `R2=740`, `R3=1480` como base
- **Altura do slide**: altere `H1`, `H2`, `H3` no topo do script
- **Adicionar slide novo**: duplique um bloco de slide existente, ajuste coordenadas e rótulo

### Cuidados ao editar

- **SEMPRE** use `R1 + offset`, `R2 + offset` ou `R3 + offset` para coordenadas `y` dentro de slides. Nunca use valores absolutos como `y=120` — isso causa sobreposição entre slides de linhas diferentes.
- Se aumentar a altura de um slide (`H1`, `H2`, `H3`), recalcule os offsets das linhas seguintes para manter pelo menos 80px de gap.
- Após editar, verifique no excalidraw.com se não há textos vazando dos containers.

## Estrutura de cada script

```
Row offsets (R1, R2, R3)      → posição y de cada linha de slides
Funções helper                 → rect(), text(), arrow(), slide_bg(), slide_label(), nav_text()
Lista elements                 → acumula todos os elementos
Blocos por slide               → slide_bg + título + conteúdo + label + navegação
Montagem do JSON               → type, version, elements, appState, files
Escrita do arquivo             → json.dump no diretório excalidraw/
```

## Template visual de referência

- Cores, fontes, dimensões e padrões: `excalidraw/modelo_apresentacao.md`
- Exemplo completo com 6 slides: `excalidraw/prompts-engenharia.excalidraw`
