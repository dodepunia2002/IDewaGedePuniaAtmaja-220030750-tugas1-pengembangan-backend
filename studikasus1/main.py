from models.address import Address
from models.student import Student
from models.professor import Professor

print("=== University System ===\n")

# 1. Create Address
address = Address(
    street="Jl Mawar",
    city="Denpasar",
    state="Bali",
    postal_code=80111,
    country="Indonesia",
)
print("Address:", address.output_as_label())

# 2. Create Student
student = Student(
    name="Budi",
    phone_number="08123456789",
    email_address="budi@gmail.com",
    student_number=123,
    average_mark=75,
)
print(
    f"\nStudent: {student.name} (#{student.student_number}) avg={student.average_mark}"
)
print("Eligible:", student.is_eligible_to_enroll("SomeCourse"))

# Assign address
student.address = address
print("Address assigned:", student.address.output_as_label())

# Purchase parking pass
print("Parking Pass:", student.purchase_parking_pass())

# 3. Create Professor
prof = Professor(
    name="Dr. Made",
    phone_number="089999123",
    email_address="made@gmail.com",
    staff_number=1,
    years_of_service=10,
    number_of_classes=3,
    salary=15000000,
)
print(f"\nProfessor: Professor {prof.name}")

# Supervise the student
prof.add_student(student)
print(f"Professor supervising {len(prof.supervised_students)} students")
print("Supervised Students:", [s.name for s in prof.supervised_students])
