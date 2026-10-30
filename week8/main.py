from file_handling import load_inventory, save_inventory
from product import Product


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
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")

    try:
        inventory, status = load_inventory()
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        print(f"Could not load inventory: {error}")
        print("Check inventory.json before running the program again.")
        return

    if status:
        print("\nInventory loaded successfully.")
    else:
        print("\ninventory.json not found. Starting with empty inventory.")

    while True:
        display_menu()
        option = input("\nEnter option: ").strip()

        if option == "1":
            inventory.display_all()

        elif option == "2":
            print("\nAdd New Product")
            product_id = input("Product ID: ").strip()
            name = input("Product Name: ").strip()

            try:
                price = float(input("Price: "))
                stock = int(input("Stock Quantity: "))
                product = Product(product_id, name, price, stock)

                if inventory.add_product(product):
                    print("Product added successfully!")
                else:
                    print("Product ID already exists.")
            except ValueError as error:
                print(f"Invalid product: {error}")

        elif option == "3":
            product_id = input("Enter Product ID: ").strip()
            product = inventory.search_product(product_id)

            if product is None:
                print("Product not found.")
            else:
                print("Name:", product.get_name())
                print("Current Stock:", product.get_stock())
                try:
                    new_stock = int(input("New Stock Quantity: "))
                    if inventory.update_stock(product_id, new_stock):
                        print("Stock updated successfully!")
                except ValueError as error:
                    print(f"Invalid stock: {error}")

        elif option == "4":
            product_id = input("Enter Product ID: ").strip()
            product = inventory.search_product(product_id)
            if product is None:
                print("Product not found.")
            else:
                product.display_information()

        elif option == "5":
            try:
                save_inventory(inventory)
                print("Inventory saved successfully to inventory.json.")
            except OSError as error:
                print(f"Could not save inventory: {error}")

        elif option == "6":
            try:
                save_inventory(inventory)
            except OSError as error:
                print(f"Could not save inventory: {error}")
                print("Please resolve the problem and try saving again.")
            else:
                print("Inventory saved. Thank you for using the system.")
                break

        else:
            print("Invalid option. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
