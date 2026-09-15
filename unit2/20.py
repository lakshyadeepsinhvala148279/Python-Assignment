print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565003")

class Calculator:
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b



print(" Student Enrolment No: 92600565003 ")
print(" Name: Lakshyadeepsinh \n")

calc = Calculator()

# Adding two numbers using add()
sum_two = calc.add(10, 20)
print("Sum of two numbers (10 + 20):", sum_two)

# Adding three numbers using the same add() method name
sum_three = calc.add(10, 20, 30)
print("Sum of three numbers (10 + 20 + 30):", sum_three)
