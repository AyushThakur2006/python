# a small menu system

menu=[]
while True:
    print("1. Add Item || 2. Remove Item || 3. View Item || 4. Exit")
    n=input()
    if n=="1":
        menu.append(input("enter item"))
    elif n=="2":
        menu.remove(input("Remove item"))
    elif n=="3":
        print(menu)
    elif n=="4":
        break
    else:
        print("Invalid choice")