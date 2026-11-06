from math import isfinite

from can_be_shipped import CanBeShipped
from product import Product


@CanBeShipped.register
class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        # Legacy physical products may have no recorded weight.
        if weight is not None and (not isfinite(weight) or weight < 0):
            raise ValueError("Weight must be a finite, non-negative number.")
        self.weight = weight

    def display_information(self):
        super().display_information()
        if self.weight is None:
            print("  Weight: Unknown | Shipping cost: Unavailable")
        else:
            print(f"  Weight: {self.weight:g} kg | Shipping cost: ${self.calculate_shipping_cost():.2f}")
        print(f"  Fulfilment: {self.get_fulfilment_info()}")

    def get_fulfilment_info(self):
        return "Requires physical shipping."

    def calculate_shipping_cost(self):
        if self.weight is None:
            raise ValueError("Shipping cost requires a known weight.")
        return 5 + 2 * self.weight
