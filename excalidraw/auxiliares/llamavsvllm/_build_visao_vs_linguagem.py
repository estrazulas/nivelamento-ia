#!/usr/bin/env python3
"""Build a side-by-side comparison: vision model vs language model file structures."""

import json, os

NOW = "2026-07-10T12:00:00.000Z"
FONT = 2

_seed = [400000]
_vn = [500000]

def _ns():
    _seed[0] += 1; return _seed[0]
def _nv():
    _vn[0] += 1; return _vn[0]

def _base(t, x, y):
    return {"type":t,"x":x,"y":y,"angle":0,"opacity":100,"roundness":None,
            "boundElements":None,"groupIds":[],"frameId":None,"isDeleted":False,
            "locked":False,"seed":_ns(),"versionNonce":_nv(),"updated":NOW,
            "createdAt":NOW,"version":1}

def rect(x, y, w, h, bg, sc="#1e1e1e", sw=1):
    el = _base("rectangle", x, y)
    el.update({"width":w,"height":h,"fillStyle":"solid","strokeWidth":sw,
               "strokeColor":sc,"backgroundColor":bg,"roughness":0})
    return el

def text(x, y, txt, fs=16, sc="#1e1e1e", ta="left"):
    lines = txt.split("\n")
    mc = max(len(l) for l in lines) if lines else 0
    w = mc * fs * 0.58 + 16
    h = len(lines) * fs * 1.35 + 8
    el = _base("text", x, y)
    el.update({"width":round(w),"height":round(h),"fontFamily":FONT,"fontSize":fs,
               "text":txt,"textAlign":ta,"verticalAlign":"top","autoResize":True,
               "lineHeight":1.25,"strokeColor":sc})
    return el

def ctext(rx, ry, rw, rh, txt, fs=16, sc="#1e1e1e"):
    lines = txt.split("\n")
    mc = max(len(l) for l in lines) if lines else 0
    tw = mc * fs * 0.58 + 16
    th = len(lines) * fs * 1.35 + 8
    return text(round(rx+(rw-tw)/2), round(ry+(rh-th)/2), txt, fs, sc,
                "center" if len(lines)==1 else "left")

def arrow(x, y, pts, sc="#333", sw=1):
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    el = _base("arrow", x, y)
    el.update({"width":max(max(xs)-min(xs),1),"height":max(max(ys)-min(ys),0),
               "points":pts,"startArrowhead":None,"endArrowhead":"arrow",
               "startBinding":None,"endBinding":None,"lastCommittedPoint":None,
               "strokeColor":sc,"backgroundColor":"transparent","fillStyle":"solid",
               "strokeWidth":sw,"roughness":0})
    return el

elements = []

L = 30
R = 640
COL_W = 590
H = 820

# ═══════════════════════════════════════════════════════════════════════════
# LEFT — Modelo de Visão (Classificador de Cachorros)
# ═══════════════════════════════════════════════════════════════════════════

elements.append(rect(L, 30, COL_W, H, "#f3e5f5", "#7b1fa2", 2))
elements.append(text(L+20, 42, "🐕 Modelo de Visão — Classificador de Raças", 20, "#4a148c"))

# Como nasceu
elements.append(text(L+20, 85, "Origem:", 15, "#4a148c"))
elements.append(text(L+20, 108, "ViT pré-treinado (ImageNet, 300M imagens)", 14, "#555"))
elements.append(arrow(L+290, 118, [[0,0],[0,22]], "#888"))
elements.append(text(L+20, 143, "Só números: reconhece bordas, texturas, formas genéricas", 13, "#888"))
elements.append(text(L+20, 168, "+ Fine-tuning com 20.580 fotos de 120 raças", 14, "#555"))
elements.append(arrow(L+290, 178, [[0,0],[0,22]], "#888"))
elements.append(text(L+20, 203, "Números ajustados para diferenciar Golden de Labrador", 13, "#888"))

# Arquivo
fx, fy, fw, fh = L+40, 240, 500, 380
elements.append(rect(fx, fy, fw, fh, "#fff", "#333", 1))
elements.append(text(fx+15, fy+6, "📄 dog-breed-classifier.bin (~340 MB)", 14, "#333"))
elements.append(text(fx+15, fy+30,
    "┌─────────────────────────────────────┐\n"
    "│ Cabeçalho:                          │\n"
    '│   type: "vision_transformer"        │\n'
    "│   base: google/vit-base-patch16-224 │\n"
    "│   classes: 71 raças                 │\n"
    "│   input: imagem 224×224 RGB         │\n"
    "│   output: 71 probabilidades         │\n"
    "├─────────────────────────────────────┤\n"
    "│                                     │\n"
    "│   -0.0034  0.0156 -0.0089  0.0214  │\n"
    "│    0.0182 -0.0067  0.0113 -0.0198  │\n"
    "│    0.0055 -0.0124 -0.0017  0.0160  │\n"
    "│    ...                              │\n"
    "│    (86 milhões de números)          │\n"
    "│                                     │\n"
    "│    ↓ o que cada número significa?   │\n"
    '│    "focinho alongado"  = +0.8423   │\n'
    '│    "pelo dourado"      = +0.7198   │\n'
    '│    "orelha caída"      = +0.6534   │\n'
    '│    "porte grande"      = -0.2311   │\n'
    '│    ...                             │\n'
    "└─────────────────────────────────────┘",
    11, "#333"))

# O que faz
elements.append(text(L+20, 645, "O que ele faz:", 15, "#4a148c"))
elements.append(text(L+20, 668, "Entrada: foto do seu cachorro (224×224 pixels)", 14, "#555"))
elements.append(text(L+20, 693, "Processo: multiplica pixels pelos 86M números", 14, "#555"))
elements.append(text(L+20, 718, "Saída: 71 números (probabilidade de cada raça)", 14, "#555"))
elements.append(text(L+20, 745, 'Ex: golden_retriever=94%  labrador=3%  poodle=0.1%', 13, "#2e7d32"))

# Resumo
elements.append(text(L+20, 790, "🔑 Só classifica cachorro. Não sabe o que é um gato, não entende texto.", 14, "#4a148c"))

# ═══════════════════════════════════════════════════════════════════════════
# RIGHT — Modelo de Linguagem (LLM)
# ═══════════════════════════════════════════════════════════════════════════

elements.append(rect(R, 30, COL_W, H, "#e8eaf6", "#283593", 2))
elements.append(text(R+20, 42, "🤖 Modelo de Linguagem — LLM (ex: Llama 8B)", 20, "#1a237e"))

# Como nasceu
elements.append(text(R+20, 85, "Origem:", 15, "#1a237e"))
elements.append(text(R+20, 108, "LLaMA pré-treinado (15 trilhões de tokens de texto)", 14, "#555"))
elements.append(arrow(R+360, 118, [[0,0],[0,22]], "#888"))
elements.append(text(R+20, 143, "Só números: completar frase, prever próxima palavra", 13, "#888"))
elements.append(text(R+20, 168, "+ Fine-tuning com instruções, código, RLHF", 14, "#555"))
elements.append(arrow(R+360, 178, [[0,0],[0,22]], "#888"))
elements.append(text(R+20, 203, "Números ajustados para seguir comandos e conversar", 13, "#888"))

# Arquivo
f2x, f2y, f2w, f2h = R+40, 240, 500, 380
elements.append(rect(f2x, f2y, f2w, f2h, "#fff", "#333", 1))
elements.append(text(f2x+15, f2y+6, "📄 llama-3.1-8b.gguf (~4.7 GB)", 14, "#333"))
elements.append(text(f2x+15, f2y+30,
    "┌─────────────────────────────────────┐\n"
    "│ Cabeçalho:                          │\n"
    '│   type: "llama"                     │\n'
    "│   layers: 32                        │\n"
    "│   dim: 4096                         │\n"
    "│   vocab: 128.256 tokens             │\n"
    "│   input: texto (sequência de tokens)│\n"
    "│   output: distribuição sobre tokens │\n"
    "├─────────────────────────────────────┤\n"
    "│                                     │\n"
    "│   -0.0034  0.0156 -0.0089  0.0214  │\n"
    "│    0.0182 -0.0067  0.0113 -0.0198  │\n"
    "│    0.0055 -0.0124 -0.0017  0.0160  │\n"
    "│    ...                              │\n"
    "│    (8 bilhões de números)           │\n"
    "│                                     │\n"
    "│    ↓ o que cada número significa?   │\n"
    '│    "rei - homem + mulher ≈ rainha"  │\n'
    '│    "Paris - França + Japão ≈ Tóquio"│\n'
    '│    "código Python usa indentação"   │\n'
    '│    "perto de SELECT vem FROM"       │\n'
    '│    ...                             │\n'
    "└─────────────────────────────────────┘",
    11, "#333"))

# O que faz
elements.append(text(R+20, 645, "O que ele faz:", 15, "#1a237e"))
elements.append(text(R+20, 668, 'Entrada: texto — "Explique SQL injection"', 14, "#555"))
elements.append(text(R+20, 693, "Processo: multiplica tokens pelos 8B números, token por token", 14, "#555"))
elements.append(text(R+20, 718, "Saída: sequência de tokens formando a resposta", 14, "#555"))
elements.append(text(R+20, 745, 'Ex: "SQL injection é um ataque onde o usuário malicioso insere..."', 13, "#1565c0"))

# Resumo
elements.append(text(R+20, 790, "🔑 Generalista. Sabe cachorro, gato, código, história, matemática, piada.", 14, "#1a237e"))

# ═══════════════════════════════════════════════════════════════════════════
# BOTTOM — COMPARAÇÃO
# ═══════════════════════════════════════════════════════════════════════════

sy = H + 50
elements.append(rect(L, sy+20, 1200, 90, "#fff9c4", "#f9a825", 2))
elements.append(text(L+20, sy+28, "🔑 A DIFERENÇA", 18, "#333"))

elements.append(text(L+20, sy+55,
    "AMBOS são só um arquivo de números. Zero código, zero regras.", 15, "#333"))
elements.append(text(L+20, sy+78,
    "VISÃO: números representam bordas, texturas, formas.       LINGUAGEM: números representam conceitos, relações, gramática.",
    14, "#555"))

# ── Write ────────────────────────────────────────────────────────────────

doc = {
    "type": "excalidraw", "version": 2,
    "source": "https://excalidraw.com",
    "elements": elements,
    "appState": {
        "viewBackgroundColor": "#ffffff", "gridSize": None,
        "scrollX": 0, "scrollY": 0,
        "zoom": {"value": 0.55},
        "activeTool": {"type":"selection","customType":None,"locked":False,"lastActiveTool":None},
    },
    "files": {},
}

out_dir = os.path.dirname(__file__)
out = os.path.join(out_dir, "visao-vs-linguagem.excalidraw")
with open(out, "w", encoding="utf-8") as f:
    json.dump(doc, f, indent=2, ensure_ascii=False)

counts = {}
for e in elements: counts[e["type"]] = counts.get(e["type"], 0) + 1
print(f"✅ Saved {len(elements)} elements to {out}")
print(f"   Types: {counts}")
