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

// Load products from external JS file
function loadProductsFromFile(filePath) {
    return new Promise((resolve, reject) => {
        const script = document.createElement('script');
        script.src = filePath;
        script.onload = () => {
            // Check if products variable exists globally
            if (typeof window.products !== 'undefined') {
                products = window.products;
                resolve();
            } else {
                reject(new Error('Products variable not found'));
            }
        };
        script.onerror = reject;
        document.head.appendChild(script);
    });
}

// Default products (fallback)
function loadDefaultProducts() {
    products = [
        {"id": 1, "name": "Air Jordan 10 - White brown40-47", "buy_usd": 39.0, "price_eur": 90, "price_box_eur": 95, "size": "40-47", "image": "", "link": "https://www.ubzy.ru/product/air-jordan-10-white-brown40-47/", "tipo": "stock", "desc": "Produto premium importado. Envio grátis. Caixa STREETMOOD incluída."},
        {"id": 108, "name": "Air Jordan 4 'Pure Money'", "buy_usd": 55.0, "price_eur": 115, "price_box_eur": 120, "size": "40-47", "image": "", "link": "", "tipo": "drop", "desc": "Fresh Drop exclusivo! Air Jordan 4 em edição limitada. Visualizador 3D disponível."}
    ];
}

// Render function - main rendering logic
function render() {
    const q = document.getElementById('q').value.toLowerCase();
    const f = document.getElementById('filter').value;
    const s = document.getElementById('sort').value;
    
    let list = products.slice();
    
    // Filter by type
    if (f === 'stock') list = list.filter(x => x.tipo === 'stock');
    if (f === 'drop') list = list.filter(x => x.tipo === 'drop');
    
    // Search filter
    if (q) {
        list = list.filter(x => 
            (x.name + ' ' + (x.size || '')).toLowerCase().includes(q)
        );
    }
    
    // Sort
    if (s === 'price-asc') {
        list.sort((a, b) => a.price_eur - b.price_eur);
    } else if (s === 'price-desc') {
        list.sort((a, b) => b.price_eur - a.price_eur);
    } else if (s === 'name') {
        list.sort((a, b) => a.name.localeCompare(b.name));
    }
    
    // Render grid
    const grid = document.getElementById('grid');
    if (list.length === 0) {
        grid.innerHTML = '<div class="no-products" style="grid-column:1/-1;text-align:center;padding:60px;color:var(--text-secondary);">Nenhum produto encontrado.</div>';
        return;
    }
    
    grid.innerHTML = list.map(gridItem).join('');
}

// Render single product card
function gridItem(p) {
    const badge = p.tipo === 'drop' 
        ? '<span class="product-badge badge-drop">🔥 Fresh Drop</span>'
        : '<span class="product-badge badge-stock">Em Stock</span>';
    
    const imagePath = imgMap[p.id] && imgMap[p.id].trim() !== '' 
        ? `imagens_produtos/${imgMap[p.id]}` 
        : null;
    
    let imageHTML = '';
    if (imagePath) {
        imageHTML = `
            <img src="${imagePath}" 
                 alt="${p.name}" 
                 class="product-image"
                 onerror="this.parentElement.innerHTML='<div class=\\'product-placeholder\\'>👟</div>'">
        `;
    } else {
        imageHTML = '<div class="product-placeholder">👟</div>';
    }
    
    return `
        <div class="product-card" onclick="openModal(${p.id})">
            <div class="product-image-container">
                ${imageHTML}
            </div>
            <div class="product-info">
                <h3 class="product-name">${p.name}</h3>
                <p class="product-price">${p.price_eur}€</p>
                ${badge}
            </div>
        </div>
    `;
}

// Open modal with product details
function openModal(id) {
    const p = products.find(x => x.id === id);
    if (!p) return;
    
    currentProduct = p;
    
    const modal = document.getElementById('modal');
    const mdName = document.getElementById('mdName');
    const mdPrice = document.getElementById('mdPrice');
    const mdDesc = document.getElementById('mdDesc');
    const mdBadge = document.getElementById('mdBadge');
    const mdImg = document.getElementById('mdImg');
    
    // Set product info
    mdName.textContent = `${p.name}${p.size ? ' • T:' + p.size : ''}`;
    mdPrice.textContent = `${p.price_eur}€`;
    mdDesc.textContent = p.desc || 'Produto premium importado. Envio grátis. Caixa STREETMOOD incluída. Caixa original disponível (+5€).';
    
    // Set badge
    if (p.tipo === 'drop') {
        mdBadge.innerHTML = '<span class="product-badge badge-drop">🔥 Fresh Drop</span>';
    } else {
        mdBadge.innerHTML = '<span class="product-badge badge-stock">Em Stock</span>';
    }
    
    // Set image or 3D viewer
    const imagePath = imgMap[p.id] && imgMap[p.id].trim() !== '' 
        ? `imagens_produtos/${imgMap[p.id]}` 
        : null;
    
    if (p.tipo === 'drop') {
        // For drops, show 3D viewer (if available) or image
        // Check if product is Pure Money (example for 3D model)
        // Check if 3D model exists for this drop product
        const isPureMoney = p.name.toLowerCase().includes('pure money') || p.name.toLowerCase().includes('puremoney');
        if (isPureMoney) {
            // Try to load 3D model - if it fails, fallback to image
            mdImg.innerHTML = `
                <model-viewer 
                    src="3d/puremoney.glb" 
                    alt="${p.name}"
                    auto-rotate
                    camera-controls
                    style="width:100%;height:360px;border-radius:12px;"
                    onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                </model-viewer>
                <div style="display:none;flex-direction:column;align-items:center;justify-content:center;height:360px;">
                    ${imagePath ? `<img src="${imagePath}" alt="${p.name}" style="width:100%;height:100%;object-fit:contain;">` : '<div class="product-placeholder" style="height:360px;">👟<br><small>Imagem em atualização</small></div>'}
                </div>
            `;
        } else if (imagePath) {
            mdImg.innerHTML = `<img src="${imagePath}" alt="${p.name}" style="width:100%;height:100%;object-fit:contain;">`;
        } else {
            mdImg.innerHTML = '<div class="product-placeholder" style="height:360px;">👟<br><small>Imagem em atualização</small></div>';
        }
    } else {
        // For stock items, show image
        if (imagePath) {
            mdImg.innerHTML = `<img src="${imagePath}" alt="${p.name}" style="width:100%;height:100%;object-fit:contain;">`;
        } else {
            mdImg.innerHTML = '<div class="product-placeholder" style="height:360px;">👟<br><small>Imagem em atualização</small></div>';
        }
    }
    
    // Show modal
    modal.classList.add('show');
    document.body.style.overflow = 'hidden';
}

// Close modal
function closeModal() {
    const modal = document.getElementById('modal');
    modal.classList.remove('show');
    document.body.style.overflow = '';
    currentProduct = null;
}

// Contact seller via WhatsApp (Buy/DM button)
function contactSeller() {
    if (!currentProduct) return;
    
    const name = currentProduct.name;
    const price = currentProduct.price_eur;
    const msg = encodeURIComponent(`Olá STREETMOOD, quero saber mais sobre o ${name} (${price}€).`);
    window.open(`https://wa.me/${WHATSAPP_NUMBER}?text=${msg}`, '_blank');
}

// Reserve product via WhatsApp
function reserveProduct() {
    if (!currentProduct) return;
    
    const name = currentProduct.name;
    const msg = encodeURIComponent(`Olá, quero reservar o produto ${name}. Podes enviar fotos reais antes do envio?`);
    window.open(`https://wa.me/${WHATSAPP_NUMBER}?text=${msg}`, '_blank');
}

// Open WhatsApp (header button)
function openWhatsApp() {
    const msg = encodeURIComponent('Olá STREETMOOD! Quero saber mais sobre os vossos produtos.');
    window.open(`https://wa.me/${WHATSAPP_NUMBER}?text=${msg}`, '_blank');
}

// Close modal on ESC key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeModal();
    }
});

// Close modal when clicking overlay
document.addEventListener('click', (e) => {
    const modal = document.getElementById('modal');
    if (e.target.classList.contains('modal-overlay')) {
        closeModal();
    }
});

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}

