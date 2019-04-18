for i in range(1,20):
    print("i is now {}".format(i))

#put each character in a string once at a time
number = "9, 233, 324, 654, 765, 976, 543"
for i in range(0, len(number)):
    print(number[i])

number = "9, 321, 432, 421, 765, 534, 986"

for i in range(0, len(number)):
    if number[i] in '0123456789':
        print(number[i], end="\n")

 
