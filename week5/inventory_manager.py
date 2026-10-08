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

def display_all(inventory):
    # Displays all products

    print("\nCurrent Inventory")
    print("------------------------------------------------")

    if len(inventory) == 0:
        print("No products found.")

    else:
        for product in inventory:
            print(
                f'ID: {product["id"]} | '
                f'Name: {product["name"]} | '
                f'Price: ${product["price"]:.2f} | '
                f'Stock: {product["stock"]}'
            )

    print("------------------------------------------------")


def display_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

def main():
    """
    Main function to run inventory manager.
    """

    inventory = []
    exit_program = False

    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")

    # Load inventory
    inventory, status = load_inventory()

    if status:
        print("\ninventory.json found.")
        print("Inventory loaded successfully.")
    else:
        print("\ninventory.json not found.")
        print("Starting with empty inventory.")

    # Display menu
    display_menu()

    while not exit_program:

        option = input("\nEnter option: ")

        # Option 1 - Display all products
        if option == "1":
            display_all(inventory)

        # Option 2 - Add product
        elif option == "2":

            print("\nAdd New Product")

            product_id = input("Product ID: ")
            name = input("Product Name: ")

            try:
                price = float(input("Price: "))
                stock = int(input("Stock Quantity: "))

                added = add_product(
                    inventory,
                    product_id,
                    name,
                    price,
                    stock
                )

                if added:
                    print("\nProduct added successfully!")
                else:
                    print("\nProduct ID already exists.")

            except ValueError:
                print("\nError: Price and stock must be valid numbers.")

        # Option 3 - Update stock
        elif option == "3":

            print("\nUpdate Stock")

            product_id = input("Enter Product ID: ")

            product = search_product(inventory, product_id)

            if product is None:
                print("\nProduct not found.")

            else:
                print("\nProduct Found:")
                print("Name:", product["name"])
                print("Current Stock:", product["stock"])

                try:
                    new_stock = int(input("\nNew Stock Quantity: "))

                    updated = update_stock(
                        inventory,
                        product_id,
                        new_stock
                    )

                    if updated:
                        print("\nStock updated successfully!")

                except ValueError:
                    print("\nError: Stock quantity must be an integer.")

        # Option 4 - Search product
        elif option == "4":

            print("\nSearch Product")

            product_id = input("Enter Product ID: ")

            product = search_product(inventory, product_id)

            if product is None:
                print("\nProduct not found.")

            else:
                print("\nProduct Found")
                print("------------------------------------------------")
                print("ID:", product["id"])
                print("Name:", product["name"])
                print(f'Price: ${product["price"]:.2f}')
                print("Stock:", product["stock"])
                print("------------------------------------------------")

        # Option 5 - Save inventory
        elif option == "5":

            print("\nSaving inventory...")

            save_inventory(inventory)

            print("Inventory saved successfully to inventory.json.")

        # Option 6 - Exit
        elif option == "6":

            print("\nSaving inventory before exit...")

            save_inventory(inventory)

            print("Inventory saved successfully.")
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")

            exit_program = True

        else:
            print("\nInvalid option. Please enter a number from 1 to 6.")


# Program Entry Point
if __name__ == "__main__":
    main()