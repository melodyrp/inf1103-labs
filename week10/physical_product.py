from math import isfinite

from can_be_shipped import CanBeShipped
from product import Product
from supplier import Supplier


class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 weight: float | None, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        # Preserve Week 9 support for old records with no recorded weight.
        if weight is not None and (not isfinite(weight) or weight < 0):
            raise ValueError("Weight must be finite and non-negative.")
        self.weight: float | None = weight

    def display_information(self) -> None:
        super().display_information()
        if self.weight is None:
            print("  Weight: Unknown | Shipping cost: Unavailable")
        else:
            print(f"  Weight: {self.weight:g} kg | "
                  f"Shipping cost: ${self.calculate_shipping_cost():.2f}")

    def get_fulfilment_info(self) -> str:
        return "Requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        if self.weight is None:
            raise ValueError("Shipping cost requires a known weight.")
        return 5.0 + 2.0 * self.weight
