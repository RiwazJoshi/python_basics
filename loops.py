"""
#While loop

# count=1
# while (count<=100):
#     print(count)
#     count+=1



# i=100
# while i>=1:
#     print(i)
#     i-=1


num=int(input("Enter a number to find the multipliction table of: "))
# num=9
i=1
while i<=10:
    table=num*i
    # print(table)
    print(num,"X",i,"=",table)
    i+=1

    
num=[1,4,9,16,25,36,49,64,81,100]
i=0

while i<=(len(num)-1):
    # print(num,i)
    print(num[i])
    i+=1


num=(1,4,9,16,25,36,49,64,81,100)
i=0

x=int(input("Enter the number to be searched: "))
while i<len(num):
    if(x==num[i]):
        print("Number found at index",i)
        break
    i+=1
else:
    print("Number is not in the list")


i=0
while(i<=5):
    if(i==2):
        i+=1
        continue
    print(i)
    i+=1

#For loop

nums=[1,2,3,4,5]
for el in nums:
    print(el)


names=["Ram","Hari","Sita"]
for value in names:
    print(value)
else:
    print("End")


nums=[1,4,9,16,25,36,49,64,81,100]
for val in nums:
    print(val)


nums=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter the number to search: "))
i=0
for val in nums:
    if val==x:
        print("Number",val,"Found ai index",i)
        break
    i+=1
else:
    print("Number is not in the tuple")


#Range()
 
for i in range(10): #range(stop)
    print(i)

for i in range(100,0,-1): #range(start,stop)
    print(i)

for i in range(2,10,2): #range(start,stop,step size)
    print(i)


n=int(input("Enter a number: "))

for el in range(1,11):
    table=n*el
    print (n,"X",el,"=",table)


#pass -used to skik the process and keep it null, usually used as a placeholder for future code
for el in range(10):
    pass
print("loop ended")

#WAP to find the sum of first n numbers

num=int(input("Enter the number to find sum upto that number: "))
i=0
sum=0
while(i<=num):

    sum=sum+i
    i+=1
print(sum)
n=int(input("Enter a number: "))

sum=0
for el in range(1,n+1):
    sum=sum+el
print(sum)    





#WAP to  find the facorial of first n numbers

n=int(input("Enter number: "))
fact=1
for el in range(1,n+1):
    fact=fact*el
print(fact)
"""

n=int(input("Enter a number: "))
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print (fact)



