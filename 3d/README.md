# Pasta 3D

Esta pasta contém os modelos 3D (.glb) para os produtos "Fresh Drops".

## Como adicionar um modelo 3D

1. Coloca o ficheiro `.glb` nesta pasta (ex: `puremoney.glb`)
2. No ficheiro `scripts/main.js`, atualiza a função `openModal()` para associar o modelo ao produto correto
3. Certifica-te de que o produto tem `"tipo": "drop"` no ficheiro de produtos

## Exemplo

Para o produto "Air Jordan 4 'Pure Money'":
- Ficheiro: `3d/puremoney.glb`
- O código já está configurado para mostrar o visualizador 3D quando o nome do produto contém "Pure Money"

## Formatos suportados

O visualizador usa `<model-viewer>` do Google, que suporta:
- `.glb` (recomendado)
- `.gltf`
- Outros formatos 3D através de extensões

