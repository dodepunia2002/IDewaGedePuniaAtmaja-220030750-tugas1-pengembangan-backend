class LibraryMember:
    """
    Represents a member of the library. Each member has a unique ID, a name,
    and a list of items they have borrowed. Provides methods to borrow and
    return library items.

    Attributes:
        member_id (int): Unique identifier for the library member.
        name (str): Name of the library member.
        borrowed_items (list): List of LibraryItem objects the member has borrowed.

    Methods:
        borrow_item(item) -> None:
            Adds a library item to the member's borrowed items and prints a confirmation.

        return_item(item) -> None:
            Removes a library item from the member's borrowed items and prints a confirmation.
            If the item was not borrowed, prints a warning message.
    """

    def __init__(self, member_id: int, name: str):
        """
        Initializes a new LibraryMember instance.

        Args:
            member_id (int): Unique identifier for the library member.
            name (str): Full name of the library member.
        """
        self.member_id = member_id
        self.name = name
        self.borrowed_items = []

    def borrow_item(self, item) -> None:
        """
        Borrows a library item by adding it to the member's borrowed items.

        Args:
            item (LibraryItem): The library item to borrow.

        Prints:
            A confirmation message indicating the item has been borrowed.
        """
        self.borrowed_items.append(item)
        print(f"{self.name} borrowed '{item.title}'")

    def return_item(self, item) -> None:
        """
        Returns a library item by removing it from the member's borrowed items.

        Args:
            item (LibraryItem): The library item to return.

        Prints:
            A confirmation message if the item is successfully returned.
            A warning message if the item was not borrowed by the member.
        """
        if item in self.borrowed_items:
            self.borrowed_items.remove(item)
            print(f"{self.name} returned '{item.title}'")
        else:
            print(f"{item.title} was not borrowed by {self.name}")
