import json
from pathlib import Path

from digital_product import DigitalProduct
from inventory import Inventory
from physical_product import PhysicalProduct
from product import Product
from supplier import Supplier

INVENTORY_FILE: str | Path = Path(__file__).with_name("inventory.json")


def load_inventory() -> tuple[Inventory, bool]:
    inventory = Inventory()
    try:
        with open(INVENTORY_FILE, encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return inventory, False

    suppliers: dict[str, Supplier] = {}
    for item in data:
        # Explicit fallback allows Week 9 files to be loaded and upgraded on save.
        record = item.get("supplier", {"supplier_id": "LEGACY",
                                      "name": "Unrecorded supplier",
                                      "contact_email": "unknown@example.com"})
        supplier_id = record["supplier_id"]
        supplier = suppliers.get(supplier_id)
        if supplier is None:
            supplier = Supplier(supplier_id, record["name"], record["contact_email"])
            suppliers[supplier_id] = supplier
        elif (supplier.get_name(), supplier.get_contact_email()) != (
                record["name"], record["contact_email"]):
            raise ValueError("Conflicting details for the same supplier ID.")

        common = (item["id"], item["name"], item["price"], item["stock"])
        product: Product
        product_type = item.get("type", "physical")
        if product_type == "physical":
            product = PhysicalProduct(*common, weight=item.get("weight"), supplier=supplier)
        elif product_type == "digital":
            product = DigitalProduct(*common, download_size=item["download_size"], supplier=supplier)
        else:
            raise ValueError(f"Unknown product type: {product_type!r}.")
        inventory.add_product(product)
    return inventory, True


def save_inventory(inventory: Inventory) -> None:
    data: list[dict[str, str | int | float | None | dict[str, str]]] = []
    for product in inventory.products:
        supplier = product.get_supplier()
        item: dict[str, str | int | float | None | dict[str, str]] = {
            "id": product.get_product_id(), "name": product.get_name(),
            "price": product.get_price(), "stock": product.get_stock(),
            "supplier": {"supplier_id": supplier.get_supplier_id(),
                         "name": supplier.get_name(),
                         "contact_email": supplier.get_contact_email()},
        }
        # Persistence needs a discriminator to reconstruct each concrete type.
        # Inventory and fulfilment behaviour still dispatch polymorphically.
        if isinstance(product, PhysicalProduct):
            item.update(type="physical", weight=product.weight)
        elif isinstance(product, DigitalProduct):
            item.update(type="digital", download_size=product.download_size)
        else:
            raise ValueError(f"Unsupported persistence type: {type(product).__name__}.")
        data.append(item)
    with open(INVENTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
        file.write("\n")
