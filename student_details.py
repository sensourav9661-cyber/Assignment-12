
class Student:
    def __init__(self, name, roll_number, course):
        self.name = name
        self.roll_number = roll_number
        self.course = course

    def display_details(self):
        print("Student Details")
        print("----------------")
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Course:", self.course)


student = Student("Sourav Sen", 101, "Computer Science")
student.display_details()
