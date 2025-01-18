"""7. Write a Python function that takes a list of words and return the longest word and the
length of the longest one.
a) Sample Output:
b) Longest word: Exercises
c) Length of the longest word: 9"""

#list = ["Naveen","Saurabh","Akashi","Gaurav","Navi Kumar"]
#list = input("Please enter the list ")
#list = list(list)
#print(list)

list = []
goOn = 'Y'
while goOn == "Y":
    wrd = input("Please enter the word ")
    goOn = input("is more words you want to input option [Y for Yes , N or other latter for No] ")
    goOn = goOn.upper()
    list.append(wrd)
print(list)

#defining the function of longest word identifing
def lngstwrd(listwrd):
    i = 0
    longest  = 0
    longestWrd = ""
    while i < len(listwrd):
        lngth = len(listwrd[i])
        if lngth > longest :
            longest = lngth
            longestWrd = listwrd[i]
        i += 1
    print(f"Longest word: {longestWrd}")
    print(f"Length of the longest word: {longest}")

# calling the function
lngstwrd(list)