from .library_item import LibraryItem


class Book(LibraryItem):
    """
    Represents a book in the library system. A Book is a type of LibraryItem
    with an associated author and ISBN number. Provides methods for displaying
    book information and calculating late fees.

    Attributes:
        isbn (str): The International Standard Book Number for the book.
        author (Author): The author of the book.

    Methods:
        display_info() -> None:
            Prints detailed information about the book including ISBN, title, and author.

        calculate_late_fee(days_late: int) -> float:
            Calculates the late fee based on the number of overdue days.
    """

    def __init__(self, isbn: str, title: str, author):
        """
        Initializes a new Book instance.

        Args:
            isbn (str): Unique ISBN identifier for the book.
            title (str): Title of the book.
            author (Author): Author object representing the book's author.
        """
        super().__init__(item_id=isbn, title=title)
        self.isbn = isbn
        self.author = author

    def display_info(self) -> None:
        """
        Displays information about the book.

        Prints:
            A formatted string showing the book's ISBN, title, and author's name.
        """
        print(
            f"[Book] ISBN: {self.isbn}, Title: {self.title}, Author: {self.author.name}"
        )

    def calculate_late_fee(self, days_late: int) -> float:
        """
        Calculates the late fee for the book based on the number of days overdue.

        Args:
            days_late (int): Number of days the book is returned late.

        Returns:
            float: Total late fee, calculated as 1.5 per day late.
        """
        return days_late * 1.5
