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
