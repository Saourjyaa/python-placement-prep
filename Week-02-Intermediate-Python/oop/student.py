class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def result(self):
        return "Pass" if self.marks >= 40 else "Fail"

    def display(self):
        return f"{self.roll_number}: {self.name} - {self.marks} ({self.result()})"


if __name__ == "__main__":
    for student in (Student("Aarav", 1, 82), Student("Mira", 2, 35)):
        print(student.display())
