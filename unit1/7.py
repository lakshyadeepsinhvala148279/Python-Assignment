#Python Program to Print the Fibonacci sequence
print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565003")

n = int(input("Enter the number: "))

a, b = 0, 1

print("Fibonacci Sequence:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
