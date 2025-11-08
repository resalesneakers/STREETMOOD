#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Process products from CSV file"""

import json
import re
import csv

def calculate_price_eur(usd_price):
    """Calculate EUR price from USD"""
    try:
        usd = float(usd_price.replace('$', '').replace(',', ''))
        if usd <= 30:
            return 70
        elif usd <= 45:
            return 90
        elif usd >= 55:
            return 115
        else:
            return 90
    except:
        return 90

def extract_size(name):
    """Extract size from product name"""
    size_match = re.search(r'(\d{1,2}-\d{1,2})', name)
    if size_match:
        return size_match.group(1)
    return ""

products = []
id_counter = 1

# Read from CSV file
try:
    with open('products_complete.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            modelo = row.get('Modelo', '').strip()
            produto = row.get('Produto', '').strip()
            preco_antigo = row.get('Preço Antigo', '').strip()
            preco_atual = row.get('Preço Atual', '').strip()
            link = row.get('Link', '').strip()
            
            size = extract_size(produto)
            try:
                buy_usd = float(preco_atual.replace('$', '').replace(',', ''))
            except:
                buy_usd = 39.0
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
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    # Fallback: process direct from text
    pass

# Output JavaScript
print("const products = [")
for i, p in enumerate(products):
    print(f"            {json.dumps(p, ensure_ascii=False)}", end="")
    if i < len(products) - 1:
        print(",")
    else:
        print()
print("        ];")

