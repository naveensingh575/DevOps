#we will create the game in python
ticTac = ["","","","","","","","",""]
i = 1
while i <= 9:
    value = input("please tell X or O : " )
    position = input("please tell the position :")
    print(value)
    #print(int(position))
    print(int(int(position) -1))
    if int(position) >= 1 or int(position) <= 9:
        if ticTac[int(int(position) -1)] == "":
            if value == "X" or  value == "O":
                ticTac[int(int(position) -1)] = value
                print(ticTac[int(int(position) -1)])
                print(ticTac)
                if ((ticTac[0] == ticTac[1]) and (ticTac[0] == ticTac[2]) and ticTac[0] != "" ) or  ((ticTac[0] == ticTac[3]) and (ticTac[0] == ticTac[6]) and ticTac[0] != "" ) or  ((ticTac[0] == ticTac[4]) and (ticTac[0] == ticTac[6]) and ticTac[0] != "") or  ((ticTac[2] == ticTac[5]) and (ticTac[2] == ticTac[8]) and ticTac[2] != "" ) or  ((ticTac[2] == ticTac[4]) and (ticTac[2] == ticTac[6]) and ticTac[2] != "" ) or  ((ticTac[6] == ticTac[7]) and (ticTac[6] == ticTac[8]) and ticTac[6] != "" ) or  ((ticTac[3] == ticTac[4]) and (ticTac[3] == ticTac[5]) and ticTac[3] != "" ) or  ((ticTac[1] == ticTac[4]) and (ticTac[1] == ticTac[7]) and ticTac[1] != "" ):  
                    print("Player1 is the winner")
                    i = 10

                i = i +1
            else:
                print(value + " is the invalid value input")
        else:
            print("the value already exist")
    else:
        print(position + " is invalid position input")

#print(f'{ticTac[0]}  {ticTac[1]}  {ticTac[2]}')
#print(f'{ticTac[3]}  {ticTac[4]}  {ticTac[5]}')
#print(f'{ticTac[6]}  {ticTac[7]}  {ticTac[8]}')

print(ticTac)    