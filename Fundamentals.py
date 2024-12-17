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
        if weight > 50:
            print(f"{user} is eligible in military with weight {weight}")
        else:
            print(f"{user} is not eligible in military with weight {we1 - weight}")
    else:   
        print(f"{user} is not eligible in military with age { ag1 - age}")        