#student = {'name': 'Vik', 'age':25, 'courses': ['Math', 'Art', 'Education']}
student = {'first_name': 'Vik', 'age':25, 3: ['Math', 'Art', 'Education']}

# print(student[1])
# print(student[3])
#print(student('name'))
print(student.get('name', 'error name does not exist'))
#print(student.get('phone', 'Doesn't' Exist'))
