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



name = input("Enter your name: ")
elgaf = 21
age = int(input("Enter your age: "))

if age >= 21 and age <=90:
        weight = float(input("Enter your weight: "))
        if weight >= 50:
            print (f"{name} is eligible to donate blood")
else:
    print (f"{name} is not eligible to donate blood, then you have to wait at age {elgaf-age} years")
    