
'''

def calc_sum(a,b):
    return a+b

sum=calc_sum(10,2)
print(sum)


def sayHello():
    print("Hello")

sayHello()


#Average of three numbers

def showAvg(a,b,c):
    return (a+b+c)/3
a=int(input("Enter a number A: "))
b=int(input("Enter a number B: "))
c=int(input("Enter a number C: "))

average=showAvg(a,b,c)
print(average)


a=[5,10,15,20,30,40]
print(len(a))


def printList(a=[5,10,20,40,50,20,50]):
    for el in a :
     print(el)



printList()


f=1
def fact(n):
    global f
    for el in range(1,n+1):
        f=f*el
    return f
    
factorial = fact(6)
print(factorial)

#WAP to print the length of list using functions

fruits=["Mango","Apple","Banana","Pear"]
vegetable=["potato","tomato","carrot"]

def print_length(a):
    print(len(a))

print_length(fruits)
print_length(vegetable)


fruits=["Mango","Apple","Banana","Pear"]
vegetable=["potato","tomato","carrot"]

def print_length(a):
    for el in a:
        print(el, end=" ")

print_length(fruits)
# print_length(vegetable)

#WAP to convert USD to NRS

def conversion(val):
    amount=val*130
    return amount

n=(int(input("Enter the amount to be converted: ")))
converted=(conversion(n))
print(converted)

#WAP to find odd or even

def oddEven(n):
    if(n%2==0):
        return "Even"
    else:
        return"Odd"
    
print(oddEven(6))

#recursion


def show(n):
    if(n==0):
        return
    print (n)
    show(n-1)
    print("End")

show(5)        


def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(5))


def find_sum(n):
    if n<=0:
        return
    if n==1:
        return 1 
    else:
        sum=n+find_sum(n-1)
        return sum
    
print (find_sum(6))


# i=1 
# n=5
# sum=0
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)

def printList(a,i=0):
    if(i==len(a)):
        return
    print(a[i])
    printList(a,i+1)

list=[10,20,30,40,50,60]
printList(list)

#Udemy
def fact(n):
    fact=1
    for el in range(1,n+1):
        fact*=el
    return fact
    # print(f"Factorial of {n} is {fact}")
b=int(input("Enter a number: "))
# print(f"Factorial of {b} is {fact(b)}")
factorial=fact(b)
print(f"Factorial of {b} is {factorial}")
# Generally don't use print inside a function rathe use return statement


def sqrt(n):
    res=n**(1/2)
    return res

a=int(input("Enter a Number: "))
square_root=sqrt(a)
print(f"Square Root of {a} is: {square_root}")


#There are two types of variable in python
Local:Declared inside the function, these variables ca be accessed locally
Global:Declared Outside the function, can be accessed anywhere


g_lang='python programming language'
def demo1():
    l_lang="java programming language"
    print(g_lang)
    print(l_lang)

    
demo1()

#global keyword is used to make local variable global


#types of arguments
There are four types of argument
1. Positional Arguments 

def add_num(n1,n2,n3):
    sum=n1+n2+n3
    return sum
print(add_num(10,20,03))
 so 10 will be passed to n1, 20 to n2 and 03 to n3 
This is called positional argument

#2. Keyword Arguments

def greet(name,surname):
    print("hello",name,surname)

greet(surname="Kapoor",name="Ram")
Here the value of name wiil be passsed to name and value of surname 
will be passed to surname requardless of their calling position 


# 3. Default Arguments
def add_num(n1=5,n2=5):
    sum=n1+n2
    return sum
print(add_num(6,6))
If you pass default argument and do not pass any arguments when 
calling function the function doesnt return error and uses the defalut 
values if you pass argument it will overwrite the deault argument and use the passed argument

#4. Variable length Arguments
when we have to use n number of arguments we use variable length arguments


def addNum(*nums):
    total=sum(nums)
    return total
print(addNum(10,20,30,40,50,60,70,80))

'''
# Fibonacci using recursive

 



