# the basic fundamental logic behind the if is if the condition is true do something inside the if block.
# else = if the condition is false then run else block.
# elif (short for else if) = check the multiple conditions. if multiple conditions = for e.g. if 3 coditions. check 3 conditions. if one of the conditions is true run the if block or go to else block. 


people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")