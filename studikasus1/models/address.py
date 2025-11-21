"""
Prompt
“Buatkan model person serta dokumentasi lengkap untuk class Address, termasuk docstring untuk class, atribut, dan\n
method dari studi kasus yang sudah ada”
"""


class Address:
    """
    Represents a physical mailing address for a person (Student or Professor).

    Attributes:
        street (str): The street name and number.
        city (str): The city where the address is located.
        state (str): The province or regional state.
        postal_code (int): The postal/ZIP code.
        country (str): The country name.

    Methods:
        validate() -> bool:
            Validates the address fields to ensure correct data types.
            Returns True only if all fields contain valid values.

        output_as_label() -> str:
            Generates a formatted address string suitable for display or printing.
    """

    def __init__(
        self, street: str, city: str, state: str, postal_code: int, country: str
    ):
        """
        Initializes a new Address instance.

        Args:
            street (str): Street information.
            city (str): City name.
            state (str): State/province.
            postal_code (int): Postal code.
            country (str): Country name.
        """
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country

    def validate(self) -> bool:
        """
        Validates the content of the address fields.

        Returns:
            bool: True if all fields have valid data types, else False.
        """
        return all(
            [
                isinstance(self.street, str),
                isinstance(self.city, str),
                isinstance(self.state, str),
                isinstance(self.country, str),
                isinstance(self.postal_code, int),
            ]
        )

    def output_as_label(self) -> str:
        """
        Formats the address into a readable, printable label.

        Returns:
            str: A formatted address string.
        """
        return f"{self.street}, {self.city}, {self.state} {self.postal_code}, {self.country}"
