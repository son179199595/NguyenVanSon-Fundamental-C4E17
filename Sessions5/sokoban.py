iP=1
jP=1
iB=2
jB=2

while True:
    for i in range(4):
        for j in range(4):
            if i==iP and j==jP:
                print("P",end="")
            elif i==iB and j==jB:
                print("B",end="")
            elif i==3 and j==1:
                print("G",end="")
            else:
                print("-",end="")
        print()
    x=input("Your move:(W/A/S/D)?").upper()
    next_iP = iP
    next_jP = jP
    next_iB = iB
    next_jB = jB
    if x == "W":
        iP -= 1

    if x == "S":
        iP += 1

    if x == "D":
        jP += 1

    if x == "A":
        jP -= 1
