# 🚀 INSTRUÇÕES: Processar Produtos da Imagem

## Como Executar:

1. Abre o PowerShell ou Command Prompt
2. Navega para a pasta: `cd C:\Users\User\Desktop\STREETMOOD`
3. Executa: `python process_products_from_image.py`

## O que o script faz:

1. ✅ Carrega produtos existentes do `all_products_output.js`
2. ✅ Processa produtos da imagem fornecida
3. ✅ Associa imagens da pasta `imagens_produtos` pelo nome
4. ✅ Calcula preços com margem (20 USD → 70€)
5. ✅ Extrai tamanhos automaticamente
6. ✅ Atualiza `all_products_output.js` com todos os produtos
7. ✅ Atualiza `streetmood_images_mapping.json` com mapeamentos

## Resultado:

- Produtos existentes mantidos
- Novos produtos da imagem adicionados
- Imagens associadas automaticamente pelo nome
- Sem links ou campos desnecessários
- Estrutura limpa e organizada

## Depois de executar:

1. Verifica `all_products_output.js` - deve ter todos os produtos
2. Verifica `streetmood_images_mapping.json` - deve ter mapeamentos
3. Abre `index.html` no navegador para testar
4. Faz commit e push para atualizar online

