from models.author import Author
from models.book import Book
from models.member import LibraryMember

print("=== Library System (Studi Kasus 2) ===\n")

# Create Author
author1 = Author("Tere Liye", 1979)

# Create Book
book1 = Book("ISBN12345", "Bumi", author1)

# Create Member
member1 = LibraryMember(1, "Eka")

# Display Book Info
book1.display_info()
print(f"Author Age (2025): {author1.get_age(2025)}\n")

# Borrow Process
member1.borrow_item(book1)
print(f"Late Fee (3 days): {book1.calculate_late_fee(3)}\n")

# Return Process
member1.return_item(book1)
