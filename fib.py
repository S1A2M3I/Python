#Fibonacci
fib1 = 0
fib2 = 1
fib = 0
num = int(input("Enter a number: "))
while(fib < num):
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib
    print(fib)