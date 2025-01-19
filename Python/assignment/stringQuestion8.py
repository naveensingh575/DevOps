"""8. Write a Python program to count the occurrences of each word in a given sentence.

our approach will be like
take a sentence as input
count the occurance of words of sentence
    loop 
    #if ==
    o/p in dict"""


sentence = input("plese input a sentence whom words we have to count: ")
#print(dir(str))
def occuranceOfEachWord(sentence) :
    list = sentence.split()
    print(list)
    dict = {}
    for word in list:
        count = list.count(word)
        dict[word] = count
    print(dict)

occuranceOfEachWord(sentence)