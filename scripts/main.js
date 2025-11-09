// STREETMOOD - Main JavaScript Logic

// products será carregado de streetmood_products.js (já declarado lá)
// Usar window.products ou products global
let imgMap = {};
let currentProduct = null;

// WhatsApp number oficial STREETMOOD
const WHATSAPP_NUMBER = '351929461628';
const INSTAGRAM_URL = 'https://instagram.com/streetm00d_';

// Initialize the application
async function init() {
    try {
        // Load image mapping
        try {
            imgMap = await fetch('streetmood_images_mapping.json').then(r => {
                if (!r.ok) throw new Error('Ficheiro não encontrado');
                return r.json();
            });
            console.log('✅ Mapeamento de imagens carregado:', Object.keys(imgMap).length, 'mapeamentos');
        } catch (error) {
            console.warn('⚠️ Erro ao carregar mapeamento de imagens:', error);
            imgMap = {}; // Continuar sem mapeamento
        }
        
        // Load products from external file
        // Products should be loaded from streetmood_products.js (loaded in HTML BEFORE this script)
        // products já foi declarado em streetmood_products.js, apenas usar a referência global
        if (typeof window.products !== 'undefined' && Array.isArray(window.products)) {
            // Usar window.products diretamente
            console.log('✅ Produtos carregados de window.products:', window.products.length);
        } else if (typeof products !== 'undefined' && Array.isArray(products)) {
            // Tentar variável global products (sem window)
            window.products = products;
            console.log('✅ Produtos carregados de products:', products.length);
        } else {
            // Aguardar um pouco para garantir que o script foi carregado
            console.warn('⚠️ Aguardando carregamento de produtos...');
            let attempts = 0;
            const maxAttempts = 50;
            while ((typeof window.products === 'undefined' && typeof products === 'undefined') && attempts < maxAttempts) {
                await new Promise(resolve => setTimeout(resolve, 50));
                attempts++;
            }
            
            if (typeof window.products !== 'undefined' && Array.isArray(window.products)) {
                console.log('✅ Produtos carregados após espera:', window.products.length);
            } else if (typeof products !== 'undefined' && Array.isArray(products)) {
                window.products = products;
                console.log('✅ Produtos carregados após espera (variável global):', products.length);
            } else {
                console.error('❌ ERRO: Produtos não encontrados! Tentando carregar via fetch...');
                
                // Tentar carregar diretamente via fetch
                try {
                    const response = await fetch('streetmood_products.js');
                    if (response.ok) {
                        const text = await response.text();
                        // Executar o código JavaScript de forma segura
                        const script = document.createElement('script');
                        script.textContent = text;
                        document.head.appendChild(script);
                        
                        // Aguardar um pouco mais
                        await new Promise(resolve => setTimeout(resolve, 200));
                        
                        if (typeof window.products !== 'undefined' && Array.isArray(window.products)) {
                            console.log('✅ Produtos carregados via fetch:', window.products.length);
                        } else if (typeof products !== 'undefined' && Array.isArray(products)) {
                            window.products = products;
                            console.log('✅ Produtos carregados via fetch (variável global):', products.length);
                        } else {
                            throw new Error('Produtos não encontrados após carregar script');
                        }
                    } else {
                        throw new Error('Ficheiro streetmood_products.js não encontrado');
                    }
                } catch (e) {
                    console.error('❌ Erro ao carregar produtos:', e);
                    console.warn('⚠️ Usando produtos padrão...');
                    loadDefaultProducts();
                }
            }
        }
        
        // Garantir que products está disponível globalmente
        // products já foi declarado em streetmood_products.js, usar window.products
        let products = window.products || [];
        
        // Verificar se produtos foram carregados
        if (!products || products.length === 0) {
            console.error('❌ ERRO: Nenhum produto foi carregado!');
            loadDefaultProducts();
            // Atualizar referência após carregar produtos padrão
            products = window.products || [];
        }
        
        console.log('📦 Total de produtos carregados:', products.length);
        
        // Process products: add images from mapping
        // Garantir que todos os produtos são processados corretamente
        products.forEach(p => {
            // Verificar se produto tem ID válido
            if (!p.id) {
                console.warn('Produto sem ID:', p);
                return;
            }
            
            const imageFile = imgMap[p.id];
            if (imageFile && imageFile.trim() !== '') {
                p.image = 'imagens_produtos/' + imageFile;
            } else {
                p.image = null;
            }
            
            // Garantir que campos obrigatórios existem
            // Converter price string para price_eur número se necessário
            if (p.price && typeof p.price === 'string') {
                p.price_eur = parseInt(p.price.replace('€', '').trim()) || 70;
            } else if (!p.price_eur) {
                p.price_eur = 70;
            }
            if (!p.size) p.size = "Tamanhos variados";
            if (!p.tipo) p.tipo = "stock";
            if (!p.desc) p.desc = "Estado: Novo. Envio grátis. Caixa STREETMOOD incluída.";
        });
        
        console.log(`✅ Carregados ${products.length} produtos`);
        console.log(`✅ ${Object.keys(imgMap).length} produtos com imagens mapeadas`);
        
        // Garantir que products está disponível globalmente para outras funções
        // Atualizar window.products com os produtos processados
        window.products = products;
        
        // Initial render - aguardar um pouco para garantir que DOM está pronto
        setTimeout(() => {
            render();
        }, 100);
        
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
    window.products = [
        {"id": 1, "name": "Air Jordan 10 - White brown40-47", "buy_usd": 39.0, "price_eur": 90, "price_box_eur": 95, "size": "40-47", "image": "", "link": "https://www.ubzy.ru/product/air-jordan-10-white-brown40-47/", "tipo": "stock", "desc": "Produto premium importado. Envio grátis. Caixa STREETMOOD incluída."},
        {"id": 108, "name": "Air Jordan 4 'Pure Money'", "buy_usd": 55.0, "price_eur": 115, "price_box_eur": 120, "size": "40-47", "image": "", "link": "", "tipo": "drop", "desc": "Fresh Drop exclusivo! Air Jordan 4 em edição limitada. Visualizador 3D disponível."}
    ];
}

// Render function - main rendering logic
function render() {
    const q = document.getElementById('q')?.value?.toLowerCase() || '';
    const f = document.getElementById('filter')?.value || 'all';
    const s = document.getElementById('sort')?.value || 'name';
    
    // Obter products da variável global
    const products = window.products || [];
    
    // Garantir que products está carregado
    if (!products || products.length === 0) {
        console.warn('Nenhum produto carregado ainda');
        return;
    }
    
    let list = products.slice();
    
    // Filter by type
    if (f === 'stock') {
        list = list.filter(x => x.tipo === 'stock');
    } else if (f === 'drop') {
        list = list.filter(x => x.tipo === 'drop');
    }
    // Se f === 'all', não filtrar
    
    // Search filter
    if (q) {
        list = list.filter(x => {
            const searchText = (x.name + ' ' + (x.size || '') + ' ' + (x.tipo || '')).toLowerCase();
            return searchText.includes(q);
        });
    }
    
    // Sort
    if (s === 'price-asc') {
        list.sort((a, b) => (a.price_eur || 0) - (b.price_eur || 0));
    } else if (s === 'price-desc') {
        list.sort((a, b) => (b.price_eur || 0) - (a.price_eur || 0));
    } else if (s === 'name') {
        list.sort((a, b) => (a.name || '').localeCompare(b.name || ''));
    }
    
    // Render grid
    const grid = document.getElementById('grid');
    if (!grid) {
        console.error('Elemento #grid não encontrado');
        return;
    }
    
    if (list.length === 0) {
        grid.innerHTML = '<div class="no-products" style="grid-column:1/-1;text-align:center;padding:60px;color:var(--text-secondary);">Nenhum produto encontrado.</div>';
        return;
    }
    
    try {
        grid.innerHTML = list.map(gridItem).join('');
        console.log(`✅ Renderizados ${list.length} produtos de ${products.length} totais`);
    } catch (error) {
        console.error('❌ Erro ao renderizar produtos:', error);
        grid.innerHTML = '<div class="no-products" style="grid-column:1/-1;text-align:center;padding:60px;color:var(--text-secondary);">Erro ao carregar produtos. Por favor, recarrega a página.</div>';
    }
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
                 onerror="this.parentElement.innerHTML='<div class=\\'product-placeholder\\'><div class=\\'placeholder-icon\\'>👟</div><p class=\\'placeholder-text\\'>Sem foto disponível — em breve!</p></div>'">
        `;
    } else {
        imageHTML = `
            <div class="product-placeholder">
                <div class="placeholder-icon">👟</div>
                <p class="placeholder-text">Sem foto disponível — em breve!</p>
            </div>
        `;
    }
    
    return `
        <div class="product-card" onclick="openModal(${p.id})">
            <div class="product-image-container">
                ${imageHTML}
            </div>
            <div class="product-info">
                <h3 class="product-name">${p.name}</h3>
                ${p.size ? `<p class="product-size" style="font-size:11px;color:var(--text-secondary);margin-bottom:5px;">T: ${p.size}</p>` : ''}
                <p class="product-price">${p.price_eur}€</p>
                ${badge}
            </div>
        </div>
    `;
}

// Open modal with product details
function openModal(id) {
    const products = window.products || [];
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
    
    // Show image (removed 3D viewer support)
    if (imagePath) {
        mdImg.innerHTML = `<img src="${imagePath}" alt="${p.name}" style="width:100%;height:100%;object-fit:contain;" onerror="this.parentElement.innerHTML='<div class=\\'product-placeholder\\' style=\\'height:360px;\\'><div class=\\'placeholder-icon\\' style=\\'font-size:64px;\\'>👟</div><p class=\\'placeholder-text\\'>Sem foto disponível — em breve!</p></div>'">`;
    } else {
        mdImg.innerHTML = `
            <div class="product-placeholder" style="height:360px;">
                <div class="placeholder-icon" style="font-size:64px;">👟</div>
                <p class="placeholder-text">Sem foto disponível — em breve!</p>
            </div>
        `;
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
    const size = currentProduct.size || '';
    const msg = encodeURIComponent(`Olá STREETMOOD 👟 quero comprar o ${name}${size ? ' (T:' + size + ')' : ''} ainda está disponível?`);
    window.open(`https://wa.me/${WHATSAPP_NUMBER}?text=${msg}`, '_blank');
}

// Reserve product via WhatsApp
function reserveProduct() {
    if (!currentProduct) return;
    
    const name = currentProduct.name;
    const msg = encodeURIComponent(`Olá STREETMOOD 👟 quero reservar o ${name}. Podes enviar fotos reais antes do envio?`);
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

// Initialize when DOM is ready AND products are loaded
function startInit() {
    console.log('🚀 Iniciando aplicação STREETMOOD...');
    console.log('📄 DOM ready:', document.readyState);
    console.log('📦 window.products:', typeof window.products !== 'undefined' ? window.products.length + ' produtos' : 'não definido');
    console.log('📦 products (global):', typeof products !== 'undefined' ? products.length + ' produtos' : 'não definido');
    
    // Aguardar que o DOM esteja pronto E que os produtos estejam carregados
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            // Aguardar um pouco mais para garantir que streetmood_products.js foi carregado
            setTimeout(() => {
                init().catch(error => {
                    console.error('❌ Erro fatal ao inicializar:', error);
                    // Tentar renderizar mesmo assim se produtos estiverem disponíveis
                    setTimeout(() => {
                        if (products && products.length > 0) {
                            console.log('🔄 Tentando renderizar produtos disponíveis...');
                            render();
                        } else {
                            console.error('❌ Não foi possível carregar produtos');
                        }
                    }, 500);
                });
            }, 200);
        });
    } else {
        // DOM já está pronto, aguardar um pouco para garantir que produtos foram carregados
        setTimeout(() => {
            init().catch(error => {
                console.error('❌ Erro fatal ao inicializar:', error);
                // Tentar renderizar mesmo assim se produtos estiverem disponíveis
                setTimeout(() => {
                    if (products && products.length > 0) {
                        console.log('🔄 Tentando renderizar produtos disponíveis...');
                        render();
                    } else {
                        console.error('❌ Não foi possível carregar produtos');
                    }
                }, 500);
            });
        }, 200);
    }
}

// Iniciar
startInit();

