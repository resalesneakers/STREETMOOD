#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Process complete product list from user message"""

import json
import re

def calculate_price_eur(usd_price):
    """Calculate EUR price from USD"""
    usd = float(usd_price.replace('$', '').replace(',', ''))
    if usd <= 30:
        return 70
    elif usd <= 45:
        return 90
    elif usd >= 55:
        return 115
    else:
        return 90

def extract_size(name):
    """Extract size from product name"""
    size_match = re.search(r'(\d{1,2}-\d{1,2})', name)
    if size_match:
        return size_match.group(1)
    return ""

# Read complete list from user's message
# Format: Modelo,Produto,Preço Antigo,Preço Atual,Link
products_data = """air-jordan-10,Air Jordan 10 - White brown40-47,$350.00,$39.00,https://www.ubzy.ru/product/air-jordan-10-white-brown40-47/
air-jordan-10,Air Jordan 10 - White black40-47,$350.00,$39.00,https://www.ubzy.ru/product/air-jordan-10-white-black40-47/
air-jordan-10,Air Jordan 10 - White black red40-47,$350.00,$39.00,https://www.ubzy.ru/product/air-jordan-10-white-black-red40-47/
air-jordan-10,Air Jordan 10 - White black grass green40-47,$350.00,$39.00,https://www.ubzy.ru/product/air-jordan-10-white-black-grass-green40-47/
air-jordan-10,Air Jordan 10 - shadow40-47,$350.00,$39.00,https://www.ubzy.ru/product/air-jordan-10-shadow40-47/
air-jordan-10,Air Jordan 10 - owl40-47,$350.00,$39.00,https://www.ubzy.ru/product/air-jordan-10-owl40-47/
air-jordan-10,Air Jordan 10 - New white black40-47,$350.00,$39.00,https://www.ubzy.ru/product/air-jordan-10-new-white-black40-47/
air-jordan-10,Air Jordan 10 - Miami Super Bowl40-47,$350.00,$39.00,https://www.ubzy.ru/product/air-jordan-10-miami-super-bowl40-47/
air-jordan-10,Air Jordan 10 - mandarin duck40-47,$350.00,$39.00,https://www.ubzy.ru/product/air-jordan-10-mandarin-duck40-47/
air-jordan-10,Air Jordan 10 - grey cement40-47,$350.00,$39.00,https://www.ubzy.ru/product/air-jordan-10-grey-cement40-47/
air-jordan-10,Air Jordan 10 - Chicago40-47,$350.00,$39.00,https://www.ubzy.ru/product/air-jordan-10-chicago40-47/
air-jordan-10,Air Jordan 10 - bull40-47,$350.00,$39.00,https://www.ubzy.ru/product/air-jordan-10-bull40-47/
air-jordan-10,Air Jordan 10 - black white red40-47,$350.00,$39.00,https://www.ubzy.ru/product/air-jordan-10-black-white-red40-47/
air-jordan-10,Air Jordan 10 - black white blue40-47,$350.00,$39.00,https://www.ubzy.ru/product/air-jordan-10-black-white-blue40-47/"""

products = []
id_counter = 1

# Process each line
for line in products_data.strip().split('\n'):
    if not line.strip():
        continue
    
    # Split by comma - handle URLs with commas
    # Split from right: modelo, produto, preco_antigo, preco_atual, link
    parts = line.rsplit(',', 4)
    
    if len(parts) >= 4:
        modelo = parts[0].strip()
        produto = parts[1].strip()
        preco_antigo = parts[2].strip()
        preco_atual = parts[3].strip()
        link = parts[4].strip() if len(parts) > 4 else ""
        
        size = extract_size(produto)
        buy_usd = float(preco_atual.replace('$', '').replace(',', ''))
        price_eur = calculate_price_eur(preco_atual)
        price_box_eur = price_eur + 5
        
        product = {
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
        
        products.append(product)
        id_counter += 1

# Output JavaScript
print("const products = [")
for i, p in enumerate(products):
    print(f"            {json.dumps(p, ensure_ascii=False)}", end="")
    if i < len(products) - 1:
        print(",")
    else:
        print()
print("        ];")

