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
    list=["T-shirt","Sweater","Jeans"]

    x=int(input("Update position?"))
    y=input("New item?")
    list[x-1]= y

    print("Our item:",*list,sep=", ")





if a=="D":
    list=("T-shirt","Skirt","Jeans")

    z=int(input("Delete position?"))
    list.pop(z-1)
    print("Our item: ", *list,sep=", ")
