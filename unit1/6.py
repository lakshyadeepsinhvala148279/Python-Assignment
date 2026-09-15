#Python Program to Find the Factorial of a Number
print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565003")
num = int(input('enter a num'))
factorial=1


if num<0:
    print("factorial is not defind")

else:
    for i in range (1,num+1):
        factorial*=i
    print("factorial of",num,"is",factorial)
    
