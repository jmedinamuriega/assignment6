# 2. The Shopping List Maker
# Objective:
# The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list.
# Task 2: Include a feature to remove items from the list.
# Task 3: Add a function that prints out the entire list in a formatted way.
list_items = []
item_do = input("Do you want to (a)dd, (r)emove, (s)how or (q)uit?: ")

def add():
    item=input("Enter the item that you want to add: ")
    list_items.append(item)
    print(f"Added {item} to the list")
def remove():
    item=input("Enter the item that you want to remove: ")
    if item in list_items:
        list_items.remove(item)
        print(f"Removed {item} from the list")
    else:
        print(f"That item is not in the list, here is the list of items: {list_items}")
def show():
    print("Here is the list of items: ")
    for items in list_items:
        print(items)

while item_do.lower()!="q":
    if item_do.lower() == "a":
        add()
    elif item_do.lower() == "r":
        remove()
    elif item_do.lower() == "s":
        show()
    else:
        item_do = input("Please put a valid input. Do you want to (a)dd, (r)emove, (s)how or (q)uit?: ")
    item_do = input("Do you want to (a)dd, (r)emove, (s)how or (q)uit?: ")