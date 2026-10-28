"""Association: A teacher teaches a student; both exist independently."""
class Student:
    def __init__(self, name):
        self.name = name

class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self, student):
        print(f"{self.name} teaches {student.name}.")

if __name__ == '__main__':
    teacher = Teacher('Ms. Cruz')
    student = Student('Alex')
    teacher.teach(student)
