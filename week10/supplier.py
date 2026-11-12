class Supplier:
    """An independent business object associated with products."""

    def __init__(self, supplier_id: str, name: str, contact_email: str) -> None:
        if not all(value.strip() for value in (supplier_id, name, contact_email)):
            raise ValueError("Supplier ID, name and email cannot be empty.")
        self.__supplier_id: str = supplier_id.strip()
        self.__name: str = name.strip()
        self.__contact_email: str = contact_email.strip()

    def get_supplier_id(self) -> str:
        return self.__supplier_id

    def get_name(self) -> str:
        return self.__name

    def get_contact_email(self) -> str:
        return self.__contact_email

    def display_information(self) -> None:
        print(f"Supplier: {self.__supplier_id} | {self.__name} | {self.__contact_email}")
