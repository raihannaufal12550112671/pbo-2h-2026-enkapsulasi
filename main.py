from book import Book

b1 = Book(1234, "Learn Python", "Affan")
b2 = Book(4321, "Mastering OOP", "Budi")

print()
print(b1.get_title() + ", " + b1.get_author())
print(b2.get_title() + ", " + b2.get_author())

b1.set_title("Belajar Python Programming")
b2.set_title("Mastering Konsep OOP")

b1.set_author("Affandes")
b2.set_author("Budi Santoso")

print()
print(b1.get_title() + ", " + b1.get_author())
print(b2.get_title() + ", " + b2.get_author())
print()
