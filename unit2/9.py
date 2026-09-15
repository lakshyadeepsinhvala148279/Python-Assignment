print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565003")


class Student:
    # Constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Method 1: Display student details
    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

    # Method 2: Calculate grade based on marks
    def get_grade(self):
        if self.marks >= 80:
            return "A"
        elif self.marks >= 60:
            return "B"
        else:
            return "C"

# Main Execution
print("Student Enrolment No: 92600565003")
print("Name: Lakshyadeepsinh \n")

# Creating an instance of the class
student1 = Student("Lakshyadeepsinh", 85)

# Calling instance methods
student1.display_info()
print("Grade:", student1.get_grade())
