
"""
#Dictionaries

student={
    "name":"John Doe",
    "age":29,
    "subjects":["Python","C","C++"]


}
print(student["name"])
student["name"]="Bob "
student["lastname"]="Doe"
print(student["name"])
print(student["lastname"])

#Nested Dictionary



student={
    "name":"Ram",
    "age":18,
    "subject": {
        "Maths":70,
        "Physics":90,
        "Chemistry":68
    }
}

print(student)
print(student["name"])
print(student["subject"])
print(student["subject"]["Chemistry"])


cars={
    "name":"Suzuki",
    "model":{
        "A1":2009,
        "A2":2005,
        "B1":2010
    },
    "colors":["Black","White","Grey"]
}
# print(cars.keys())
# print(cars["model"].keys())

# print(list(cars))
# print(list((cars).keys()))

# print(cars.values())
# pairs=list(cars.items())
# print(pairs[0])


# print(cars.get("model"))#returns none and doesnt give error if given key is not present

cars.update({"Dealerships":{

"Kathmandu Cars":444400000,
"Pokhara Jeeps":100000000}})
print(cars)


#Sets

collection={1,2,5,4,3,2,1,"World","hello","Hello","World"}
print(len(collection))
print(collection)

coll=set()#syntax to create enpty set
coll.add(1)
coll.add("hello")
coll.add((1,2,3))
coll.add("World")
print(coll)
coll.remove("World")
print(coll)

print(coll.pop())


print(coll)
coll.clear()
print(len(coll))


set1={1,3,4,6}
set2={1,2,3,4,5}

set3= set1.union(set2)
print(set1.intersection(set2))
print(set3)



#Questions
# Store word and meaning in python dictionary

WordMeaning={
    "table:":["a table of furniture","list of facts & figures"],
    "cat: ":"a small animal"
}

print(WordMeaning)


subjects={"python","java","C++","python","javascript","java","python","java","C++","C"}
print("Number of classes required is: ",len(subjects))


#WAP to enter marks of 3 subjects from user and store them in a dictionary.Start with an empty dictionary and add one by one. Use subject name as key and marks as value

marks={}

x=int(input("Enter the marks  of x-subject: "))
marks.update({"Physics: ": x})

y=int((input("Enter the marks of y-subject: ")))
marks.update({"Chemistry":y})

print(marks)

"""

#Store 9 and 9.0 as seperate values in a set

num=set()

num.add(9)
num.add(str(9.0))
print(num)

