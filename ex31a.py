
food_type = input("Would you like to order Seafood, Pizza or Ice Creame?: ")
distance = int(input("Enter the distance from the restaurant?: "))

if food_type == 'Seafood' and distance <= 5:
    print("Delivery charge will be Rs.30")
elif food_type == 'Pizza' and distance <= 5:
    print("Delivery charge will be Rs.30")
elif food_type == 'Ice Creame' and distance <=5:
    print("Delivery charge will be Rs.30")

elif food_type == 'Seafood' and distance == 6 or distance <= 10:
    print("Delivery charge will be Rs.50")
elif food_type == 'Pizza' and distance == 6 or distance <= 10:
    print("Delivery charge will be Rs.50")
elif food_type == 'Ice Creame' and distance == 6 or distance <= 10:
    print("Delivery charge will be Rs.50")

elif food_type == 'Seafood' and distance == 11 or distance <= 20:
    print("Delivery charge will be Rs.100")
elif food_type == 'Pizza' and distance == 11 or distance <= 20:
    print("Delivery charge will be Rs.100")
elif food_type == 'Ice Creame' and distance == 11 or distance <= 20:
    print("Delivery charge will be Rs.100")

else:
    print("Delivery in your area is not available.")




# if food_type == 'Seafood' and distance <= 5:
#     print("Delivery charge will be Rs.30")
# elif food_type == 'Seafood' and distance == 6 or distance <= 10:
#     print("Delivery charge will be Rs.50")
# elif food_type == 'Seafood' and distance == 11 or distance <= 20:
#     print("Delivery charge will be Rs.100")
# else:
#     print("Delivery in your area is not available.")


# food_type = input("Would you like to order Seafood, Pizza or Ice Creame?: ")
# distance = int(input("Enter the distance from the restaurant?: "))





# if (food_type == 'Seafood' or food_type == 'Pizza' or food_type == 'Ice Creame' and distance <= 5):
#     print("Delivery charge will be Rs.30")
# elif (food_type == 'Seafood' or food_type == 'Pizza' or food_type == 'Ice Creame' and distance == 6 or distance <= 10):
#     print("Delivery charge will be Rs.50")
# elif (food_type == 'Seafood' or food_type == 'Pizza' or food_type == 'Ice Creame' and distance == 11 or distance <= 20):
#     print("Delivery charge will be Rs.100")
# else:
#     print("Delivery in your area is not available.")

