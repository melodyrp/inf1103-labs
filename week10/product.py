from abc import ABC, abstractmethod
from math import isfinite

from supplier import Supplier


class Product(ABC):
    """Common contract: numeric price, non-negative stock, display and fulfilment."""

    def __init__(self, product_id: str, name: str, price: float,
                 stock: int, supplier: Supplier) -> None:
        if not product_id.strip() or not name.strip():
            raise ValueError("Product ID and name cannot be empty.")
        if not isfinite(price) or price < 0:
            raise ValueError("Price must be finite and non-negative.")
        self.__product_id: str = product_id.strip()
        self.__name: str = name.strip()
        self.__price: float = float(price)
        self.__supplier: Supplier = supplier
        self.__stock: int = 0
        self.update_stock(stock)

    def get_product_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    @property
    def price(self) -> float:
        return self.__price

    def get_stock(self) -> int:
        return self.__stock

    def get_supplier(self) -> Supplier:
        return self.__supplier

    def update_stock(self, quantity: int) -> None:
        """Set the absolute available quantity, including digital licences."""
        if type(quantity) is not int or quantity < 0:
            raise ValueError("Stock must be a non-negative integer.")
        self.__stock = quantity

    def display_information(self) -> None:
        print(f"ID: {self.__product_id} | Name: {self.__name} | "
              f"Price: ${self.__price:.2f} | Stock: {self.__stock}")
        self.__supplier.display_information()

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        """Return how this product is delivered."""
