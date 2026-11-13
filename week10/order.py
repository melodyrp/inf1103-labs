from order_line import OrderLine
from product import Product


class Order:
    """Owns order lines; callers receive value snapshots, never live lines."""

    def __init__(self, order_id: str) -> None:
        if not order_id.strip():
            raise ValueError("Order ID cannot be empty.")
        self.__order_id: str = order_id.strip()
        self.__order_lines: list[OrderLine] = []

    def get_order_id(self) -> str:
        return self.__order_id

    def add_order_line(self, product: Product, quantity: int) -> None:
        self.__order_lines.append(OrderLine(product, quantity))

    def remove_order_line(self, index: int) -> None:
        if index < 0 or index >= len(self.__order_lines):
            raise IndexError("Order line index is out of range.")
        del self.__order_lines[index]

    def get_order_lines(self) -> tuple[tuple[Product, int, float], ...]:
        return tuple((line.get_product(), line.get_quantity(),
                      line.calculate_subtotal()) for line in self.__order_lines)

    def calculate_total(self) -> float:
        return sum((line.calculate_subtotal() for line in self.__order_lines), 0.0)

    def cancel(self) -> None:
        """Remove all owned lines; referenced Products remain independent."""
        self.__order_lines.clear()
