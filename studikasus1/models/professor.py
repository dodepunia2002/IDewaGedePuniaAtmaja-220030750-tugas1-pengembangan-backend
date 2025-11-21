from .person import Person
from .student import Student

"""
Prompt
“Buatkan model person serta dokumentasi lengkap untuk class Professor, termasuk docstring untuk class, atribut, dan\n
method dari studi kasus yang sudah ada”
"""


class Professor(Person):
    """
    Represents a professor in the university system. A professor is a type of Person
    who has additional attributes such as staff number, years of service, number of
    classes they teach, and salary. Professors may also supervise students.

    Attributes:
        staff_number (int): Unique identifier for the professor within the institution.
        years_of_service (int): Total years the professor has worked at the university.
        number_of_classes (int): Number of classes the professor is currently teaching.
        _salary (int): The private salary amount of the professor.
        supervised_students (list[Student]): A list of students supervised by the professor.

    Methods:
        add_student(student: Student):
            Adds a student to the professor's list of supervised students.
            Raises an exception if the limit of 5 supervisees is exceeded.

        get_salary() -> int:
            Retrieves the professor's salary.
    """

    def __init__(
        self,
        name,
        phone_number,
        email_address,
        staff_number: int,
        years_of_service: int,
        number_of_classes: int,
        salary: int,
        address=None,
    ):
        """
        Initializes a new Professor instance.

        Args:
            name (str): Full name of the professor.
            phone_number (str): Contact phone number.
            email_address (str): Email address for communication.
            staff_number (int): Unique staff ID number.
            years_of_service (int): Number of years employed at the university.
            number_of_classes (int): Total classes taught by the professor.
            salary (int): Salary of the professor.
            address (Address, optional): Physical address. Defaults to None.
        """
        super().__init__(name, phone_number, email_address, address)
        self._salary = salary
        self.staff_number = staff_number
        self.years_of_service = years_of_service
        self.number_of_classes = number_of_classes
        self.supervised_students = []

    def add_student(self, student: Student):
        """
        Assigns a student under the professor's supervision.

        Args:
            student (Student): The student to be supervised.

        Raises:
            Exception: If the professor already supervises 5 students.
        """
        if len(self.supervised_students) >= 5:
            raise Exception("Professor cannot supervise more than 5 students.")
        self.supervised_students.append(student)

    def get_salary(self):
        """
        Returns:
            int: The salary of the professor.
        """
        return self._salary
