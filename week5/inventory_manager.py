import json

INVENTORY_FILE = "inventory.json"

def load_inventory():
    # Loads inventory data from inventory.json

    inventory = []

    try:
        with open(INVENTORY_FILE, "r") as file:
            inventory = json.load(file)

        return inventory, True

    except FileNotFoundError:
        return inventory, False


def save_inventory(inventory):
    # Saves inventory data to inventory.json

    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory, file, indent=4)

def search_product(inventory, product_id):
    # Searches for a product using its product ID

    for product in inventory:
        if product["id"] == product_id:
            return product

    return None


def add_product(inventory, product_id, name, price, stock):
    # Check if product already exists

    existing_product = search_product(inventory, product_id)

    if existing_product is not None:
        return False

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }

    inventory.append(product)

    return True


def update_stock(inventory, product_id, new_stock):
    # Search for the product

    product = search_product(inventory, product_id)

    if product is None:
        return False

    product["stock"] = new_stock

    return True

