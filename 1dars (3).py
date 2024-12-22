class Student:
    def __init__(self, first_name, last_name, age, card_number, student):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.card_number = card_number
        self.student = student
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    @property
    def about(self):
        return f"I am {self.full_name}, I am {self.student}, I am {self.age}, I have {self.card_number} numbered in the student card"
student = Student('Brave', 'To\'lqinov', 22, 123456, 'student')
print(student.about)
