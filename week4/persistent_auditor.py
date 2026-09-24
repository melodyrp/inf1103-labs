max_capacity = 500
tax_rate = 0.1 #10% tax rate

def load_inventory():
    #Loads the current inventory from a file.

    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()

            inventory = int(lines[0].strip())

            if len(lines) > 1 and lines[1].strip():
                transaction_history = [
                    int(value) for value in lines[1].strip().split(",")
                ]
            else:
                transaction_history = []

            return inventory, transaction_history

    except FileNotFoundError:
        return 0, []



def get_valid_input():
    stock_input = input("Enter stock quantity (or 'exit' to exit): ")

    # exit program
    if stock_input.lower() == "exit":
        return "exit"

    # check for negative number
    if stock_input.startswith("-"):
        if stock_input[1:].isdigit():
            print("Error: Negative stock quantities are not allowed.")
            return None

    if not stock_input.isdigit():
        print("Error: Invalid input. Please enter a valid stock quantity (Integer).")
        return None  # check for invalid input

    # convert input to interger
    value = int(stock_input)

    return value

def process_delivery(current_total, new_value):
    # Adds the new delivery amount to the current inventory.

    new_total = current_total + new_value

    return new_total

def calculate_tax(amount):
    #Calculates 10% tax for the current delivery.

    tax = amount * tax_rate

    return tax


def generate_report(total_units, failed_attempts):
    #Prints the final inventory report.

    print("\n--- Inventory Report ---")
    print("Total Deliveries Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)

#Added in week4
# Saves the inventory total and transaction history into inventory.txt file
def save_inventory(total_inventory, transaction_history):
        with open("inventory.txt", "w") as file:
            file.write(str(total_inventory) + "\n")

            history_text = ",".join(str(value) for value in transaction_history)
            file.write(history_text)


def main():
    #Main function to run inventory auditor program.
    
    # Load previous data
    inventory, transaction_history = load_inventory()

    # Local variables
    failed_entries = 0
    deliveries_processed = 0
    exit_program = False

    print("Loaded inventory:", inventory)
    print("Transaction history:", transaction_history)

    while not exit_program:

        stock = get_valid_input()

        if stock == "quit":
            exit_program = True

        elif stock is None:
            failed_entries += 1

        else:
            inventory = process_delivery(inventory, stock)

            tax_amount = calculate_tax(stock)

            # Add valid transaction to history list
            transaction_history.append(stock)

            deliveries_processed += 1

            print("Current inventory:", inventory)
            print("Tax for this delivery:", f"{tax_amount:.2f}")

            if inventory > max_capacity:
                print("WARNING: Inventory has exceeded 500 units!!!")
                exit_program = True

    # Save data before program ends
    save_inventory(inventory, transaction_history)

    generate_report(deliveries_processed, failed_entries)

    print("Inventory saved successfully.")

main()