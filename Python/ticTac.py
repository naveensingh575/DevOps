#we will create the game in python
ticTac = ["","","","","","","","",""]
i = 1
while i <= 9:
    value = input("please tell X or O : " )
    position = input("please tell the position :")
    print(value)
    print(position)
    if ticTac[position] != "":
        if value == "X" or  value == "O":
            ticTac[position] = value
        else:
            Print(value + "is the invalid input")
    else:
        print("the value already exist")