# STREETMOOD - Mini Site

Site moderno e funcional para a marca STREETMOOD, especializada em moda urbana, sneakers e streetwear.

## 🚀 Estrutura do Projeto

```
STREETMOOD/
├── streetmood_catalogo.html    # Página principal do catálogo
├── assets/
│   ├── images/                 # Imagens padrão (coming_soon.jpg)
│   ├── models/                 # Modelos 3D (.glb files)
│   └── css/                    # Estilos adicionais (opcional)
├── imagens_produtos/          # Imagens dos produtos (128 imagens .jpg)
└── README.md                   # Este ficheiro
```

## 📋 Características

- ✅ Design moderno com modo escuro (#0a0a0a / #121212)
- ✅ Toques em vermelho vibrante (#e50914 / #ff1e1e)
- ✅ Cards de produtos com animações e hover effects
- ✅ Modal interativo com modelo 3D para drops especiais
- ✅ Integração WhatsApp com mensagem automática
- ✅ Totalmente responsivo (mobile-first)
- ✅ Pesquisa e filtros avançados
- ✅ Visualizador 3D usando `<model-viewer>`

## 🎨 Funcionalidades

### Catálogo de Produtos
- Grid responsivo de produtos
- Cards com efeitos de hover (zoom, brilho, sombra)
- Badge "FRESH DROP" para produtos especiais
- Sistema de preços automático baseado em custo em dólares

### Sistema de Preços
- 30$ → 70€
- 45$ → 90€
- 55$ → 110-120€
- +5€ para caixa original

### Drops Especiais
- Produtos com `tipo: "drop"` aparecem no topo
- Modelo 3D interativo usando `model-viewer`
- Badge destacado com animação

### Modal Interativo
- Visualização de imagem ou modelo 3D
- Detalhes do produto
- Botão de reserva via WhatsApp com mensagem automática

## 📦 Instalação

1. Abra o ficheiro `streetmood_catalogo.html` no navegador
2. Ou use um servidor local (VSCode Live Server, Python HTTP Server, etc.)

### Para adicionar o modelo 3D:
1. Coloque o ficheiro `Air Jordan 4 Pure Money.glb` na pasta `assets/models/`
2. Renomeie para `jordan4.glb`
3. Os produtos com `tipo: "drop"` e `modelUrl: "assets/models/jordan4.glb"` irão mostrar o modelo 3D

### Para adicionar imagem padrão:
1. Coloque uma imagem `coming_soon.jpg` na pasta `assets/images/`
2. Produtos sem imagem usarão esta imagem padrão

## 🔧 Configuração

### Adicionar Todos os Produtos

O ficheiro atual contém apenas alguns produtos de exemplo. Para adicionar todos os 325 produtos:

1. Copie o array `products` completo do ficheiro original
2. Substitua o array no `streetmood_catalogo.html` (linha ~322)
3. Ou carregue de um ficheiro JSON externo usando `fetch()`

### Personalizar WhatsApp

Edite o número de telefone no código:
- Procure por `351912345678` e substitua pelo número real
- Aparece em várias funções: `openWhatsApp()`, `reserveProduct()`, etc.

### Personalizar Cores

As cores principais estão definidas em `:root` no CSS:
```css
--bg-primary: #0a0a0a;
--bg-secondary: #121212;
--accent-red: #e50914;
--accent-red-hover: #ff1e1e;
```

## 📱 Responsividade

O site é totalmente responsivo e adapta-se a:
- Telemóveis (320px+)
- Tablets (768px+)
- Desktop (1024px+)
- Large screens (1280px+)

## 🎯 Tecnologias Utilizadas

- HTML5 / CSS3 / JavaScript
- TailwindCSS (via CDN)
- AOS.js (Animate On Scroll)
- Google Model Viewer (para 3D)
- Google Fonts (Inter)

## 📝 Notas

- As imagens dos produtos estão na pasta `imagens_produtos/`
- O sistema tenta mapear automaticamente imagens pelo nome do produto
- Produtos sem imagem mostram `coming_soon.jpg` (precisa ser criado)
- Drops especiais precisam do ficheiro `.glb` para mostrar o modelo 3D

## 🚀 Deploy

Pode fazer deploy em:
- GitHub Pages
- Netlify
- Vercel
- Qualquer servidor estático

## 📞 Contacto

- Instagram: @streetm00d_
- WhatsApp: (configurar número real)

## 📄 Licença

Este projeto foi criado para a marca STREETMOOD.

