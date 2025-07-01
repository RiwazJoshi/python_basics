"""
#List are mutable(you can change it)
#Tuples are not mutable(you cannot change it)



marks=[10,20,30]
print(marks)
print(marks[0])
print(len(marks))

person=["Ram",18,"Teacher"]
name=person[0]
age=person[1]
job=person[2]
print("name is: ",name ,"\nage is: ",age, "\njob is: ", job )


marks=[10,20,30,40,50,60,70,80,90] #marks=[-9,-8,-7,-6,-5,-4,-3,-2,-1]
print(len(marks))
# print(marks[0:4])
print(marks[-5:-1])

#list methods

list=[1,3,5,2,6,4,7,7]
# list.append(8)
# list.sort()
# list.sort(reverse=1)
# print(list.count(7))
# list.reverse()
# list.insert(5,25) #list.insert(index,value)
# list.remove(7)
# list.pop(5)S
# list[1]=100
print(list)


#tuples
tup=(1,2,3,4,3)
print(tup)
print(type(tup))
# print(tup[3])
print(tup.index(4)) #prints in whinch index the element is stores
print(tup.count(3))

#WAP to ask user to enter three favourite movies and store them in a list

movie_name =[]
mov1=input("Enter the name of first movie: ")
mov2=input("Enter the name of second movie: ")
mov3=input("Enter the name of third movie: ")

movie_name.append(mov1)
movie_name.append(mov2)
movie_name.append(mov3)
print(movie_name)

movie=[]
mov=input("Enter movie name1: ")
movie.append(mov)
mov=input("Enter movie name2: ")
movie.append(mov)
mov=input("Enter movie name3: ")
movie.append(mov)

print(movie)



#WAP to check if a list contains a palindrom of elements

mylist=["My","name","is","name","My"]

list1=mylist.copy()
list1.reverse()
print(list1)
print(mylist)


if mylist==list1:
    print("Is Palindrom")
else:
    print("Not Palindrom")


Grade=("C","D","A","A","B","B","A")
print("Number of students with A grade are: ",Grade.count("A"))



#WAP to store above values in a list and sort them from A to D
grade=["C","D","A","A","B","B","A"]
grade.sort() #grade.sort(reverse=1) for decending
print("Sorted array is :",grade)
"""











































