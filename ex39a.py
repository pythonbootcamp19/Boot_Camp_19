number_of_profiles = 0
user_profile = {}

for number_of_profiles in range(5):
    names = input("Enter name: ")
    age = int(input("Enter age: "))
    user_profile[names] = [age]
print(user_profile)

#--------using while loop------

count = 0
users = []
while count <= 5:
    names = input("Enter name: ")
    age = int(input("Enter age: "))
    users.append(count)
    count = count + 1
    print ({names}, {age})



