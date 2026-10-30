import json
from inventory import Inventory
from product import Product
INVENTORY_FILE = "inventory.json"

def load_inventory():
    inventory = Inventory()

    try:
        with open(INVENTORY_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return inventory, False

    # JSON stores dictionaries. Rebuild Product objects when loading them.
    for item in data:
        product = Product(
            item["id"], item["name"], item["price"], item["stock"]
        )
        if not inventory.add_product(product):
            raise ValueError("Duplicate product ID in inventory.json.")

    return inventory, True


def save_inventory(inventory):
    # Convert each Product to a dictionary that json.dump can write.
    data = []
    for product in inventory.get_products():
        data.append({
            "id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock()
        })

    with open(INVENTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
