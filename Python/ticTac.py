#we will create the game in python
ticTac = ["","","","","","","","",""]
i = 1
while i <= 9:
    value = input("please tell X or O : " )
    position = input("please tell the position :")
    print(value)
    print(int(position))
    print(int(int(position) -1))
    if ticTac[int(int(position) -1)] == "":
        if value == "X" or  value == "O":
            ticTac[int(int(position) -1)] = value
            print(ticTac[int(int(position) -1)])
            i = i +1
        else:
            print(value + " is the invalid input")
    else:
        print("the value already exist")

print(ticTac)    