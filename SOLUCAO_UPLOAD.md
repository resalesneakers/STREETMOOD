# 🚀 SOLUÇÃO: Upload Ficheiro a Ficheiro (SEM Pastas)

## ⚡ Método Rápido - Passo a Passo

### 1️⃣ Criar Repositório
- Vai a: https://github.com/new
- Nome: `streetmood-catalog`
- **Public** ✅
- Clica "Create repository"

### 2️⃣ Upload Ficheiros da Raiz (5 ficheiros)

**"Add file"** → **"Upload files"** → Arrasta:
- `index.html`
- `style.css`
- `streetmood_images_mapping.json`
- `all_products_output.js`

Clica **"Commit changes"**

### 3️⃣ Criar Pasta `scripts/` (Método: Criar Ficheiro com Caminho)

**"Add file"** → **"Create new file"**

Escreve: `scripts/main.js`

Copia e cola o conteúdo completo do ficheiro `scripts/main.js` do teu computador.

[Copia o conteúdo abaixo - são as primeiras 50 linhas, depois copia o resto do ficheiro]

```javascript
// STREETMOOD - Main JavaScript Logic

let products = [];
let imgMap = {};
let currentProduct = null;

// WhatsApp number (update with your actual number)
const WHATSAPP_NUMBER = '351912345678';

// Initialize the application
async function init() {
    try {
        // Load image mapping
        imgMap = await fetch('streetmood_images_mapping.json').then(r => r.json());
        
        // Load products from external file
        // Products should be loaded from all_products_output.js (loaded in HTML)
        if (typeof window.products !== 'undefined') {
            products = window.products;
        } else {
            // Fallback: load from scripts/products.js
            try {
                await loadProductsFromFile('scripts/products.js');
            } catch (e) {
                console.warn('Could not load products from file, using default products');
                loadDefaultProducts();
            }
        }
        
        // Process products: add images from mapping
        products.forEach(p => {
            const imageFile = imgMap[p.id];
            if (imageFile && imageFile.trim() !== '') {
                p.image = 'imagens_produtos/' + imageFile;
            } else {
                p.image = null;
            }
        });
        
        // Initial render
        render();
        
    } catch (error) {
        console.error('Error initializing:', error);
        // Fallback to default products
        loadDefaultProducts();
        render();
    }
}
```

**[IMPORTANTE: Copia TODO o conteúdo do ficheiro scripts/main.js do teu computador]**

Clica **"Commit new file"**

### 4️⃣ Criar `scripts/products.js`

Repete o processo:
- **"Add file"** → **"Create new file"**
- Escreve: `scripts/products.js`
- Cola o conteúdo do ficheiro `scripts/products.js`

### 5️⃣ Upload Imagens (Truque Especial)

**Para cada imagem:**
1. **"Add file"** → **"Upload files"**
2. Arrasta algumas imagens (10-20 por vez)
3. **ANTES de fazer commit**, clica em cada ficheiro e edita o nome para: `imagens_produtos/[nome-do-ficheiro]`

**Exemplo:** Se a imagem se chama `Air Jordan 312_1.jpg`, escreve: `imagens_produtos/Air Jordan 312_1.jpg`

4. Clica **"Commit changes"**
5. Repete para mais imagens

### 6️⃣ Criar `3d/README.md`

**"Add file"** → **"Create new file"**
- Escreve: `3d/README.md`
- Cola o conteúdo do `3d/README.md`

### 7️⃣ Ativar GitHub Pages

- Settings → Pages → Source: **main** → Save

---

## 💡 DICA MEGA RÁPIDA

**Se tiveres muitas imagens (128 imagens):**

Faz upload apenas de **10-15 imagens de teste** primeiro para ver se funciona. Depois adicionas o resto gradualmente ou usa GitHub Desktop quando tiveres oportunidade.

---

## ✅ Estrutura Final no GitHub

```
streetmood-catalog/
├── index.html
├── style.css
├── streetmood_images_mapping.json
├── all_products_output.js
├── scripts/
│   ├── main.js
│   └── products.js
├── imagens_produtos/
│   ├── Air Jordan 312_1.jpg
│   ├── Air Jordans 1 CD4487-100_1.jpg
│   └── ... (todas as imagens)
└── 3d/
    └── README.md
```

---

## 🎯 Resumo Ultra-Rápido

1. ✅ Upload 4 ficheiros da raiz
2. ✅ Criar `scripts/main.js` (criar novo ficheiro com caminho)
3. ✅ Criar `scripts/products.js`
4. ✅ Upload imagens (mudar nome para `imagens_produtos/...`)
5. ✅ Criar `3d/README.md`
6. ✅ Ativar Pages

Feito! 🚀

