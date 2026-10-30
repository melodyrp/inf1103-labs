class Product:
    def __init__(self, product_id, name, price, stock):
        if not product_id.strip() or not name.strip():
            raise ValueError("Product ID and name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")

        self.__product_id = product_id.strip()
        self.__name = name.strip()
        self.__price = price
        self.update_stock(stock)

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def update_stock(self, quantity):
        if quantity < 0:
            raise ValueError("Stock cannot be negative.")
        self.__stock = quantity

    def display_information(self):
        print(
            f"ID: {self.__product_id} | "
            f"Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | "
            f"Stock: {self.__stock}"
        )



