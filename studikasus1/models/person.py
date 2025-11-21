from .address import Address

"""
Prompt
“Buatkan model person serta dokumentasi lengkap untuk class Person, termasuk docstring untuk class, atribut, dan\n
method dari studi kasus yang sudah ada”
"""


class Person:
    """
    Represents a general person in the university system, such as a Student or Professor.

    Attributes:
        name (str): The full name of the person.
        phone_number (str): Contact phone number.
        email_address (str): Email address used for communication.
        address (Address | None): Optional physical address associated with the person.

    Methods:
        purchase_parking_pass() -> str:
            Simulates purchasing a parking pass and returns a confirmation message.
    """

    def __init__(
        self, name: str, phone_number: str, email_address: str, address: Address = None
    ):
        """
        Initializes a new Person instance.

        Args:
            name (str): The full name of the person.
            phone_number (str): The contact phone number.
            email_address (str): The person's email address.
            address (Address, optional): An Address instance representing the person's location.
                                         Defaults to None.
        """
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address
        self.address = address

    def purchase_parking_pass(self):
        """
        Creates a parking pass purchase confirmation.

        Returns:
            str: Confirmation message indicating the person has purchased a parking pass.
        """
        return f"{self.name} purchased a parking pass."
