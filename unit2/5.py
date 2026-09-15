#positional arguments

def student(name,age):
    print("Name:",name)
    print("Age:",age)

student("Lakshyadeepsinh",21)

#keyword arguments

student(name="Lakshyadeepsinh",age=21)


#Default arguments
def greet(name="student"):
     print("Hello",name)
greet()
greet("lucky")

#Variable-length arguments
def total(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n
    print("Toatal =",sum)

total(10,20)
total(10,20,30,40)
