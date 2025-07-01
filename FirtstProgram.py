'''name=input("Enter your name : ")
age=int(input("Enter your age: "))
marks=int(input("Enter your marks: "))

print("Welcome",name)
print("Age is", age)
print("Marks is", marks)

num1=int(input("enter a number: "))
num2=int(input("enter another number: "))
sum=num1+num2
print(sum)

side=int(input("Enter the length of one side of square: "))
print("Area of Square is: ",side ** 2)

num1=float(input ("Enter a number: "))
num2=float(input("Enter second number: "))
print("Average is: ",(num1+num2)/2)

a=int(input("Enter a number: "))
b=int(input("Enter second number: "))
#print(a>=b)
if a>=b:
    print("True")
else:
    print("False") 

##lecture 2
str1=("this is a pragraph\n this is new line")
print(str1)

str1=("This is ") 
str2=("a string")

print (str1+str2)
print(len(str1+str2))
str1=("Hello World")
ch=(str1[4])
print(ch) 

##SLicing
str=("Helloworld")
# print(str[0:5])
print(str[-4:-1])

#Functions 
# str= "hello world"
str="my name is john doe"
print(str.endswith('de'))

str="hello world, I live in this world"
#print(str.capitalize())
#print(str.replace("l","p"))
# print(str.replace("world","earth"))
# print(str.find("world"))
# print(str.count("world"))

name=input("Enter your name: ")
# print(name,"length of name is ", len(name))
name=name.capitalize()
print(name, name.count("R"))

#Conditionals
lightcolor= "green"
if lightcolor =="red":  
    print("Stop")     #statement for true is done after 4 spaces it is callef indentation
elif lightcolor=="yellow":
    print("Wait")
else:
    print("Go")


marks=int(input("Enter your marks: "))
if marks>=90:
    print("A")
elif marks>=80:
    print("B")
elif marks>=70:
    print("C")
else :
    print("Fail")


age=19
gender="female"
if age>=18:
    print("can vote")
    if gender=="male":
        print("Use line 1")
    else:
        print("Use line 2")
else:
    print("Cannot vote")        

    
num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
num3=int(input("Enter 3rd number: "))

if(num1>num2 and num1>num3):
    print("Num1 is greatest")
elif(num2>num1 and num2>num3):
    print("Num2 is greatesr")
else:
    print("Num3 is greatest")

'''
num=int(input("Enter a number: "))
if num%7==0:
    print("Is a multiple by 7")
else:
    print("Is not a multiple of seven")