from math import isfinite

from product import Product
from supplier import Supplier


class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 download_size: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        if not isfinite(download_size) or download_size < 0:
            raise ValueError("Download size must be finite and non-negative.")
        self.download_size: float = download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"  Download size: {self.download_size:g} MB")

    def get_fulfilment_info(self) -> str:
        return "Delivered digitally."
