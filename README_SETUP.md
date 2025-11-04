# STREETMOOD - Mini Site Catálogo

Mini site interativo para apresentar todos os produtos da marca STREETMOOD.

## 🚀 Estrutura do Projeto

```
streetmood/
│
├── index.html                    # Página principal
├── style.css                     # Estilos dark/red STREETMOOD
├── streetmood_images_mapping.json   # Mapeamento produto → imagem
│
├── scripts/
│   ├── main.js                  # Lógica do catálogo, filtros, modal
│   └── products.js              # Fallback de produtos (opcional)
│
├── imagens_produtos/            # Pasta com todas as imagens .jpg
│   ├── Air Jordan 312_1.jpg
│   ├── Air Jordans 1 CD4487-100_1.jpg
│   └── ...
│
└── 3d/                          # Modelos 3D para Fresh Drops
    ├── README.md
    └── puremoney.glb            # (adicione aqui o modelo 3D)
```

## 📋 Funcionalidades

✅ **Catálogo Completo**
- Exibe todos os produtos do ficheiro `all_products_output.js`
- Imagens associadas via `streetmood_images_mapping.json`
- Placeholder para produtos sem imagem

✅ **Filtros e Pesquisa**
- Pesquisa por nome ou tamanho
- Filtro por tipo (Todos / Stock / Fresh Drops)
- Ordenação por nome ou preço

✅ **Modal de Detalhes**
- Visualização detalhada do produto
- Visualizador 3D interativo para Fresh Drops (usando model-viewer)
- Botões de ação: Comprar/DM e Reservar

✅ **Integração WhatsApp**
- Botão "Comprar / DM" → mensagem automática com produto e preço
- Botão "Reservar" → mensagem automática de reserva
- Botão WhatsApp no header

✅ **Design STREETMOOD**
- Tema dark com gradientes (#0b0b0b → #111)
- Acentos vermelhos (#ff2a2a)
- Efeitos glass/blur
- Totalmente responsivo (desktop e mobile)

## 🛠️ Como Usar

### 1. Preparação

1. **Imagens**: Certifica-te de que todas as imagens estão na pasta `imagens_produtos/`
2. **Mapeamento**: O ficheiro `streetmood_images_mapping.json` já está configurado
3. **Produtos**: Os produtos são carregados de `all_products_output.js`

### 2. Adicionar Modelo 3D

Para produtos com `"tipo": "drop"`:

1. Coloca o ficheiro `.glb` na pasta `3d/` (ex: `puremoney.glb`)
2. No `scripts/main.js`, o código já detecta produtos com "Pure Money" no nome
3. Para outros produtos, adiciona a lógica na função `openModal()`

### 3. Configurar WhatsApp

Edita o número no ficheiro `scripts/main.js`:

```javascript
const WHATSAPP_NUMBER = '351912345678'; // Substitui pelo teu número
```

### 4. Abrir o Site

Simplesmente abre `index.html` no navegador. Não precisa de servidor!

Para desenvolvimento local com atualizações automáticas:
```bash
# Com Python 3
python -m http.server 8000

# Com Node.js (http-server)
npx http-server
```

Depois abre `http://localhost:8000` no navegador.

## 📦 Hospedagem

O site funciona perfeitamente em:

- **GitHub Pages**: Faz push para um repositório e ativa GitHub Pages
- **Vercel**: Arrasta a pasta para vercel.com
- **Netlify**: Arrasta a pasta para netlify.com
- **Firebase Hosting**: `firebase deploy`

## 🎨 Personalização

### Adicionar Novo Produto "Drop"

1. Adiciona o produto em `all_products_output.js` com `"tipo": "drop"`
2. Adiciona o mapeamento da imagem em `streetmood_images_mapping.json`
3. Se quiseres 3D, adiciona o modelo `.glb` na pasta `3d/`
4. Atualiza a função `openModal()` em `scripts/main.js` para associar o modelo

### Mudar Cores

Edita as variáveis CSS em `style.css`:

```css
:root {
    --bg-primary: #0b0b0b;
    --bg-secondary: #111111;
    --accent: #ff2a2a;        /* Cor principal vermelha */
    --accent-hover: #ff4040;
    ...
}
```

## 📝 Notas Importantes

- O visualizador 3D usa `<model-viewer>` do Google (carregado via CDN)
- As imagens são carregadas dinamicamente via `streetmood_images_mapping.json`
- Se uma imagem não existir, aparece um placeholder automático
- Os produtos são filtrados e ordenados em tempo real (sem reload)

## 🐛 Troubleshooting

**Problema**: Imagens não aparecem
- Verifica que o caminho em `streetmood_images_mapping.json` está correto
- Verifica que o ficheiro existe na pasta `imagens_produtos/`

**Problema**: Modelo 3D não carrega
- Verifica que o ficheiro `.glb` existe na pasta `3d/`
- Verifica o console do navegador para erros
- Certifica-te de que o produto tem `"tipo": "drop"`

**Problema**: Produtos não aparecem
- Verifica que `all_products_output.js` está carregado no HTML
- Abre o console do navegador para ver erros

## 📞 Suporte

Para questões ou sugestões, contacta STREETMOOD via WhatsApp ou Instagram.

---

**STREETMOOD** — Qualquer vibe, qualquer ocasião. 🔥

