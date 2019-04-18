parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])
print(parrot[0:6])
print(parrot[6:])
print(parrot[-4:-2])
print(parrot[0:6:2]) #Starting from index position 0 extract all the charachters up to, but not including
                     #index position 6 in steps of two
                     #Start from N skip to r and skip to e.
                     #skipping 2 characters at a time.

number = "9,255,432,432,564,657,876,087"
print(number[1::4])                     

print("Hello " * 4)

today = "firday"
print("day" in today)
print("in" in today)

#The slice starts at the first characters, and include every 5th character.
days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])