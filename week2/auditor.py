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
