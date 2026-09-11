inventory = 0
failed_entries = 0

while True:
    stock_input = input("Enter stock quantity (or 'exit' to exit): ")

    #exit
    if stock_input.lower() == "exit":
        print("\n--- Inventory Report ---")
        print("Number of Failed/Rejected Entries:", failed_entries)
        print("Number of Failed/Rejected Entries:", failed_entries)
        break

    # check for negative number
    if stock_input.startswith("-"):
        if stock_input[1:].isdigit():
            print("Error: Negative stock quantities are not allowed.")
            failed_entries += 1
            continue

    # check for invalid inputs
    if not stock_input.isdigit():
        print("Error: Invalid input. Please enter a valid stock quantity (Integer).")
        failed_entries += 1
        continue

    # convert input to integer
    stock = int(stock_input)

    # add stock to inventory
    inventory += stock

    print("Current inventory:", inventory)

    # Check storage limit
    if inventory > 500:
        print("WARNING: Inventory has exceeded 500 units!!!")
        break
    