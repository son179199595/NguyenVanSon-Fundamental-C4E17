while True:
    import random
    tukhoa = ["champion","meticolous","hexagon"]
    a=random.choice(tukhoa)


    if a == "champion":
        b=random.sample(a,8)
        print(*b)
        x=input("Your answer:")
        if x == a:
            print("Hura")
        else:
            print(":(")
    if a == "meticolous":
        b=random.sample(a,10)
        print(*b)
        x=input("Your answer:")
        if x == a:
            print("Hura")
        else:
            print(":(")
    if a== "hexagon":
        b=random.sample(a,7)
        print(*b)
        x=input("Your answer:")
        if x == a:
            print("Hura")
        else:
            print(":(")
