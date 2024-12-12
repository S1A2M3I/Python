#celsius and Farenheit temperature  
temp = input("Enter the temperature in cel or fahr: ")
if temp == "cel":
    cel = float(input("Enter the temperature in cel: "))
    fahr = (cel * 9/5) + 32
    print(fahr)
elif temp == "fahr":
    fahr = float(input("Enter the temperature in fahr: "))
    cel = (fahr - 32) * 5/9
    print(cel)
else:
    print("Invalid input")