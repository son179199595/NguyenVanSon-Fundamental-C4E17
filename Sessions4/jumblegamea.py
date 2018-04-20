while True:
    import random
    list=["c","h","a","m","p","i","o","n"]
    print(*random.sample(list,8))
    x=input("Your answer:")
    a="champion"
    if a==x:
        print("Hura")
        break
    else:
        print(":(")
