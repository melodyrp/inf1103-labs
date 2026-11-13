from digital_product import DigitalProduct
from file_handling import load_inventory, save_inventory
from inventory import Inventory
from order import Order
from physical_product import PhysicalProduct
from product import Product
from supplier import Supplier


def display_menu() -> None:
    print("\n----------- MENU -----------")
    print("1. Display all products\n2. Add product\n3. Update stock")
    print("4. Search product\n5. Save inventory\n6. Save and exit")
    print("7. Remove product\n8. Add product to order\n9. Display orders")
    print("10. Remove order line\n11. Cancel order")


def read_supplier(inventory: Inventory) -> Supplier:
    supplier_id = input("Supplier ID: ").strip()
    for product in inventory.products:
        if product.get_supplier().get_supplier_id() == supplier_id:
            print("Using existing supplier:", product.get_supplier().get_name())
            return product.get_supplier()
    return Supplier(supplier_id, input("Supplier name: "), input("Supplier email: "))


def display_order(order: Order) -> None:
    print(f"Order {order.get_order_id()}")
    for index, (product, quantity, subtotal) in enumerate(order.get_order_lines(), 1):
        print(f"  {index}. {product.get_name()} x {quantity}: ${subtotal:.2f}")
    print(f"  Total: ${order.calculate_total():.2f}")


def main() -> None:
    print("INVENTORY MANAGEMENT SYSTEM - WEEK 10")
    try:
        inventory, loaded = load_inventory()
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        print(f"Could not load inventory: {error}")
        return
    print("Inventory loaded." if loaded else "Starting with an empty inventory.")
    print("Orders are demonstrations kept in memory for this session only.")
    orders: dict[str, Order] = {}

    while True:
        display_menu()
        option = input("Enter option: ").strip()
        try:
            if option == "1":
                inventory.display_all_products()
            elif option == "2":
                kind = input("Type (1 = physical, 2 = digital): ").strip()
                if kind not in ("1", "2"):
                    raise ValueError("Choose product type 1 or 2.")
                product_id = input("Product ID: ").strip()
                name = input("Product name: ").strip()
                price = float(input("Price: "))
                stock = int(input("Stock quantity: "))
                supplier = read_supplier(inventory)
                product: Product
                if kind == "1":
                    product = PhysicalProduct(product_id, name, price, stock,
                                              float(input("Weight (kg): ")), supplier)
                else:
                    product = DigitalProduct(product_id, name, price, stock,
                                             float(input("Download size (MB): ")), supplier)
                inventory.add_product(product)
                print("Product added.")
            elif option == "3":
                product_id = input("Product ID: ").strip()
                quantity = int(input("New stock quantity: "))
                print("Stock updated." if inventory.update_stock(product_id, quantity)
                      else "Product not found.")
            elif option == "4":
                found = inventory.find_product(input("Product ID: ").strip())
                if found is None:
                    print("Product not found.")
                else:
                    found.display_information()
                    print(found.get_fulfilment_info())
            elif option in ("5", "6"):
                save_inventory(inventory)
                print("Inventory saved.")
                if option == "6":
                    break
            elif option == "7":
                inventory.remove_product(input("Product ID: ").strip())
                print("Product removed from inventory; existing orders retain their references.")
            elif option == "8":
                order_id = input("Order ID: ").strip()
                found = inventory.find_product(input("Product ID: ").strip())
                if found is None:
                    raise ValueError("Product not found.")
                quantity = int(input("Order quantity: "))
                order = orders.get(order_id)
                if order is None:
                    order = Order(order_id)
                    order.add_order_line(found, quantity)
                    orders[order_id] = order
                else:
                    order.add_order_line(found, quantity)
                display_order(order)
            elif option == "9":
                if not orders:
                    print("No orders.")
                for order in orders.values():
                    display_order(order)
            elif option in ("10", "11"):
                order_id = input("Order ID: ").strip()
                order = orders.get(order_id)
                if order is None:
                    raise ValueError("Order not found.")
                if option == "10":
                    display_order(order)
                    order.remove_order_line(int(input("Line number: ")) - 1)
                    display_order(order)
                else:
                    order.cancel()
                    del orders[order_id]
                    print("Order and its lines removed. Products remain available.")
            else:
                print("Choose an option from 1 to 11.")
        except (ValueError, IndexError, OSError) as error:
            print(f"Could not complete operation: {error}")


if __name__ == "__main__":
    main()
