"""6. Write a Python program to count the number of characters (character frequency) in a
string.
a) Sample String : 'devops.example.com'
b) Expected Result : {'d': 1, 'e': 3, 'v': 1, 'o': 2, 'p': 1, 's': 1, '.': 2, 'x': 1, 'a': 1, 'm': 2, 'l': 1,
'c': 1} """

def CountNoOfOccrn(str):
    str = str.casefold()
    str = str.upper()
    i = 0
    dict = {}
    while i < len(str):
        count = str.count(str[i])
        dict[str[i]] = count
        dict = dict
        i += 1
    try:
            print(dict.pop(' '))
    except:
            pass
    return print(dict)

sample_str = input("Please enter the string whom latter you want to count: ")
output = CountNoOfOccrn(sample_str)
print(output)