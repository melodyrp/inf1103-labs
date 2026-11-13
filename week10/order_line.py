from product import Product


class OrderLine:
    """Internal order part: created and managed by an Order."""

    def __init__(self, product: Product, quantity: int) -> None:
        if type(quantity) is not int or quantity <= 0:
            raise ValueError("Order quantity must be a positive integer.")
        self.__product: Product = product
        self.__quantity: int = quantity

    def get_product(self) -> Product:
        return self.__product

    def get_quantity(self) -> int:
        return self.__quantity

    def calculate_subtotal(self) -> float:
        return self.__product.price * self.__quantity
