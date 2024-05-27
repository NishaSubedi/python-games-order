menu = {
    'Pizza': 400,
    'coffee': 140,
    'Salad': 430,
    'Pasta': 540,
}

print("Welome")
print("Pizza: RS400\ncoffee: Rs140\nSalad: Rs430\nPasta: Rs540")
order_total = 0

item_1 = input("Enter item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered iten not available! ")

another_order = input("Do you want to order more? (yes/no)")
if another_order == "yes":
    item_2 = input("Enter the second order= ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item{item_2} has been added to your order")
    else:
        print(f"ordered item{item_2}is not available!")


another_order = input("Do you want to order more? (yes/no)")
if another_order == "yes":
    item_3 = input("Enter the third order= ")
    if item_3 in menu:
        order_total += menu[item_3]
        print(f"item{item_3} has been added to your order")
    else:
        print(f"ordered item{item_3}is not available!")


print(f"The total amount of your order is{order_total}")
