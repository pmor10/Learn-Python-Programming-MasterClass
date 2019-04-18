age = 24
print("My age is " + str(age) + " years")

# Using str.format() method
# {} replacement field and placeholder 
# Syntax:{}.format(value)
print("My age is {0} years".format(age)) 

# Using multiple formatterss
print ("There are {0} days in {1}, {2}, {3}. {4}, {5}, {6}, and {7}".format( 31, "Jan", "Mar", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))

print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Aug: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}
 """.format(28,30,31))

# %d replace with an integer 
# %s stands with string
print("My age is %d years" % age)
print("My age is %d %s, %d %s" % (age, "years", 6, "months"))

# %2d allocated 2 spaces
for i in range(1,12):
    print("No %2d squared is %4d and cube is %4d" % (i, i**2, i**3))

print("Pi is approximately %12f" % (22 / 7))   

for i in range(1,12):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i**2, i**3))

print("Pi is approximately {0:12.50}".format(22 / 7))

for i in range(1, 12):
    print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))

    