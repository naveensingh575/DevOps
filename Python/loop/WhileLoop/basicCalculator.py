#we will make a calculator
func = input("Type of function you want ['add','subtract', 'multiply' ,'divide']: ")
num1 = input("input first number: ")
num2 = input("input second number: ")

def calc(function, number1, number2):
    if function == "add" :
        output = int(number1) + int(number2)
    elif function == "subtract":
       # if int(number1) >= int(number2):
            output = int(number1) - int(number2)
       # else:
        #    output = int(number2) - int(number1)
    elif function == "multiply":
        output = int(number1) * int(number2)
    elif function == "divide":
        output = int(number1) / int(number2)
    else:
        output = "wrong function"

    print (f"{num1} and {num2} {func} is {output}")

calc(func,num1,num2)