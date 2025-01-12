#we will find first even number in a tuple
i = 0
number = [25,877,93,88]
print(number)
while i in number:
    print("inside while")
    if i % 2 == 0:
        print(f"{i}, is a even no.")
        break
    print(i)