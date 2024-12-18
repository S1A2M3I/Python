# Python is a programming language that lets you work quickly and integrate systems more effectively.
# It's a general-purpose language that lets you work with data, whether in the cloud or on-premises.
# Framework is a collection of tools and libraries that can be used to build applications.
# Framework for Python is the tkinter library which is used to build GUI applications.
# Python is a well intentended and standard language.
# Python is a high-level, interpreted, general-purpose programming language.
# Python is a high-level programming language that is interpreted, which means that the code is executed directly by the   
# interpreter.
# Inventory Managment System using python, tkinter library, and MySQL Database.
# in-built functions in python like print(), input(), etc.
# Opps and Procedural Programming Language difference between them.
# Procedural programming is a programming paradigm that uses a collection of functions to build a program.
# Opps programming is a programming paradigm that uses objects and their interactions to build a program.
# numpy and pandas are two popular libraries in Python for data analysis and manipulation.
# Pandas is a popular library for data manipulation and analysis in Python.
# Numpy is a popular library for numerical computing in Python.


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
#Relational operators
#Assignment operators 
#Special operators

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
print(num//num1)#floor division returns the nearest whole number
print(num**num1)#exponential returns the value of num raised to the power  
#of num1

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
print(not(num>num1 or num>num1))#not returns the opposite value of the 
#expression and returns true if the expression is false 

#bitwise operators is used to perform bit-wise operations on integers
#and is used to perform bitwise and operation on integers
#or is used to perform bitwise or operation on integers
#not is used to perform bitwise not operation on integers
#xor is used to perform exclusive or operation on integers
#left shift is used to move the bits to the left by the specified amount
#right shift is used to move the bits to the right by the specified amount
print(num&num1)
print(num|num1)
print(~num)
print(num^num1)
print(num<<num1)
print(num>>num1)#right shift 

#membership operators is used to check if a sequence is present in an object
#in
#not in
li = [1,2,3,4,5]
print(3 in li)
print(3 not in li)

#identity operators is used to check if two objects are the same or not
#is
#is not
print(num is num1)
print(num is not num1)

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
print(str[-3:-1])

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

#String Methods
str = "Susan"
str1 = 'p'
str2 = str.upper()
print(str2)
str2 = str.lower()
print(str2)
str2 = str.title()
print(str2)
str2 = str.capitalize()
print(str2)
str2 = str.find('u')
print(str2)
str2 = str.replace('u','o')
print(str2)
str2 = str.count('u')
print(str2)
str2 = str.strip()
print(str2)
str2 = str.split()
print(str2)
str2 = str.endswith('n')
print(str2)
str2 = str.startswith('S')
print(str2)
str2 = str.count('u')
print(str2)


#Conditional Statements
# if
# else
# elif
#Nested if
#Ternary Operator

#if-else
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#if-elif-else
age = int(input("Enter your age: "))
if age >= 18 and age < 100:
    print("You are eligible to vote")
elif age == 17:
    print("You can vote next year")
else:
    print("You are not eligible to vote")
    
#multiple if
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
if age == 17:
    print("You can vote next year")
if age < 18:
    print("You are not eligible to vote")
else:
    print("You are not eligible to vote")
    

a = 10
b = 15
c = 9

if a > b and a > c:
    print("a is greater")
elif b > c:
    print("b is greater")
else:
    print("c is greater")
    
    
    
    
#tuple 
#list
#set
#dictionary

#tuple used to store multiple values and immutable
#helps to store hetrogenous values
#it will store your data in continuous memory allocation
#random access of data not possible
tup = (1,2,3,4,5,2,3,6,2,1)
print(tup)
print(type(tup))

#Random accesss
print(tup[0])

#tuple immutable
# tup[0] = 10
# print(tup)
#single value in tuple is not tuple type value but it is int type value
tup1 = (1)
print(tup1)
print(type(tup1))

#tuple slicing
print(tup[0:3])
print(tup[:3])
print(tup[1:3])
print(tup[1:])
print(tup[-3:-1])

#tuple methods
print(tup.count(2))#count of the element
print(tup.index(2))#index of the element


#list used to store multiple values 
#helps to store heterogenous values
#it will store your data in continuous memory allocation
#it is mutable that is it can be changed
#it will also have random access of data possible i.e. indexing
list = [1,2,3,4,5,6]
print(list)
print(type(list))

#Random accesss
list[0] = 10
print(list)

#single value in list is a list type value
list1 = [1]
print(list1)
print(type(list1))

#list slicing
print(list[0:3])
print(list[:3])
print(list[1:3])
print(list[1:])
print(list[-3:-1])

#list methods
print(list.count(2))#count of the element
print(list.index(2))#index of the element
print(list.append(6))#inserts the element
print(list.insert(2,6))#inserts the element
#print(list.remove(2)) removes the element
# print(list.pop()) removes the last element
# print(list.clear()) clears the list
print(list.reverse())#Descending 
print(list.sort())#Ascending by using sort method
print(list.sort(reverse=True))#Descending by using sort method

#Functions work for multiple values
#methods work for single value
#stack is static memory allocation
#Heap is dynamic memory allocation
#list uses methods and dynamic memory allocation


#set are used to store unique values
#it is immutable
#it will also have random access of data possible
#it is unordered
#it is not indexed
#Hashable does not allow duplicate values in set
set = {1,2,3,4,5}
print(set)
print(type(set))

#single value in set is a set type value
set1 = {1}
print(set1)
print(type(set1))

#unhashable
# set = {1,2,3,4,5,1,[2,3,2,2,1]} lists are unhashable
# print(set)

#immutable
# set[0] = 10
# print(set)

#set methods
print(set.add(6))#adds the element by sorting and then add the element
print(set.remove(2))
print(set.discard(2))
# print(set.clear())
# print(set.pop())

set2 = {6,7,6,4,2,8,9,2}
print(set.union(set2))
print(set.intersection(set2))


#dictionary here values are stored in key value pair
#it is mutable
#it will also have random access of data possible
#it is unordered
#it is not indexed
dict = {"name": "John", "age": 30, "city": "New York"}
print(dict)
print(type(dict))

#accessing values in dictionary using key
print(dict["name"])
print(dict["age"])
print(dict["city"])

#single value in dictionary is a dictionary type value
dict1 = {"name": "John"}
print(dict1)
print(type(dict1))

#mutable
dict["name"] = "John Smith"
dict["age"] = 31
dict["city"] = "New York"
print(dict)

#Empty dictionary
dict = {}
print(dict)

#nested dictionary
dict = {
  "name": "John",
  "age": 30,
  "address": {
    "street": "123 street",
    "city": "Hyderabad",
    "state": "Telangana" 
  }
}
print(dict)

#accessing values in nested dictionary
print(dict["address"]["street"])

#dictionary methods
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("name"))
print(dict.pop("name"))
# print(dict.popitem())
# print(dict.clear())
print(dict.copy())
print(dict.update({"name": "John Smith"}))

#update
new_dict = {
    name: "John Smith",
}


#return list of keys in dictionary
print(dict.keys())

#add dictionary manually by user input with keys and values
dict4 = {}
num8 = int(input("Enter the number of keys: "))
for i in range(num8):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    dict4[key] = value
print(dict4)

#counting vowels
str9 = "John Smith"
count = 0
for i in str9:
    if i in "aeiouAEIOU":
        count += 1
print(count)


#loops 
#while loop
count = 5
while count > 10:
    print("Hello World")
    i += 1
    

# for loop using range
for i in range(1, 11):
    print(i)
    
#for loop using list
kli = [22,12,2,23,2]
for i in kli:
    print(kli[i])
    
# for loop using tuple
kli2 = (22,12,2,23,2)
for i in kli:
    print(kli2[i])
    
# for loop using dictionary
kli3 = {"name": "John", "age": 30, "city": "New York"}
for i in kli:
    print(kli3[i])


#finding an element in a list using while loop
li = [1,4,7,9,12,15,23]
count = len(li)-1
key = 15
flag = 0
while count >= 0:
    if ((li[count]) == key):
    #or if key in li[count]:
        print("found the key :",key,"and index is :",count)
        flag = flag + 1
        break
    count -= 1
if flag == 0:
    print("key not found")
    
#finding an element in a list using index method
li1 = li.index(15)
if li1:
    print("Element found :",li1)
else:
    print("Element not found")
    
#Unique Elements     
li4 = [3,7,8,1,1,3]
li5 = []
count = len(li4)-1
for i in range(0,count):
    for j in range(i+1,count+1):
        if li4[i] == li4[j]:
            print("Duplicate elements are :",li4[i])
            break
        else:
            li5.append(li4[i])
            

#Counting odd elements in a list
li9 = [1,2,3,4,5,6,7,8,9]
count = 0
for i in li9:
    if i % 2 != 0:
        count = count + 1
print("Count of odd elements are :",count)

#finding an element in a list using for loop
li10 = [1,4,9,16,25]
key = 16
count = 0
for i in li10:
    count += 1
    if i == key:
        print("Element found",i,"and index is :",count)
        break
    
 #else should be outside the for loop to avoid infinite loop

else:
    print("Element not found")
    

#Factorial 
num = int(input("Enter a number: "))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print(fact)


#Function
def hello(n):
    return n*n

print(hello(5))

#user defined function
#print(),len(),max(),min(),sorted(),sum(),all(),any(),input()

def bill(amt,unit):
    total = unit + amt
    return total
#calling the function
print(bill("500000","Rs"))

#default parameter
def greet(name = "user"):
    print("Hello",name)
greet()

#converting every unit into usd
def bill(amt,unit="USD"):
    if unit == "Rs":
        total = float(amt) * 0.014
        return total
    elif unit == "dhr":
        total = float(amt) * 2.65
        return total
    else:
        total = unit + amt
        return total        
#calling the function
print(bill("500000","Rs"))
print(bill("500000","dhr"))
print(bill("500000"))


fruits = ["apple","banana","cherry"]
i = 0
while i<len(fruits):
        print(fruits[i])
        i += 1
