'''
# Palindrome number
n=int(input("Enter a number: "))
# count=len(str(n))
original=n
reversed=0
while(n>0):
    digit=n%10
    # print(digit)
    reversed=reversed*10+digit
    n//=10
if original==reversed:
    print("Number is palindrome")
else:
    print("Number is not palindrome")

# Sum of n numbers

n=int(input("Enter a number: "))
sum=0
while(n>0):
    sum+=n
    n-=1
print(f"Sum of {n} numbers is {sum}")


#Factorial of a given number

n=int(input("Enter a number: "))
original=n
fact=1
while(n>0):
    fact*=n
    n-=1
print(f"Factorial of {original} is: {fact}")


#Print Tables of a given number
num=int(input("Enter a number: "))
i=1
while(i<=10):
    table=num*i
    print(f"{num} X {i} = {table}")
    i+=1

#Fibonacci Series
terms=int(input("Enter the number of terms you want to print: "))
a=0
b=1
while(terms>0):
    print(a, end=" ")
    c=a+b
    a=b
    b=c
    terms-=1


#Armstrong Numbers
n=int(input("Enter a number: "))
original=n
count=len(str(n))
sum=0
while(n>0):
    digit=n%10
    sum+=digit**count
    n//=10
if original== sum:
    print(f"{original} is a armstrong number")
else:
    print(f"{original} is not a armstrong number")

# for loop
for el in range(10,0,-1):
    print(el, end= " ")

#Factorial using For Loop
n=int(input("Enter the number: "))
fact=1
for el in range(1,n+1):
    fact*=el
print(f"Factorial is {fact}")

# For Loop
for el in range(5,0,-1):
    print('*'*el)

for el in range(6):
    for i in range(el):
        print(i, end=" ")
    print()

    
for el in range(6,0,-1):
    for i in range(el):
        print(chr(i+65),end=" ")
    print()


#Prime Numbers
n=int(input("Enter a number: "))
count=0
for el in range(2,n):
    if n%el==0:
       count+=1
if count>=1:
     print(f"{n} is not prime")
else:
    print(f"{n} is prime")
'''

#Print prime numbers from 1 to 100
prime_count=0
for el in range(1,200):
    count=0
    num=el
    for i in range(2,num):
        if num%i==0:
            count+=1
    if count<1:
        prime_count+=1
        print(num, end=",")
print(f"\nNumbers of Prime from 1 to 200 is {prime_count}\n")

