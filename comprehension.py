'''
#Without Uisng Comprehension
myList=[]
for el in range(10):
    myList.append(el**2)
print(myList)


#Using Comprehension
#Sntax
newList=[expression for item in iterable if condition==True]

#List Comprehension

myList=[]
newList=[el**2 for el in range(1,11) if el%2 ==0 ]
print(newList)

#Set Comprehension
Syntax:
newSet={expression for element in iterable}

#Without using comprehension

myset=set()
mylist=[1,2,3,4,5,6,7,8,9,10]
for el in mylist:
    myset.add(el*5) 
print(myset)

#Using comprehension
mylist=[1,2,3,4,5,6,7,8,9,10]
newset={el*5 for el in mylist}
print(newset)


#Dictionary Comprehension
#Syntax:

myDict={key:value for var in iterable}

myList=[1,2,3,4,5,6]
myDict={x:x**3 for x in myList}
print(myDict)

'''

myDict1={1:1,2:2,3:3,4:4,5:5,6:6}
myDict2={x:x**3 for x in myDict1 if x%2==0 }
print(myDict2)


