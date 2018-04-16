print("Hello,my name is Son and here is my sheep sizes in crease 50:")
size=[5, 7, 300, 90, 24, 50, 75]
print(size)
print("Now biggest sheep has size 300 let's shear it")

size[2]=8
print("After shearing, here is my flock")
print(size)
print("One month has passed, now here is my flock")

print([x+50 for x in size])
