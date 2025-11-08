# Script para processar produtos da imagem e associar imagens
# Executa: python process_products_from_image.py

import json
import re
import os

# Função para calcular preço final com margem
def calculate_price_usd(buy_usd):
    if buy_usd <= 30:
        return 70
    elif buy_usd <= 45:
        return 90
    elif buy_usd >= 55:
        return 115
    else:
        buy_eur = buy_usd * 0.92
        price = buy_eur * 2
        return int(round(price / 5) * 5)

# Função para extrair tamanho
def extract_size(name):
    patterns = [r'(\d{2}-\d{2})']
    for pattern in patterns:
        match = re.search(pattern, name)
        if match:
            size = match.group(1)
            parts = size.split('-')
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                if 30 <= int(parts[0]) <= 50 and 30 <= int(parts[1]) <= 50:
                    return size
    return "Tamanhos variados"

# Função para determinar tipo
def determine_type(name):
    drop_keywords = ['pure money', 'limited', 'exclusive', 'special']
    if any(keyword in name.lower() for keyword in drop_keywords):
        return 'drop'
    return 'stock'

# Função para normalizar nome
def normalize_name(name):
    name = name.lower()
    name = re.sub(r'[^\w\s]', '', name)
    name = re.sub(r'\s+', ' ', name)
    return name.strip()

# Carregar imagens disponíveis
imagens_dir = 'imagens_produtos'
imagens_disponiveis = {}
if os.path.exists(imagens_dir):
    for filename in os.listdir(imagens_dir):
        if filename.endswith('_1.jpg'):
            base_name = filename.replace('_1.jpg', '')
            normalized = normalize_name(base_name)
            imagens_disponiveis[normalized] = filename

print(f"✅ Encontradas {len(imagens_disponiveis)} imagens disponíveis")

# Produtos da imagem (baseado na descrição fornecida)
produtos_da_imagem = [
    # Air Jordan 1
    {"nome": "Air Jordan 1 Mid Black White Red", "preco": 20.0},
    {"nome": "Air Jordan 1 Low White Black Red", "preco": 20.0},
    {"nome": "Air Jordans 1 CD4487-100", "preco": 20.0},
    {"nome": "Air Jordans 1 High University Blue 555088-134", "preco": 20.0},
    {"nome": "AIR JORDANS 1 HIGH ZOOM \"Racer Blue\" CK6637-104", "preco": 20.0},
    {"nome": "AIR JORDANS 1 LOW \"Mystic Green\"553558-113", "preco": 20.0},
    {"nome": "Air Jordans 1 Mid 'Candy' 554725-083", "preco": 20.0},
    {"nome": "Air Jordans 1 Mid \"Black Cone\" 554724-062", "preco": 20.0},
    {"nome": "Air Jordans 1 Mid \"Chicago Black Toe\" 554724-069", "preco": 20.0},
    {"nome": "Air Jordans 1 Mid \"Lakers Top 3\"852542-005", "preco": 20.0},
    {"nome": "Air Jordans 1 Mid \"Multicolor\" 554724-125", "preco": 20.0},
    {"nome": "Air Jordans 1 MID \"Top 3\" 554724-124", "preco": 20.0},
    {"nome": "Air Jordans 1 Mid (GS)555112-500", "preco": 20.0},
    {"nome": "Air Jordans 1 Mid GS \"Light Smoke Grey\"554724-092", "preco": 20.0},
    {"nome": "Air Jordans 1 MID SE \"South Beach\"852542-306", "preco": 20.0},
    {"nome": "Air Jordans 1 Mid SE 852542-400", "preco": 20.0},
    {"nome": "Air Jordans 1 Retro High CN8607-002", "preco": 20.0},
    {"nome": "Air Jordans 1 Retro High Co.JP 'Midnight Navy' DC1788-100", "preco": 20.0},
    {"nome": "Air Jordans 1 Retro High OG GS \"Crimson Tint\" 555088-081", "preco": 20.0},
    {"nome": "Jordans 1 Mid White Black Light Arctic Pink 555112-103", "preco": 20.0},
    {"nome": "Jordans 1 Retro High \"Homage To Home\" 555088-001", "preco": 20.0},
    
    # Air Jordan 3
    {"nome": "Air Jordan 3 Retro Black Cement", "preco": 20.0},
    {"nome": "Air Jordans 3 'Lazer Orange' CK9246-108", "preco": 20.0},
    {"nome": "Air Jordans 3 Retro 'Red Cement' CT8532-104", "preco": 20.0},
    {"nome": "Jordan Air Jordan 3 Barely Grape Pink Purple", "preco": 20.0},
    {"nome": "Jordan Air Jordan 3 Retro Black Gold Black gold", "preco": 20.0},
    {"nome": "Jordan Air Jordan 3 retro true blue White Blue", "preco": 20.0},
    {"nome": "Jordan Air Jordan 3 tinker black and white", "preco": 20.0},
    
    # Air Jordan 4
    {"nome": "Air Jordan 4 Retro", "preco": 20.0},
    {"nome": "Air Jordan 4 Retro Bred", "preco": 20.0},
    {"nome": "Air Jordans 4 'Black Cat' CU1110-010", "preco": 20.0},
    {"nome": "Air Jordans 4 'Fire Red' DC7770-160", "preco": 20.0},
    {"nome": "Air Jordans 4 'Off Noir' DC9533-001", "preco": 20.0},
    {"nome": "Air Jordans 4 'PSG' CZ6509-100", "preco": 20.0},
    {"nome": "Air Jordans 4 'Pure Money' 308497-100", "preco": 20.0},
    {"nome": "Air Jordans 4 Bred 408452-060", "preco": 20.0},
    {"nome": "Air Jordans 4 Retro 'University Blue' CT8527-400", "preco": 20.0},
    {"nome": "Air Jordans 4 Retro \"White Oreo\" CT8527-100", "preco": 20.0},
    {"nome": "Air Jordans 4 Retro SP 'Union – Guava Ice DC9533-009", "preco": 20.0},
    {"nome": "Jordan 4 Retro Cool Grey (2019)", "preco": 20.0},
    {"nome": "Jordan 4 Retro Flight Nostalgia", "preco": 20.0},
    {"nome": "Jordan 4 Retro Lightning (2021)", "preco": 20.0},
    {"nome": "Jordan 4 Retro Metallic Green", "preco": 20.0},
    {"nome": "Jordan 4 Retro Metallic Red", "preco": 20.0},
    {"nome": "Jordan 4 Retro Motorsports (2017)", "preco": 20.0},
    {"nome": "Jordan 4 Retro SE 95 Neon", "preco": 20.0},
    {"nome": "Jordan 4 Retro Thunder (2012)", "preco": 20.0},
    
    # Air Jordan 5
    {"nome": "Nike Air Jordan 5", "preco": 20.0},
    
    # Air Jordan 6
    {"nome": "Nike Air Jordan 6 Retro Black Infrared", "preco": 20.0},
    {"nome": "Nike Air Jordan 6 Retro Carmine (2014)", "preco": 20.0},
    {"nome": "Nike Air Jordan 6 Retro Chrome Metallic Silver", "preco": 20.0},
    {"nome": "Nike Air Jordan 6 Retro DMP 2020 (GS)", "preco": 20.0},
    {"nome": "Nike Air Jordan 6 Retro Midnight Navy (2000)", "preco": 20.0},
    {"nome": "Nike Air Jordan 6 Retro UNC", "preco": 20.0},
    
    # Air Jordan 11
    {"nome": "Air Jordans 11 Retro 'Gamma Blue' 378038-006", "preco": 20.0},
    
    # Air Jordan 13
    {"nome": "Jordan 13 Retro Black White Gum", "preco": 20.0},
    {"nome": "Jordan 13 Retro Brave Blue", "preco": 20.0},
    {"nome": "Jordan 13 Retro French Blue", "preco": 20.0},
    
    # Jordan Stadium 90
    {"nome": "Nike Jordan Stadium 90 Gris", "preco": 20.0},
    {"nome": "Nike Jordan Stadium 90 White Amarillo de hoja caduca", "preco": 20.0},
    {"nome": "Nike Jordan Stadium 90 White black", "preco": 20.0},
    {"nome": "Nike Jordan Stadium 90 White Morado", "preco": 20.0},
    {"nome": "Nike Jordan Stadium 90 White pink", "preco": 20.0},
    {"nome": "Nike Jordan Stadium 90 White red", "preco": 20.0},
    
    # Outros
    {"nome": "Air Jordan 312", "preco": 20.0},
    {"nome": "Nike ACG Mountain Fly 2 Black", "preco": 20.0},
    {"nome": "Nike ACG Mountain Fly 2 Gerry", "preco": 20.0},
    {"nome": "Nike ACG Mountain Fly 2", "preco": 20.0},
]

# Carregar produtos existentes do CSV
existing_products = []
if os.path.exists('all_products_output.js'):
    with open('all_products_output.js', 'r', encoding='utf-8') as f:
        content = f.read()
        # Extrair produtos existentes usando regex
        import re as regex_module
        matches = regex_module.findall(r'\{"id":\s*(\d+),\s*"name":\s*"([^"]+)",\s*"price_eur":\s*(\d+),\s*"size":\s*"([^"]+)",\s*"tipo":\s*"([^"]+)",\s*"desc":\s*"([^"]+)"\}', content)
        for match in matches:
            existing_products.append({
                "id": int(match[0]),
                "name": match[1],
                "price_eur": int(match[2]),
                "size": match[3],
                "tipo": match[4],
                "desc": match[5]
            })

# Processar produtos da imagem
new_products = []
img_map = {}
id_counter = max([p["id"] for p in existing_products] + [0]) + 1

for item in produtos_da_imagem:
    nome_produto = item["nome"]
    buy_usd = item["preco"]
    
    # Verificar se produto já existe
    if any(p["name"] == nome_produto for p in existing_products):
        continue  # Pular se já existe
    
    price_eur = calculate_price_usd(buy_usd)
    size = extract_size(nome_produto)
    tipo = determine_type(nome_produto)
    
    # Tentar encontrar imagem correspondente
    imagem_encontrada = None
    nome_normalized = normalize_name(nome_produto)
    
    for img_normalized, img_filename in imagens_disponiveis.items():
        if nome_normalized == img_normalized:
            imagem_encontrada = img_filename
            break
        if nome_normalized in img_normalized or img_normalized in nome_normalized:
            palavras_nome = set(nome_normalized.split())
            palavras_img = set(img_normalized.split())
            if len(palavras_nome & palavras_img) >= max(2, len(palavras_nome) * 0.7):
                imagem_encontrada = img_filename
                break
    
    product = {
        "id": id_counter,
        "name": nome_produto,
        "price_eur": price_eur,
        "size": size,
        "tipo": tipo,
        "desc": "Estado: Novo. Envio grátis. Caixa STREETMOOD incluída."
    }
    
    new_products.append(product)
    
    if imagem_encontrada:
        img_map[str(id_counter)] = imagem_encontrada
    
    id_counter += 1

# Combinar produtos existentes com novos
all_products = existing_products + new_products

# Carregar e atualizar mapeamento
existing_map = {}
if os.path.exists('streetmood_images_mapping.json'):
    with open('streetmood_images_mapping.json', 'r', encoding='utf-8') as f:
        existing_map = json.load(f)

existing_map.update(img_map)

# Gerar ficheiro JavaScript
js_content = "const products = [\n"
for p in all_products:
    js_content += f'    {json.dumps(p, ensure_ascii=False)},\n'
js_content = js_content.rstrip(',\n') + "\n];\n"

# Escrever ficheiros
with open('all_products_output.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

with open('streetmood_images_mapping.json', 'w', encoding='utf-8') as f:
    json.dump(existing_map, f, indent=2, ensure_ascii=False)

print(f"✅ Total de produtos: {len(all_products)}")
print(f"✅ Produtos existentes: {len(existing_products)}")
print(f"✅ Novos produtos adicionados: {len(new_products)}")
print(f"✅ {len(img_map)} novos produtos com imagens associadas!")
print(f"✅ Ficheiros atualizados!")
