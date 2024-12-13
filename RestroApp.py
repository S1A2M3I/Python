#Food Menu
menu = {
    "Burger": 35,
    "Fries":120,
    "Salad":130,
    "Pizza": 230,
    "Coffee":330
}

#Greet 
print("Welcome to restro")
print("Pizza :Rs230\n Burger :Rs35\n Fries :Rs120\n Salad :Rs130\n Coffee :Rs330")
order_total = 0
item_1 = input("Enter the item name ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet!")
    
while(True):
    
    another_order = input("Do You Want Another Item!:(yes or no)")

    if another_order == "yes":
        item_2 = input("Enter the name of the next item !")
    
        if item_2 in menu:
            order_total = order_total + menu[item_2]
            print(f"Item {item_2} has been added to your order")
        else:
            print(f"Ordered item {item_2}  is not available yet!")
    elif another_order == "no":
        print("Thank You for ordering !")
        break

print(f"The Total Amount for items to pay is{order_total}")