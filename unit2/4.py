
print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565003")

def area_of_circle(radius):
    return 3.14159 * (radius ** 2)

def area_of_triangle(base, height):
    return 0.5 * base * height

def area_of_square(side):
    return side ** 2

def area_of_rectangle(length, width):
    return length * width

def area_of_trapezoid(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def interest(principal, rate, time):
    return (principal * rate * time) / 100



print("Circle Area (r=7):", area_of_circle(7))
print("Triangle Area (b=8, h=5):", area_of_triangle(8, 5))
print("Square Area (s=6):", area_of_square(6))
print("Area of Rectangle:", area_of_rectangle(10, 5))
print("Area of Trapezoid:", area_of_trapezoid(6, 10, 4))
print("Interest:", interest(1000, 5, 2))
