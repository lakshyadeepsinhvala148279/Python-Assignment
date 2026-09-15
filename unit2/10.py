print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565003")

class Student:
    # Class Variable (Shared across all instances)
    college_name = "Marwadi University"

    def __init__(self, name, marks):
        # Instance Variables
        self.name = name
        self.marks = marks

    # 1. Instance Method (Works with instance attributes using 'self')
    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

    # 2. Class Method (Works with class attributes using 'cls')
    @classmethod
    def get_college(cls):
        print(f"College Name: {cls.college_name}")

    # 3. Static Method (Independent utility method, uses neither 'self' nor 'cls')
    @staticmethod
    def is_passing(marks):
        return marks >= 40


# Main Execution
print("=== Student Enrolment No: 92600565003 ===")
print("=== Name: Lakshyadeepsinh ===\n")

# Creating an instance
s1 = Student("Lakshyadeepsinh", 85)

# 1. Calling Instance Method
print("--- Instance Method ---")
s1.display_details()

# 2. Calling Class Method
print("\n--- Class Method ---")
Student.get_college()

# 3. Calling Static Method
print("\n--- Static Method ---")
result = Student.is_passing(s1.marks)
print(f"Is Student Passing? {result}")




