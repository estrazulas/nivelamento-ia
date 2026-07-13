#!/usr/bin/env python3
"""
Helpers para gerar slides .excalidraw programaticamente.

Uso:
    from gerar_slide import Slide, save

    slide = Slide(960, 620)  # width, height
    slide.add_title("Meu Slide")
    slide.add_card(x=40, y=100, w=880, h=200, bg="#e7f5ff", stroke="#4c6ef5",
                   title="💡 Conceito", body="Texto do card")
    save([slide], "meu-modulo.excalidraw")
"""

import json, uuid

# ─── Cores do tema ──────────────────────────────────────────────

CORES = {
    "slide_bg":      "#f8f9fa",
    "slide_borda":   "#dee2e6",
    "texto":         "#1e1e1e",
    "texto_sec":     "#868e96",
    "negativo_bg":   "#fff5f5",
    "negativo_borda":"#ffc9c9",
    "positivo_bg":   "#f0fff4",
    "positivo_borda":"#b2f2bb",
    "info_bg":       "#e7f5ff",
    "info_borda":    "#4c6ef5",
    "alerta_bg":     "#fff4e6",
    "alerta_borda":  "#fd7e14",
    "destaque_bg":   "#f3f0ff",
    "destaque_borda":"#7950f2",
    "card_bg":       "#ffffff",
    "card_borda":    "#adb5bd",
}

# ─── Elementos básicos ──────────────────────────────────────────

def _mid():
    return "m" + uuid.uuid4().hex[:16]


def rect(x, y, w, h, bg, stroke="#adb5bd", sw=1):
    return {
        "id": _mid(), "type": "rectangle",
        "x": x, "y": y, "width": w, "height": h,
        "backgroundColor": bg, "strokeColor": stroke, "strokeWidth": sw,
        "angle": 0, "opacity": 100, "roughness": 0, "roundness": None,
        "boundElements": None, "groupIds": [], "frameId": None,
        "isDeleted": False, "locked": False, "seed": 1, "versionNonce": 1, "updated": 1,
        "fillStyle": "solid",
    }


def text(x, y, content, fs, color="#1e1e1e", w=None, h=None):
    lines = content.split("\n")
    max_line = max(len(l) for l in lines)
    if w is None:
        w = round(max(max_line * fs * 0.58, 60))
    if h is None:
        h = round(len(lines) * fs * 1.25)
    return {
        "id": _mid(), "type": "text",
        "x": x, "y": y, "width": w, "height": h,
        "text": content, "fontSize": fs, "strokeColor": color,
        "fontFamily": 2, "textAlign": "left", "verticalAlign": "top",
        "autoResize": True, "lineHeight": 1.25,
        "angle": 0, "opacity": 100, "roughness": 0, "roundness": None,
        "boundElements": None, "groupIds": [], "frameId": None,
        "isDeleted": False, "locked": False, "seed": 1, "versionNonce": 1, "updated": 1,
        "backgroundColor": "transparent", "fillStyle": "solid",
    }


def arrow(x, y, w, h, color="#adb5bd", sw=1):
    end = "arrow" if w != 0 or h != 0 else None
    return {
        "id": _mid(), "type": "arrow",
        "x": x, "y": y, "width": w, "height": h,
        "strokeColor": color, "strokeWidth": sw,
        "startArrowhead": "arrow", "endArrowhead": end,
        "startBinding": None, "endBinding": None, "lastCommittedPoint": None,
        "points": [[0, 0], [w, h]],
        "angle": 0, "opacity": 100, "roughness": 0, "roundness": None,
        "boundElements": None, "groupIds": [], "frameId": None,
        "isDeleted": False, "locked": False, "seed": 1, "versionNonce": 1, "updated": 1,
        "backgroundColor": "transparent", "fillStyle": "solid",
    }


# ─── Slide helper ───────────────────────────────────────────────

class Slide:
    """Um slide no grid (960×620 padrão, coluna esquerda x=20, direita x=1100)."""

    def __init__(self, x, y, w=960, h=660, titulo="", subtitulo="", slide_num="", modulo=""):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.elements = []

        # Fundo do slide
        self.elements.append(rect(x, y, w, h, CORES["slide_bg"], CORES["slide_borda"]))

        # Título
        if titulo:
            self.elements.append(text(x + 40, y + 20, titulo, 28))

        # Subtítulo
        if subtitulo:
            self.elements.append(text(x + 40, y + 58, subtitulo, 14, CORES["texto_sec"]))

        # Label
        if slide_num:
            label = f"{modulo} — SLIDE {slide_num}" if modulo else f"SLIDE {slide_num}"
            self.elements.append(text(x + (w - 160) // 2, y + h + 38, label, 12, CORES["texto_sec"]))

    def add_card(self, x, y, w, h, bg, stroke, titulo="", body="", titulo_fs=18, body_fs=17):
        """Adiciona um card retangular com título e corpo opcionais."""
        cx = self.x + x
        cy = self.y + y
        self.elements.append(rect(cx, cy, w, h, bg, stroke))
        if titulo:
            self.elements.append(text(cx + 24, cy + 14, titulo, titulo_fs))
        if body:
            self.elements.append(text(cx + 24, cy + 42, body, body_fs))
        return cx, cy, w, h

    def add_text(self, x, y, content, fs=17, color=None):
        """Adiciona texto livre."""
        self.elements.append(text(self.x + x, self.y + y, content, fs, color or CORES["texto"]))
        return self

    def add_arrow(self, x, y, w, h, color=None):
        """Adiciona seta de navegação."""
        self.elements.append(arrow(self.x + x, self.y + y, w, h, color or CORES["card_borda"]))
        return self

    def add_nav(self, txt, x=None, y=None):
        """Adiciona texto de navegação (seta + dica)."""
        if x is None:
            x = self.w // 2 - 80
        if y is None:
            y = self.h + 8
        self.elements.append(text(self.x + x, self.y + y, txt, 13, CORES["texto_sec"]))
        return self

    def add_section_footer(self, txt, y=None):
        """Faixa inferior verde/azul no fundo do slide."""
        if y is None:
            y = self.h - 70
        self.elements.append(rect(self.x + 20, self.y + y, self.w - 40, 50,
                                  CORES["positivo_bg"], CORES["positivo_borda"]))
        self.elements.append(text(self.x + 40, self.y + y + 10, txt, 14))
        return self


# ─── Export ──────────────────────────────────────────────────────

def save(slides, filepath, zoom=1):
    """Gera o arquivo .excalidraw a partir de uma lista de Slides."""
    elements = []
    for s in slides:
        elements.extend(s.elements)

    data = {
        "type": "excalidraw",
        "version": 2,
        "source": "gerar_slide.py",
        "elements": elements,
        "appState": {
            "viewBackgroundColor": "#ffffff",
            "gridSize": None,
            "scrollX": 0,
            "scrollY": 0,
            "zoom": {"value": zoom},
            "activeTool": {
                "type": "selection", "customType": None,
                "locked": False, "lastActiveTool": None,
            },
        },
    }
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ {filepath} salvo ({len(elements)} elementos)")


# ─── Exemplo de uso ────────────────────────────────────────────

if __name__ == "__main__":
    # Exemplo: 2 slides lado a lado na primeira linha
    s1 = Slide(x=20, y=20, titulo="Título Esquerdo", subtitulo="Subtítulo",
               modulo="EXEMPLO", slide_num="1")
    s1.add_card(40, 100, 880, 200, CORES["info_bg"], CORES["info_borda"],
                titulo="💡 Card Azul",
                body="Conteúdo do card explicando o conceito.\nSegunda linha de exemplo.")
    s1.add_nav("→ arraste para a direita")

    s2 = Slide(x=1100, y=20, titulo="Título Direito", subtitulo="Subtítulo",
               modulo="EXEMPLO", slide_num="2")
    s2.add_card(40, 100, 430, 200, CORES["negativo_bg"], CORES["negativo_borda"],
                titulo="❌ Exemplo Ruim",
                body="O que não fazer.")
    s2.add_card(470, 100, 430, 200, CORES["positivo_bg"], CORES["positivo_borda"],
                titulo="✅ Exemplo Bom",
                body="O que fazer em vez disso.")

    save([s1, s2], "exemplo-slides.excalidraw")
