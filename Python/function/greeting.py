#Greet the person
name = input("What is your person? ")
greetMessage = input("with which words you want to greet the person? ")
def greetFunc(person, message):
    print(f"{person}, {message}")

greetFunc(name, greetMessage)