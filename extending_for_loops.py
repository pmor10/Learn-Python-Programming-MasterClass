number = "9, 223, 432, 421, 645, 968, 165"
cleanedNumber = ''

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char

NewNumber = int(cleanedNumber)
print("The number is {}".format(NewNumber))

for state in ["not pinin'", "no more", "a stiff", "bereft of life"]:
    print("This parrot is " + state)
    #print("This parrot is {}".format(state))

for i in range(0, 100, 5):
    print("i is {}".format(i))   

#nest for loop
for i in range(1, 13):
    for j in range(1, 13):
        print("{1} times {0} is {2}".format(i, j, i*j))
    print("===============") 



