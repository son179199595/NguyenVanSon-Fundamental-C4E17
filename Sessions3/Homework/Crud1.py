a=input("Welcome to our shop, what do you want (C ,R ,U ,D)?")
list=["T-shirt","Sweater"]
if a=="R":
    input(" ")
    print("Our item:",*list,sep=", ")
if a=="C":
    n=input("Enter new item: ")
    list.append(n)
    print("Our item:",*list,sep=", ")
if a=="U":
    input("Update position?")
    x=int(input("Update position?"))
    list.pop(x)
    y=input("New item?")
    list.append(y)
    print("Our item:",*list,sep=", ")
if a=="D":
    input("Delete position?")
    z=int(input("Delete position?"))
    list.pop(z)
    print("Our item:",*list,sep=", ")
