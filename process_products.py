# Script to process product list and generate JavaScript array
products_text = """air-jordan-10,Air Jordan 10 - White brown40-47,$350.00,$39.00,https://www.ubzy.ru/product/air-jordan-10-white-brown40-47/
air-jordan-10,Air Jordan 10 - White black40-47,$350.00,$39.00,https://www.ubzy.ru/product/air-jordan-10-white-black40-47/"""

# Function to calculate EUR price from USD
def calculate_price_eur(usd_price):
    usd = float(usd_price.replace('$', ''))
    if usd <= 30:
        return 70
    elif usd <= 45:
        return 90
    elif usd >= 55:
        return 115
    else:
        return 90

# Process products
products_js = []
id_counter = 1

lines = products_text.strip().split('\n')
for line in lines:
    if not line.strip():
        continue
    parts = line.split(',')
    if len(parts) >= 4:
        modelo = parts[0].strip()
        produto = parts[1].strip()
        preco_antigo = parts[2].strip()
        preco_atual = parts[3].strip()
        link = parts[4].strip() if len(parts) > 4 else ""
        
        # Extract size from product name if present
        size = ""
        if "40-47" in produto:
            size = "40-47"
        elif "36-40" in produto:
            size = "36-40"
        elif "40-46" in produto:
            size = "40-46"
        elif "36-46" in produto:
            size = "36-46"
        elif "36-47" in produto:
            size = "36-47"
        elif "36-45" in produto:
            size = "36-45"
        
        # Calculate EUR price
        price_eur = calculate_price_eur(preco_atual)
        price_box_eur = price_eur + 5
        
        # Extract buy_usd
        buy_usd = float(preco_atual.replace('$', ''))
        
        product_obj = {
            "id": id_counter,
            "name": produto,
            "buy_usd": buy_usd,
            "price_eur": price_eur,
            "price_box_eur": price_box_eur,
            "size": size,
            "image": "",
            "link": link,
            "tipo": "stock",
            "desc": ""
        }
        
        products_js.append(product_obj)
        id_counter += 1

# Generate JavaScript array
js_output = "const products = [\n"
for p in products_js:
    js_output += f'            {p},\n'
js_output += "        ];"

print(js_output)

