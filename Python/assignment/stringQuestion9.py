"""9. Write a Python program that accepts a comma-separated sequence of words as input and
prints the distinct words in sorted form (alphanumerically).
a) Sample Words : build, deploy, monitor, build, scale, monitor
b) Expected Result : build, deploy, monitor, scale"""

string = input("Please enter a string with ',' seperated: ")
def sortString(string):
    list = string.split(', ')
    list.sort()
    print(list)
    j = 0
    output = ""
    for word in list:
        if list[j - 1] != list[j]:
            output = output + ', ' + list[j]
        j += 1
    output = output.removeprefix(', ')
    print(output)

sortString(string)