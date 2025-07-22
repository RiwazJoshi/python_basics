'''
Behaviour==methods
Attributes==variables




Syntax of creating class:

class <class_name>:
    attributes
    Behaviour

Syntax for creating objects:
obj=class_name([argumments])


#Creating Class
class Student:
    
    def __init__(self,name,roll,age):
      #initialization

        self.name=name
        self.roll=roll
        self.age=age

    def display(self):
        print("\nName: ",self.name)
        print("\nRoll Number:",self.roll)
        print('\nAge: ',self.age)

#Creating object

Std1=Student('Riwaz',115,21)
Std2=Student('Ram',114,20)

Std1.display()
Std2.display()


class Employee:
    def __init__(self,name,age,salary):  #__init__ is a constructor(USed to initialize attributes)
        self.name=name
        self.age=age
        self.salary=salary

    def diplay(self):
        print(f"\nEmployee name is : {self.name}")
        print(f"Employee age is : {self.age}")
        print(f"Employee salary  is : {self.salary}\n")

Emp1=Employee('ram',25,25000)
Emp2=Employee('shyam',29,29000)

Emp1.diplay()
Emp2.diplay()

class Employee:

    def __init__(self):
        self.Empid=99
        self.Salary=50000


obj1=Employee()
print(obj1.Empid)
print(obj1.Salary)
'''


class Student:
    def __init__(self,rno,name,age):
        self.rno=rno
        self.name=name
        self.age=age

    def display(self):
        print('Name is: ',self.name)
        print('Roll no: ',self.rno)
        print('Age is: ',self.age)

stu1=Student(111,'Ram',15)
# stu1.display()
# Built in function in oops

print(getattr(stu1,'age'))#get attribute value
setattr(stu1,'name','john')#modify value
print(getattr(stu1,'name'))
delattr(stu1,'age')#delete attribute
print(hasattr(stu1,'name'))#check if attribute is present