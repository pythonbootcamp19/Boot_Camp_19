
count = 0
users = []
while count <= 2:
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    city = input("Enter City: ")
    zip_code = int(input("Enter Zip: "))
    subjects = input("Enter Subjects: ")
    marks = int(input("Enter Marks: "))
    
    users.append(count)
    count = count + 1
    
    user_info = {"Name": name, "Age": age, "City": city, "Zip": zip_code, "Subjects":subjects, "Marks": marks}
    
    print(user_info["Name"])
    print(user_info["Zip"])
    
# user_info = {"Name": "Vik", "age": 30, "city": "Mumbai", "Zip": 12345}
# print(user_info["Zip"])