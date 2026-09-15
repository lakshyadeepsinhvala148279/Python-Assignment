
print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565003")
#class&objects
class MyNewClass:
    """This class demonstrates the creation of objects"""
    num=100
    def hello(self):
        print("hello word")
obj=MyNewClass()
print(obj.num)
obj.hello()
print(MyNewClass.__doc__)



class Employee:
    def __init__(self,name,id):
        self.id=id
        self.name=name

    def display(self):
        print(self.id,self.name)

emp1=Employee("john",101)
emp2=Employee("David",102)

emp1.display()
emp2.display()




class Student:
    def __init__(self):
        print("this is non parametrized constructor")
    def show(self,name):
        print("hello",name)

obj=Student()
obj.show("Lakshyadeepsinh")




        
