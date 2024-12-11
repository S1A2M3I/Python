#Python is a programming language that lets you work quickly and integrate systems more effectively.
#It's a general-purpose language that lets you work with data, whether in the cloud or on-premises.
#Framework is a collection of tools and libraries that can be used to build applications.
#Framework for Python is the tkinter library which is used to build GUI applications.
#Python is a well intentended and standard language.
#Python is a high-level, interpreted, general-purpose programming language.
#Python is a high-level programming language that is interpreted, which means that the code is executed directly by the   
#interpreter.
#Inventory Managment System using python, tkinter library, and MySQL Database.
#in-built functions in python like print(), input(), etc.
#Opps and Procedural Programming Language difference between them.
#Procedural programming is a programming paradigm that uses a collection of functions to build a program.
#Opps programming is a programming paradigm that uses objects and their interactions to build a program.
#numpy and pandas are two popular libraries in Python for data analysis and manipulation.
#Pandas is a popular library for data manipulation and analysis in Python.
#Numpy is a popular library for numerical computing in Python.


print("Hello World")
print(True)
#ZeroDivisionError is a arithmetic exception which do not allow illegal mathematical 
#operations

# print(5/0)
#datatypes
#int
#float
#list 
#dictionary
#tuple
#set 
#string 
#boolean

#type of operators
#arithmetic operators
#comparison operators
#logical operators
#bitwise operators
#membership operators
#identity operators
#boolean operators

#arithmetic operators
#addition
#subtraction
#multiplication
#division
#modulus
#floor division
#exponent

num = 5
num1 = 4
print(num+num1)
print(num-num1)
print(num*num1)
print(num/num1)
print(num%num1)
print(num//num1)
print(num**num1)

#comparison operators
#equal to
#not equal to
#greater than
#less than  
#greater than or equal to
#less than or equal to
print(num==num1)
print(num!=num1)
print(num>num1)
print(num<num1)
print(num>=num1)
print(num<=num1)

#logical operators
#and
#or
#not
print(num>num1 and num>num1)
print(num>num1 or num>num1)
print(not(num>num1 or num>num1))

#bitwise operators
#and
#or
#not
#xor
#left shift
#right shift
print(num&num1)
print(num|num1)
print(~num)
print(num^num1)
print(num<<num1)
print(num>>num1)

name = input("Enter your name: ")
print("Name is :",name)

#Type Casting
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
print("Number is: ",num1+num2)

#literals in python are values that are directly assigned to a variable.
#literals are also called constants in python.
#literals in python are values that are directly assigned to a variable.

num1 = 10.5
print(int(num1))
print(type(num1))

num4 = int(input("Enter a number:"))
print("area :",num4**2)

#average
num5 = int(input("Enter a number:"))
num6 = int(input("Enter a number"))
num7 = int(input("Enter a number"))
print("average :",num5+num6+num7/3)

#to swap numbers using 3rd variable
a = 10
b = 20
c = a
a = b
b = c

print("a =", a)
print("b =", b)

#to swap two numbers using plus and minus
a = 10
b = 20
a = a + b
b = a - b
a = a - b

print("a =", a)
print("b =", b)

FirstName = "John"
LastName = "Smith"
print(FirstName,LastName)
print(FirstName+" "+LastName)
print(len(FirstName))

#Strings are immutable 
# str = "Susan"
# str1 = 'p'
# str1 = str[0]

#String Slicing 
str = "Susan"
print(str[0:3])
print(str[:3])
print(str[1:3])
print(str[1:])
print(str[-1:1])

#String Concatenation
str = "Susan"
str1 = 'p'
str2 = str+str1
print(str2)

#String Formatting
str = "Susan"
str1 = 'p'
str2 = f"{str}{str1}"
print(str2)