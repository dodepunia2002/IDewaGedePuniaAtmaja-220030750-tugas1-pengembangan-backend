from .person import Person

"""
Prompt
“Buatkan model person serta dokumentasi lengkap untuk class Student, termasuk docstring untuk class, atribut, dan\n
method dari studi kasus yang sudah ada”
"""


class Student(Person):
    """
    Represents a student in the university system. A student is a type of Person
    who has additional academic–related attributes such as student number,
    average mark, and tracking for seminar participation.

    Attributes:
        student_number (int): Unique identifier assigned to the student.
        average_mark (int): The student's overall academic performance score.
        seminars_taken (int): Counter for the number of seminars the student has attended.

    Methods:
        is_eligible_to_enroll(course: str) -> bool:
            Determines whether the student is eligible to enroll in a course based
            on the minimum required average mark.

        get_seminars_taken() -> int:
            Returns the total number of seminars the student has participated in.
    """

    def __init__(
        self,
        name,
        phone_number,
        email_address,
        student_number: int,
        average_mark: int,
        address=None,
    ):
        """
        Initializes a new Student instance.

        Args:
            name (str): Full name of the student.
            phone_number (str): Contact phone number.
            email_address (str): Email address for communication.
            student_number (int): Unique ID assigned to the student.
            average_mark (int): Student's average grade score.
            address (Address, optional): Residential address. Defaults to None.
        """
        super().__init__(name, phone_number, email_address, address)
        self.student_number = student_number
        self.average_mark = average_mark
        self.seminars_taken = 0

    def is_eligible_to_enroll(self, course: str) -> bool:
        """
        Checks if the student is eligible to enroll in the given course.

        Args:
            course (str): The course the student intends to enroll in.

        Returns:
            bool: True if average_mark >= 60, otherwise False.
        """
        return self.average_mark >= 60

    def get_seminars_taken(self) -> int:
        """
        Retrieves the number of seminars the student has attended.

        Returns:
            int: Total seminars taken.
        """
        return self.seminars_taken
