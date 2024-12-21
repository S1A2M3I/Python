#Python
#------------------- 
#In Compiler and Interpreter Parser is used to check the syntax of the 
# program
#In Compiler Parser is used to check the semantic of the program
#Python is a high-level, interpreted, general-purpose programming language.
#General-Purpose Programming Language which is used for Mobile  
# Application, Web Application, Desktop Application, Data Analysism, #Machine Learning, and Data Science.
#For Mobile Application Development Kiwi
#For Web Application Development Django, Flask, Bottle, FastAPI
#For Desktop Application Development Tkinter, PYQT
#For Data Analysism Pandas, Numpy, Matplotlib
#For Machine Learning Scikit-learn
#For Data Science Numpy, Pandas, Matplotlib, Scikit-learn



#in-built functions in python
#input(): It is used to take input from the user.
name = input("Enter your name: ")

# print(): It is used to print the output on the screen.
print(name)

#type(): It is used to check the data type of the variable.
print(type(name))

#Identifiers are used to name the variables, functions, classes, modules.

#Single Valued data type
#int
#float
#bool
#str
#complex is a data type which is used to store complex number

complex = 3+4j
print(complex)


#Data Types
#int
#float
#bool
#str - "", '', """ """
#list - [], list()
#tuple - (), tuple()
#dict - {"key": "value"}, dict()
#set - {}, set()
#In Set it can have "", '', ''' '''
#''' is docstring which is used to document the code in python 

name = input("Enter your name: ")
elgaf = 21
age = int(input("Enter your age: "))

if age >= 21 and age <=90:
        weight = float(input("Enter your weight: "))
        if weight >= 50:
            print (f"{name} is eligible to donate blood")
else:
    print (f"{name} is not eligible to donate blood, then you have to wait at age {elgaf-age} years")
    
    
    #Online GDB Compiler 
    #https://www.onlinegdb.com/online_python_compiler
    
    # for i in range(1,100):
    #     print(i)
        
    # i = 1
    # while i <= 100:
    #     print(i)
    #     i += 1
    
    
    num = int(input("Enter a number: "))
    for i in range(1,11):
        print(num, "*", i, "=",num*i)

    rev = 11
    while rev > 1:
        rev = rev - 1
        mul = num * rev
        print(num ,"*",rev, "=",mul )
    
    # python was developed by Guido van Rossum in 1989

    user = input("Enter your name: ")
    age = int(input("Enter your age: "))
    we1 = 50
    ag1 = 16
    if age > 16 and age < 30:
        weight = float(input("Enter your weight: "))
        if weight > 50 and weight < 80:
            print(f"{user} is eligible in military with weight {weight}")
        else:
            print(f"{user} is not eligible in military need weight {we1 - weight} kg more")
    else:   
        print(f"{user} is not eligible in military with age { ag1 - age} years more")        
        
    
    

#Ascii Value
#A = 65
#Z = 90
# a = 97
# z = 122

#Slicing of String
name = "John Smith"
print(name[0:3])
print(name[:3])
print(name[1:3])
print(name[1:])
print(name[-3:-1])
print(name[0::2])#step size is 2
print(name[::2])

#match case
name = "John Smith"
print(name.upper())
print(name.lower())
print(name.title())


#Grade
name = input("Enter your name: ")
percentage = int(input("Enter your percentage: "))
if percentage >= 90 :
    print(f"{name} your grade is A")
elif percentage >= 80 and percentage < 90:
    print(f"{name} your grade is B")
elif percentage >= 70 and percentage < 80:
    print(f"{name} your grade is C")
elif percentage >= 60 and percentage < 70:
    print(f"{name} your grade is D")
else:
    print(f"{name} your grade is F")
    
    
    
    
while True:
    num10 = int(input("Enter a number: "))
    if num10 % 2 == 0:
        print(f"{num10} is even")
    else:
        print(f"{num10} is odd")
        break
            
            
#Range 
li = list(range(1,101))
print(li)
li1 = list(range(0,101,2)) #step size is 2 and to get even numbers
print(li1)
li2 = list(range(1,101,2)) #step size is 2 and to get odd numbers
print(li2)


# list functions
print(li.count(2))
print(li.index(2))
print(li.reverse())
print(li.sort())
print(li.append(102))
print(li.insert(0, 100))
print(li.pop(0))
print(li.remove(2))
print(li.clear())
print(li.copy())
print(li.extend([100,101,102]))


str = "Susan hello how are you"
print(str.title())


#For Loop 
li = ["Susan", "John", "Smith"]
for i in range(len(li)):
    print(f"Hi {li[i]} ...... nice to meet you")
    
    
#Single line Conditions 
name = "Susan"
print("yes" if name == "Susan" else "no")

#ternary operator
num = 10
num1 = 20
print(num1 if num > num1 else num)

#git is a version control system
#github is a cloud based version control system

#Virtual Environment is a seperate copy of python interpreter.
#OnlineGDB is a online compiler for python which is Virtual Environment.

nam1 = "John Smith"
print(nam1.rfind("S"))
print(nam1.find("S"))

age = 20
print("Hi {}, you are {} years old".format(nam1, age))

# print(nam1.find("a"))

#user wants to vote using single line if else statement 
us1 = input("Enter your name ")
age = int(input("Enter your age "))
print("yes" if age >= 18 else "no")

na20 = ["John Smith", "John Doe", "John Doe", "John Doe", "John Doe"]
for i in na20:
    for j in i:
        print (j)
        

#nested list 
li = [["John", "Smith"], ["Sussan"], ["John", "Doe"]]
# print(li[0][0])

for i in range(1,101):
    print(i)
    if i == 15:
        break

#break take exit out of the loop
#exit takes exit out of the loop and exit the program
#continue takes you to the next iteration

li9 = len(li) - 1
while li9>=0:
    print(li[li9])
    li9 -= 1
    
#types of databases 
#relational database
#non-relational database

fruits = ["apple","banana","watermelon","cherry"]
for i in range(0,len(fruits)):
    print(f"{i+1}.{fruits[i]} and length is - {len(fruits[i])}")
    


#Exception Handling
#try, except, else, finally
try:
    num = 10 / 0
    print(num)
except ZeroDivisionError:
    print("ZeroDivisionError is raised when you try to divide a number by zero")
else:
    print("This will be printed if there is no exception")
finally:
    print("This will be printed whether there is an exception or not")
    
    
#Exception Handling is used to handle the errors in the program if not handled then 
# it will crash the program
# # ValueError is raised when a function or method receives an argument of the wrong 
# # type, and it cannot be performed with that argument.
# age = int(input("Enter your age: "))
# # if age is not a number then ValueError will be raised

# # IndexError is raised when you try to access an index in a list that is out of range
# li = [1,2,3,4]
# print(li[5])

# # KeyError is raised when you try to access a key in a dictionary that does not exist
# d = {"name": "John", "age": 30, "city": "New York"}
# print(d["address"])

# # TypeError is raised when you try to perform an operation on an object of a 
# # different type than the expected type for that operation.
# num = 10
# print(num + "10")

# # ZeroDivisionError is raised when you try to divide a number by zero
# num = 10
# print(num/0)

# # IOError is raised when you try to read or write to a file that does not exist
# f = open("file.txt", "r")
# print(f.read())

# # AttributeError is raised when you try to access an attribute of an object that does 
# # not exist or is not accessible in that context 
# f = open("file.txt", "r")
# print(f.name)

# # ImportError is raised when you try to import a module that does not exist
# import module1

# # ModuleNotFoundError is raised when you try to import a module that does not exist
# import module1

# # NameError is raised when you try to access a variable that does not exist
# name = "John"
# print(name) 

# # SyntaxError is raised when you try to write Python code that is not valid
# print("Hello world"

# # ValueError is raised when you try to perform an operation on a value that is not valid
# num = 10
# print(num + "10")

