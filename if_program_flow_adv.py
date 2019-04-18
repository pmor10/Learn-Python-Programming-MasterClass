age = int(input("How old are you? "))

if (age >= 16) and (age <= 65):
    print("Have a good day at work")
else:
    print("Enjoy your free time")

#Other way
if (age < 16) or (age > 65):
    print("Enjoy your free time")
else:
    print("Have a good day at work")    

#any non-zero or non-empty value will evaluate to true.
x = "false" 
if x:
    print("x is true")    

x = input("Please enter some text: ")
if x:
    print("You entered '{}' ".format(x))
else:
    print("You did not enter anything")    

parrot = "Norwegian Blue"
letter = input("Enter a character: ")

if letter in parrot:
    print("Give me an {}, Bob".format(letter))
else:
    print("I don't need that lettter")    