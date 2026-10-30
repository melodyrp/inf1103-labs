class Inventory:
    
    def __init__(self):
        self.__products = []

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def add_product(self, product):
        if self.search_product(product.get_product_id()) is not None:
            return False
        self.__products.append(product)
        return True

    def update_stock(self, product_id, new_stock):
        product = self.search_product(product_id)
        if product is None:
            return False
        product.update_stock(new_stock)
        return True

    def display_all(self):
        print("\nCurrent Inventory")
        print("------------------------------------------------")
        if not self.__products:
            print("No products found.")
        else:
            for product in self.__products:
                product.display_information()
        print("------------------------------------------------")

    def get_products(self):
        # Return a copy of the list so callers cannot append to our private list.
        return self.__products.copy()