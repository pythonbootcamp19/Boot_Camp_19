food_type = input("Would you like to order Seafood, Pizza or Ice Creame?: ")
distance = int(input("Enter the distance from the restaurant?: "))
if food_type == "Seafood" and distance <= "5":
    print("Delivery charge will be Rs.30")
elif food_type == "Seafood" and distance == "6" or <= "10":
    print("Delivery charge will be Rs.50")
elif food_type == "Seafood" and distance == "11" or <= "20":
    print("Delivery charge will be Rs.100")
else food_type == "Seafood" and distance >= "20" 
    print("Delivery in your area is not available.")

