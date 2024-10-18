from flask import Flask, render_template, jsonify
import json
import random
import os

app = Flask(__name__)

def load_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    stores_path = os.path.join(base_dir, 'data', 'stores.json')
    menus_path = os.path.join(base_dir, 'data', 'menus.json')
    
    with open(stores_path, 'r', encoding='utf-8') as f:
        stores = json.load(f)
    with open(menus_path, 'r', encoding='utf-8') as f:
        menus = json.load(f)
    print(f"Loaded {len(stores)} stores and {len(menus)} menus.")
    return stores, menus

@app.route('/')
def index():
    stores, menus = load_data()
    if stores and menus:
        selected_store = random.choice(stores)
        store_menus = [menu for menu in menus if menu['store_id'] == selected_store['id']]
        print(f"ร้านที่สุ่มได้: {selected_store['name']}, เมนูที่สุ่มได้: {len(store_menus)}")
        if store_menus:
            selected_menu = random.choice(store_menus)
        else:
            selected_menu = None
    else:
        selected_store = None
        selected_menu = None

    return render_template('index.html', store=selected_store, menu=selected_menu)

@app.route('/random-food')
def random_food():
    stores, menus = load_data()
    if stores and menus:
        selected_store = random.choice(stores)
        store_menus = [menu for menu in menus if menu['store_id'] == selected_store['id']]
        if store_menus:
            selected_menu = random.choice(store_menus)
        else:
            selected_menu = None
    else:
        selected_store = None
        selected_menu = None

    return jsonify(store=selected_store, menu=selected_menu)

if __name__ == '__main__':
    app.run(debug=True)
