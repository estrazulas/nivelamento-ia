# CLAUDE.md — Capacitação IA para Devs

## Excalidraw — Modelo de Apresentação

**SEMPRE leia** [`excalidraw/modelo_apresentacao.md`](excalidraw/modelo_apresentacao.md) **ANTES de criar qualquer slide novo.**
Contém: grid de slides (2 colunas × N linhas), dimensões, cores do tema,
tipografia, padrões de conteúdo (comparação 2 colunas, grid 2×2),
script de exportação Python e checklist de validação.

**Exemplo visual de referência**: [`excalidraw/prompts-engenharia.excalidraw`](excalidraw/prompts-engenharia.excalidraw)
— apresentação completa com 6 slides. Use `get_code_snippet` ou leia o JSON
para consultar posições, cores e dimensões reais de slides existentes.

## Excalidraw — Lições Aprendidas (NÃO REPETIR)

### 1. MCP é volátil → sempre exportar para arquivo
O servidor MCP do Excalidraw armazena elementos apenas em memória.
Se a sessão resetar, **tudo se perde**.
**Regra**: após criar elementos via MCP, imediatamente exportar para `.excalidraw` no disco.

### 2. Formato `.excalidraw` é rigoroso — TODOS os campos são obrigatórios
Os elementos retornados pelo `get_resource` do MCP **não incluem** campos defaults.
Ao montar o JSON para arquivo, **todo elemento precisa de**:

```
angle, opacity, roundness, boundElements, groupIds, frameId,
isDeleted, locked, seed, versionNonce, updated
```

**Text** precisa adicionalmente de:
```
width, height, fontFamily (1=Virgil, 2=Helvetica, 3=Cascadia),
textAlign, verticalAlign, autoResize, lineHeight, strokeColor
```

**Rectangle** precisa de: `fillStyle`
**Arrow** precisa de: `startArrowhead, endArrowhead, points`

### 3. Dimensões de texto precisam ser calculadas
Excalidraw **não calcula** width/height automaticamente ao carregar o JSON:
- `width = max_chars_por_linha × fontSize × 0.58`
- `height = num_linhas × fontSize × 1.35`

### 4. Validar layout antes de entregar
Sempre verificar se textos cabem dentro dos containers:
- `texto.y + texto.height < container.y + container.height`
- Se não couber: aumentar `container.height` OU mover texto para baixo

### 5. `appState` mínimo funcional
```json
{
  "viewBackgroundColor": "#ffffff",
  "gridSize": null,
  "scrollX": 0,
  "scrollY": 0,
  "zoom": {"value": 1},
  "activeTool": {"type": "selection", "customType": null, "locked": false, "lastActiveTool": null}
}
```

### 6. Pipeline correto para criar apresentações Excalidraw
1. Criar elementos via MCP (`create_element`)
2. Obter elementos via `get_resource` (`elements`)
3. Montar JSON completo com **todos os campos obrigatórios** (script Python)
4. Salvar como `.excalidraw` no diretório `excalidraw/`
5. Validar abrindo em [excalidraw.com](https://excalidraw.com)

### 7. Efeito cascata ao redimensionar — validar de dentro pra fora
Quando um texto vaza de um container e você aumenta o container, **o problema sobe um nível**:
- Texto vaza do card → aumenta o card → card vaza da seção → aumenta a seção → **seção vaza do slide**
- **Regra**: após qualquer redimensionamento, validar a cadeia inteira:
  1. `texto` cabe no `card`?
  2. `card` cabe na `seção` (fundo colorido)?
  3. `seção` cabe no `slide` (fundo cinza)?
  4. `labels` e `navegação` não foram soterrados?
- **NUNCA aumentar só o primeiro nível e parar.**
