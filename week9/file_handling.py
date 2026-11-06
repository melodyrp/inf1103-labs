import json

from digital_product import DigitalProduct
from inventory import Inventory
from physical_product import PhysicalProduct

INVENTORY_FILE = "inventory.json"


def load_inventory():
    inventory = Inventory()

    try:
        with open(INVENTORY_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return inventory, False

    for item in data:
        common = (item["id"], item["name"], item["price"], item["stock"])
        product_type = item.get("type", "physical")
        if product_type == "physical":
            product = PhysicalProduct(*common, weight=item.get("weight"))
        elif product_type == "digital":
            product = DigitalProduct(*common, download_size=item["download_size"])
        else:
            raise ValueError(f"Unknown product type: {product_type!r}.")
        if not inventory.add_product(product):
            raise ValueError("Duplicate product ID in inventory.json.")

    return inventory, True


def save_inventory(inventory):
    data = []
    for product in inventory.get_products():
        item = {
            "id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock(),
        }
        if isinstance(product, PhysicalProduct):
            item.update(type="physical", weight=product.weight)
        elif isinstance(product, DigitalProduct):
            item.update(type="digital", download_size=product.download_size)
        else:
            raise ValueError(f"Unsupported product class: {type(product).__name__}.")
        data.append(item)

    with open(INVENTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
        file.write("\n")
