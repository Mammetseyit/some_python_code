print("Warehouse item list\n")
number_of_items=int(input("How many items You wanna add: "))
items=[]

for i in range(number_of_items):
    additem=input("Add item: ")
    items.append(additem)
print(f"This is your list {items} \n")

items.sort()
print("The given list in a sorted order: ", items)

items.reverse()
print("The given list in a reverse sorted order: ", items)
