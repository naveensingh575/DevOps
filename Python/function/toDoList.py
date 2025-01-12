#we will make to do list
#import datetime
from datetime import date as d
dateOfTask = input("What is the date of doing this task : ")
#print(datetime.date.today())
todayDate = d.today()
i = 0
listOfTask = ["",""]
listOfDesc = ["",""]
if dateOfTask >= str(todayDate):
    while i < 2:
        task =  input("Please tell the task: ")
        description = input("Please write the description of above task: ")
        listOfTask[i] = task
        listOfDesc[i] = description
        i += 1
else:
    print("Unfortunatlly, we can't correct our past")
print(listOfTask)
print(listOfDesc)