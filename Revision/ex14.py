from sys import argv

file_name, user_name = argv
prompt='> '
print(f"{user_name}, {file_name}")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f"""
Helloo world........
I am learning Python
""")