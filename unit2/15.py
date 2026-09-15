print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565003")


# 1. Positional Arguments
def area(w, h):
    return w * h

# 2. Default Arguments
def greet(name, msg="Hello"):
    print(f"{msg}, {name}!")

# 3. Keyword Arguments
def student_info(name, age):
    print(f"Name: {name}, Age: {age}")

# 4. Variable-length Positional Arguments (*args)
def add_all(*numbers):
    print("Sum:", sum(numbers))

# 5. Variable-length Keyword Arguments (**kwargs)
def print_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

# Main Execution
print(" Student Enrolment No: 92600565003 ")
print(" Name: Lakshyadeepsinh\n")

# Demonstrating function calls
print("Area:", area(5, 10))
greet("Lakshyadeepsinh")
student_info(age=22, name="Lakshyadeepsinh")
add_all(10, 20, 30)
print_details(Role="Student", City="Rajkot")
