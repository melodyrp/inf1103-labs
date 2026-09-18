max_capacity = 500
tax_rate = 0.1 #10% tax rate

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


def main():
    """
    Main function to run inventory auditor program.
    """

    # local variables
    inventory = 0
    failed_entries = 0
    deliveries_processed = 0
    tax_amount = 0
    exit_program = False

    while not exit_program:

        stock = get_valid_input()
        # quit
        if stock == "exit":
            exit_program = True

main()