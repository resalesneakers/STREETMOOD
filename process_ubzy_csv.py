import csv
import json
import re
import io

# Função para calcular preço final com margem
def calculate_price_usd(buy_usd):
    """Calcula preço de venda em EUR baseado no preço de compra USD"""
    # Regras específicas conforme especificação:
    if buy_usd <= 30:
        price = 70
    elif buy_usd <= 45:
        price = 90
    elif buy_usd >= 55:
        price = 115  # Entre 110-120, usar 115
    else:
        # Margem mínima de 100% + arredondar para múltiplo de 5
        buy_eur = buy_usd * 0.92  # Converter USD para EUR
        price = buy_eur * 2
        price = round(price / 5) * 5
    
    return int(price)

# Função para extrair tamanho do nome
def extract_size(name):
    """Extrai tamanho do nome do produto"""
    # Padrões: "40-47", "36-40", "41", "42", etc.
    # Procurar padrões de tamanho válidos (36-59)
    patterns = [
        r'(\d{2}-\d{2})',  # 40-47, 36-40 (prioridade alta)
    ]
    
    for pattern in patterns:
        match = re.search(pattern, name)
        if match:
            size = match.group(1)
            parts = size.split('-')
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                # Validar que é um tamanho válido (36-59)
                if 30 <= int(parts[0]) <= 50 and 30 <= int(parts[1]) <= 50:
                    return size
    
    # Se não encontrar intervalo, procurar tamanho único
    single_match = re.search(r'\b(3[6-9]|4[0-9]|5[0-9])\b', name)
    if single_match:
        size = single_match.group(1)
        if 36 <= int(size) <= 59:
            return size
    
    return "Tamanhos variados"

# Função para determinar tipo (stock ou drop)
def determine_type(name, modelo):
    """Determina se é 'stock' ou 'drop'"""
    drop_keywords = ['pure money', 'limited', 'exclusive', 'special']
    name_lower = name.lower()
    if any(keyword in name_lower for keyword in drop_keywords):
        return 'drop'
    return 'stock'

# Dados do CSV (fornecido pelo utilizador)
csv_data = """Modelo,Produto,Preço Antigo,Preço Atual,Link
air-jordan-10,Air Jordan 10 - White brown40-47,$350.00,$39.00,https://www.ubzy.ru/product/air-jordan-10-white-brown40-47/
air-jordan-10,Air Jordan 10 - White black40-47,$350.00,$39.00,https://www.ubzy.ru/product/air-jordan-10-white-black40-47/
air-jordan-4-air-jordan,Air Jordans 4 'Pure Money' 308497-100,$338.00,$32.00,https://www.ubzy.ru/product/air-jordans-4-pure-money-308497-100/"""

# Ler CSV
products = []
id_counter = 1

# Tentar ler do ficheiro primeiro
csv_file = None
csv_paths = [
    'c:\\Users\\User\\Desktop\\ubzy_products.csv',
    'ubzy_products.csv',
    '..\\ubzy_products.csv'
]

for path in csv_paths:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            csv_file = path
            break
    except:
        continue

if csv_file:
    print(f"Lendo CSV de: {csv_file}")
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                produto_nome = row['Produto'].strip()
                preco_atual = row['Preço Atual'].strip()
                
                # Extrair preço de compra USD
                buy_usd_str = preco_atual.replace('$', '').replace(',', '')
                try:
                    buy_usd = float(buy_usd_str)
                except:
                    buy_usd = 35.0
                
                # Calcular preço final
                price_eur = calculate_price_usd(buy_usd)
                
                # Extrair tamanho
                size = extract_size(produto_nome)
                
                # Determinar tipo
                tipo = determine_type(produto_nome, row.get('Modelo', ''))
                
                # Criar produto (SEM campos de compra, link, etc.)
                product = {
                    "id": id_counter,
                    "name": produto_nome,
                    "price_eur": price_eur,
                    "size": size,
                    "tipo": tipo,
                    "desc": "Estado: Novo. Envio grátis. Caixa STREETMOOD incluída."
                }
                
                products.append(product)
                id_counter += 1
    except Exception as e:
        print(f"Erro ao processar CSV: {e}")
        products = []

if len(products) == 0:
    print("⚠️ CSV não encontrado ou vazio. Usando dados de exemplo...")

# Gerar ficheiro JavaScript
js_content = "const products = [\n"
for p in products:
    js_content += f'    {json.dumps(p, ensure_ascii=False)},\n'
js_content = js_content.rstrip(',\n') + "\n];\n"

# Escrever ficheiro
with open('all_products_output.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"✅ Processados {len(products)} produtos!")
print(f"✅ Ficheiro all_products_output.js atualizado!")
