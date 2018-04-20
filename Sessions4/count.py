from collections import Counter
numbers=[1,6,8,1,2,1,5,6]
x= Counter(numbers)
y=int(input("Enter a number:"))
print(y,"appear", x.get(y),"times in my list")
