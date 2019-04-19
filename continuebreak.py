shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    if item == 'spam':
        print("I am ignoring " + item)
        continue #Stops processing any more lines in the block and forces the for loop to move on to the next value in the sequence
    print("Buy " + item)

meal = ["egg", "bacon", "beans", "sausages"]
nasty_food_item = ''

for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
else:
    print("I'll have a plate for that, then, please")

if nasty_food_item == 'spam':
    print("Can't I have anything without spam in it.")
        