#code to for counting
def counting(number):
    i = 0
    while i <= int(number):
        print(f"counter value is {i}")
        i += 1

num = input("Write counting from 0 to ")
counting(num)