class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print("Name is ",self.name)
        print("Age is ",self.age)

ob1=A("Lakshyadeep",21)
ob1.show()
