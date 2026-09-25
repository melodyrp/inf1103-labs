"""
INF1103 Week 4 - Persistent Auditor (Advanced)
"""

# Global Constants
EXIT_SIGNAL = -99
MAX_CAPACITY = 500
TAX_RATE = 0.1
INVENTORY_FILE = "inventory.txt"

# Inventory item structure
ITEM_FIELDS = {
    "id": 0,
    "name": 1,
    "quantity": 2,
    "transaction_history": 3
}

FIELD_SEPARATOR = ","
HISTORY_SEPARATOR = "|"


def load_inventory():
    # Load all inventory items from inventory.txt

    inventory = []

    try:
        with open(INVENTORY_FILE, "r") as file:

            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split(FIELD_SEPARATOR)

                item_id = parts[0]
                name = parts[1]
                quantity = int(parts[2])

                transaction_history = []

                if len(parts) > 3 and parts[3]:
                    history_values = parts[3].split(HISTORY_SEPARATOR)

                    for value in history_values:
                        transaction_history.append(int(value))

                item = [
                    item_id,
                    name,
                    quantity,
                    transaction_history
                ]

                inventory.append(item)

    except FileNotFoundError:
        # Start with an empty inventory if file does not exist
        inventory = []

    return inventory


def save_inventory(inventory):
    # Save all inventory items and transaction histories

    with open(INVENTORY_FILE, "w") as file:

        for item in inventory:

            history = HISTORY_SEPARATOR.join(
                str(value)
                for value in item[ITEM_FIELDS["transaction_history"]]
            )

            line = (
                str(item[ITEM_FIELDS["id"]])
                + FIELD_SEPARATOR
                + item[ITEM_FIELDS["name"]]
                + FIELD_SEPARATOR
                + str(item[ITEM_FIELDS["quantity"]])
                + FIELD_SEPARATOR
                + history
            )

            file.write(line + "\n")


def display_inventory(inventory):
    # Display all current inventory items

    print("\nCurrent Inventory:")

    if not inventory:
        print("No inventory items found.")
        return

    for item in inventory:
        print(
            item[ITEM_FIELDS["id"]],
            item[ITEM_FIELDS["name"]],
            item[ITEM_FIELDS["quantity"]],
            item[ITEM_FIELDS["transaction_history"]]
        )


def find_item(inventory, item_id):
    # Search inventory for matching item ID

    for item in inventory:

        if item[ITEM_FIELDS["id"]] == item_id:
            return item

    return None


def get_valid_input(item):
    # Get and validate stock quantity

    stock_input = input(
        "Enter stock quantity for "
        + item[ITEM_FIELDS["name"]]
        + " (or 'quit' to quit): "
    )

    if stock_input.lower() == "quit":
        return EXIT_SIGNAL

    # Check negative input
    if stock_input.startswith("-"):
        if stock_input[1:].isdigit():
            print("Error: Negative stock quantities are not allowed.")
            return None

    # Check invalid input
    if not stock_input.isdigit():
        print("Error: Please enter a valid integer.")
        return None

    return int(stock_input)


def process_delivery(item, new_quantity):
    # Update item quantity

    item[ITEM_FIELDS["quantity"]] += new_quantity

    # Store transaction history
    item[ITEM_FIELDS["transaction_history"]].append(new_quantity)


def calculate_tax(amount, tax_rate):
    # Calculate tax for delivery

    tax = amount * tax_rate

    return tax


def display_status(item, valid_quantity, tax_amount):
    # Display updated item information

    print("\nDelivery accepted.")
    print("Item:", item[ITEM_FIELDS["name"]])
    print("Delivery quantity:", valid_quantity)
    print("Current quantity:", item[ITEM_FIELDS["quantity"]])
    print("Tax for this delivery:", f"{tax_amount:.2f}")


def generate_report(inventory, failed_entries):
    # Print final inventory summary

    print("\n--- Inventory Report ---")

    total_units = 0

    for item in inventory:
        total_units += item[ITEM_FIELDS["quantity"]]

    print("Total Inventory Units:", total_units)
    print("Number of Failed/Rejected Entries:", failed_entries)


def main():
    # Load inventory from file

    inventory = load_inventory()

    failed_entries = 0
    exit_program = False

    while not exit_program:

        # Show existing inventory
        display_inventory(inventory)

        item_id = input("\nEnter Item ID (or 'quit' to quit): ")

        if item_id.lower() == "quit":
            exit_program = True
            continue

        # Find selected item
        item = find_item(inventory, item_id)

        if item is None:
            print("Error: Item ID not found.")
            failed_entries += 1
            continue

        # Get delivery amount
        quantity = get_valid_input(item)

        if quantity == EXIT_SIGNAL:
            exit_program = True

        elif quantity is None:
            failed_entries += 1

        else:
            # Update item
            process_delivery(item, quantity)

            # Calculate tax
            tax_amount = calculate_tax(quantity, TAX_RATE)

            display_status(item, quantity, tax_amount)

            # Check capacity
            if item[ITEM_FIELDS["quantity"]] > MAX_CAPACITY:
                print("WARNING: Item quantity has exceeded 500 units!!!")
                exit_program = True

    # Save all data before exiting
    save_inventory(inventory)

    generate_report(inventory, failed_entries)

    print("Inventory successfully saved to inventory.txt.")


if __name__ == "__main__":
    main()