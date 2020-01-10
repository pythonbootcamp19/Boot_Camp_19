def take_user_details():
    """
    This function asks users 4 questions to the users
    1. number of people - loop will run number of times based on the number of people
    2. user details consists of name, age and country - after taking user details it stores them in dict and list
    3. 
    """

    no_of_people = int(input("Enter the number of people:" ))
    user_list = []
    for user in range(no_of_people):
        user_details = {}
        user_details["name"] = input("Enter name: ")
        user_details["age"] = input("age: ")
        user_details["country"] = input("Enter country: ")
        user_list.append(user_details)

    return user_list

result = take_user_details()
#print(result)

def filter_users(filter_key, filter_value, all_users):
    """
    It'll ask user to enter the name of the country and based on the country 
    it'll filter the users.
    """
    filter_result = []

    for user in all_users:
        if user[filter_key] == filter_value:
            filter_result.append(user)
    return filter_result
all_users = take_user_details()