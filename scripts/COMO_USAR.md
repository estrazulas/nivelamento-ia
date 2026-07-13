# Como Usar o `gerar_slide.py`

Script com helpers para gerar arquivos `.excalidraw` programaticamente, sem editar JSON manualmente.

## Rápido

```python
from gerar_slide import Slide, save, CORES

slide = Slide(x=20, y=20, titulo="Meu Slide", modulo="M1", slide_num="1")
slide.add_card(40, 100, 880, 200, CORES["info_bg"], CORES["info_borda"],
               titulo="💡 Título", body="Texto do card")
save([slide], "meu-modulo.excalidraw")
```

## Grid de Slides

```
   x=20         x=1100
┌──────────┐ ┌──────────┐  ← y += 700
│ SLIDE 1  │ │ SLIDE 2  │
│ (ímpar)  │ │ (par)    │
└──────────┘ └──────────┘
┌──────────┐ ┌──────────┐  ← y += 700
│ SLIDE 3  │ │ SLIDE 4  │
└──────────┘ └──────────┘
```

- **Cada slide**: 960×660 px
- **Slide ímpar** (esquerda): x=20
- **Slide par** (direita): x=1100
- **Próxima linha**: y += 700

## API

### `Slide(x, y, w=960, h=660, titulo="", subtitulo="", slide_num="", modulo="")`
Cria slide no grid.

| Método | Descrição |
|--------|----------|
| `add_card(x, y, w, h, bg, stroke, titulo="", body="")` | Card com título e corpo. Coordenadas relativas ao slide. |
| `add_text(x, y, content, fs=17, color=None)` | Texto livre |
| `add_arrow(x, y, w, h, color=None)` | Seta de navegação |
| `add_nav(txt, x=None, y=None)` | Dica de navegação (ex: "↓ arraste para baixo") |
| `add_section_footer(txt, y=None)` | Faixa colorida no rodapé |

### `save(slides, filepath)`
Gera o arquivo `.excalidraw` a partir da lista de slides.

## Cores disponíveis

| Nome | Uso | BG | Borda |
|------|-----|-----|-------|
| `slide_bg` | Fundo do slide | `#f8f9fa` | `#dee2e6` |
| `negativo_bg/borda` | Lado ruim | `#fff5f5` | `#ffc9c9` |
| `positivo_bg/borda` | Lado bom | `#f0fff4` | `#b2f2bb` |
| `info_bg/borda` | Informativo | `#e7f5ff` | `#4c6ef5` |
| `alerta_bg/borda` | Intermediário | `#fff4e6` | `#fd7e14` |
| `destaque_bg/borda` | Destaque | `#f3f0ff` | `#7950f2` |
| `card_bg/borda` | Card neutro | `#ffffff` | `#adb5bd` |
| `texto` | Texto principal | — | `#1e1e1e` |
| `texto_sec` | Texto secundário | — | `#868e96` |

## Tipografia

| Elemento | fontSize |
|----------|----------|
| Título do slide | 28 |
| Subtítulo | 14 |
| Título de card | 18 |
| Corpo de card | 17 |
| Label "SLIDE N" | 12 |
| Dica de navegação | 13 |

## Exemplo completo

Veja o bloco `if __name__ == "__main__"` no próprio `gerar_slide.py`.
Execute com `python3 scripts/gerar_slide.py` para gerar `exemplo-slides.excalidraw`.

## Validação

Sempre validar o `.excalidraw` antes de entregar:

```python
import json
with open("arquivo.excalidraw") as f:
    data = json.load(f)
for el in data["elements"]:
    if el["type"] == "text":
        # Verificar se texto cabe no container
        pass
```

Ou simplesmente abrir em [excalidraw.com](https://excalidraw.com).
