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

