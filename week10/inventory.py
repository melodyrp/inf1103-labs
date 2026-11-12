from product import Product


class Inventory:
    """Aggregates independent Products; the same Product may be shared."""

    def __init__(self) -> None:
        self.__products: list[Product] = []

    @property
    def products(self) -> list[Product]:
        """A copy protects the collection while retaining Product identity."""
        return self.__products.copy()

    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def add_product(self, product: Product) -> None:
        if self.find_product(product.get_product_id()) is not None:
            raise ValueError("Product ID already exists in this inventory.")
        self.__products.append(product)

    def remove_product(self, product_id: str) -> None:
        product = self.find_product(product_id)
        if product is None:
            raise ValueError("Product not found.")
        self.__products.remove(product)

    def update_stock(self, product_id: str, new_stock: int) -> bool:
        product = self.find_product(product_id)
        if product is None:
            return False
        product.update_stock(new_stock)
        return True

    def display_all_products(self) -> None:
        print("\nCurrent Inventory")
        if not self.__products:
            print("No products found.")
        for product in self.__products:
            product.display_information()
            print(f"  Fulfilment: {product.get_fulfilment_info()}")

    # Keep the Week 9 public names available.
    def search_product(self, product_id: str) -> Product | None:
        return self.find_product(product_id)

    def display_all(self) -> None:
        self.display_all_products()

    def get_products(self) -> list[Product]:
        return self.products
