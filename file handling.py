import os
"""
f=open("test.txt","r")
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
line3=f.readline()
print(line3)
print(type(line1))
f.close()

f=open("test1.txt","w")
f.write("Hello World")
f.close()


f=open("test1.txt","a")
f.write("\n This is a new line")
f.close()

r=read
w=write(removes all content and writes new content)
a=append(writes content at the end)
r+(writes content at the start)
w+(removes all content)
a+(erites cintent at the last)

#proper syntax

with open ("filename","mode") as f:
f.read()
print(f)


with open ("test.txt","r") as f:
    content=f.read()
    print(content)

os.remove("test1.txt")


with open("practice.txt","w") as f:
    f.write(
        "Hi everyone \n"
        "we are learning File I.O\n"
        "using java\n"
        "I like programming in java"
         
    )
    
with open("practice.txt","r+") as f:
  data=f.read()
  new_data=data.replace("java","Python")
  print(new_data)

with open("practice.txt","w") as f:
  f.write(new_data)
"""

with open("practice.txt","r") as f:
    data=f.read()
    print (data.find("learning"))
    # print(data)


