#We will learn about the If else if conditions here
#syntax
"""if condition1 :
    statement1
elif condition2 :
    statement2
else :
    statement3 """
i = 0

system = [11, 13, 15 , 17, 19, 22, 25, 29]

while i in system:
    if i % 2 == 0:
        print(f'{i} is even no')
        break
    else:
        print('Tuple do not have even no')
