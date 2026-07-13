# Scripts de Geração das Apresentações Excalidraw

## ⚠️ Mudança: agora temos um helper reutilizável

Os scripts `gerar_modulo_01.py` a `gerar_modulo_07.py` foram **removidos**
— não estavam sincronizados com os slides (que foram editados manualmente via MCP).

Em vez deles, use o `gerar_slide.py`.

## Como usar

```bash
cd /home/estrazulas/git/docs_capacitacao_ia
python3 -c "
from scripts.gerar_slide import Slide, save, CORES
# crie seus slides aqui...
"
```

Ou crie um script que importa `gerar_slide` e chama `save()`.

## Documentação

- `gerar_slide.py` — helpers: `Slide`, `save()`, `CORES`
- `COMO_USAR.md` — guia rápido com exemplos e grid de slides

## Template visual de referência

- Cores, fontes, dimensões e padrões: `excalidraw/modelo_apresentacao.md`
