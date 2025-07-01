
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

'''
def printList(a,i=0):
    if(i==len(a)):
        return
    print(a[i])
    printList(a,i+1)

list=[10,20,30,40,50,60]
printList(list)