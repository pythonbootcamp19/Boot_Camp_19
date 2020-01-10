#script is a text file containing the statements that comprise a Python program. Once you have created the script, you can execute #it over and over without having to retype it each time. Scripts are editable.


from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
