from sys import argv
file_name, user_name = argv
prompt ='>'
print(f"Hi {user_name}, I'm the {file_name} file_name.")
print("I'd like you ask you a few questions.")
print(f"What is your favorite subject {user_name}?")
subject = input(prompt)
print(f"What is your favorite food {user_name}?")
food = input(prompt)
print(f"what is your favoite sports {user_name}?")
sports = input(prompt)

print(f"""
      So {user_name} you said your favorite is {subject}. 
      You favorite food is {food}. and your favorite sports is {sports}. That's awesome!
      """)