class Author:
    """
    Represents an author with a name and year of birth. This class provides
    functionality to calculate the author's age given the current year.

    Attributes:
        name (str): The full name of the author.
        birth_year (int): The year the author was born.

    Methods:
        get_age(current_year: int) -> int:
            Calculates and returns the author's age based on the current year.
    """

    def __init__(self, name: str, birth_year: int):
        """
        Initializes a new Author instance.

        Args:
            name (str): Full name of the author.
            birth_year (int): Year of birth of the author.
        """
        self.name = name
        self.birth_year = birth_year

    def get_age(self, current_year: int) -> int:
        """
        Calculates the current age of the author.

        Args:
            current_year (int): The current year to use for age calculation.

        Returns:
            int: The author's age based on the current year.
        """
        return current_year - self.birth_year
