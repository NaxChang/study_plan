class Student:
    def __init__(self, name, age):
        assert 18 <= age <= 100, "Age must be between 18 and 100"
        self.name = name
        self.age = age


try:
    student1 = Student("Alice", 20)
    print(f"Name:{student1.name} ,Age:{student1.age}")
    student2 = Student("nameless", 120)
except AssertionError as e:
    print(f"AssertionError: {e}")
