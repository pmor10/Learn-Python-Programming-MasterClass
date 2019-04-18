# Write a small program to ask for a name and an age
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (They must be over 18 and under 31)
# If they are, welcome them to the holiday, otherwise print 
# a polite messege refusing them entry.

name = input("Please enter your name: ")
age = int(input("How old are you, {} ? ".format(name)))

if (age > 18) and (age < 31):
    print("Welcome {} to the holiday!".format(name))
else:
    print("Thank you for your intrest in the holiday but we won't be able to accept you. ")    
