class LibraryItem:
    """
    Represents a generic item in a library. Each library item has a unique ID
    and a title. Provides methods to display information and calculate late fees.

    Attributes:
        item_id (int): Unique identifier for the library item.
        title (str): Title of the library item.

    Methods:
        display_info() -> None:
            Prints the ID and title of the library item.

        calculate_late_fee(days_late: int) -> float:
            Calculates the late fee for returning the item past its due date.
    """

    def __init__(self, item_id: int, title: str):
        """
        Initializes a new LibraryItem instance.

        Args:
            item_id (int): Unique identifier for the library item.
            title (str): Title of the library item.
        """
        self.item_id = item_id
        self.title = title

    def display_info(self) -> None:
        """
        Displays information about the library item.

        Prints:
            A formatted string showing the item's ID and title.
        """
        print(f"[LibraryItem] #{self.item_id} - {self.title}")

    def calculate_late_fee(self, days_late: int) -> float:
        """
        Calculates the late fee for returning the item late.

        Args:
            days_late (int): Number of days the item is returned past the due date.

        Returns:
            float: Total late fee, calculated as 1.0 per day late.
        """
        return days_late * 1.0
