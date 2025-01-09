#Program to generate the table of input number
def table():
    num = input("Input a number whoes table you want to print:")
    i = 1
    while i <= 10:
        table = int(num) * int(i)
        print(table)
        i += 1
table()