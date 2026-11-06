from math import isfinite

from product import Product


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        if not isfinite(download_size) or download_size < 0:
            raise ValueError("Download size must be a finite, non-negative number.")
        self.download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"  Download size: {self.download_size:g} MB")
        print(f"  Fulfilment: {self.get_fulfilment_info()}")

    def get_fulfilment_info(self):
        return "Delivered digitally."
