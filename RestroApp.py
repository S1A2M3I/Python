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
    print(f"Ordered item {item_1} it is not available yet!")
    
#Order
order = {
    "Burger": 2,
    "Fries": 1,
    "Salad": 1,
    "Pizza": 1,
    "Coffee": 1
}
