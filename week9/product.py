from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        if not product_id.strip() or not name.strip():
            raise ValueError("Product ID and name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")

        self.__product_id = product_id.strip()
        self.__name = name.strip()
        self.__price = price
        self.update_stock(stock)

        