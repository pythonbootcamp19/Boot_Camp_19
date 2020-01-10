#Python library import argument variable

from sys import argv

#call a script text file that contains Python program. Filename will be what user enter. In this program file name is ex15_sample.txt

script_name, filename = argv

#txt is a variable. Save all the text from the text file into variable.

txt = open(filename)

# when the user presses enter in terminal, it'll display the filename user entered

print(f"Here's your file {filename}:")

#it'll print the text from the file name

print(txt.read())

print("Type the filename again:")
file_again = input(">")
txt_again = open(file_again)

print(txt_again.read())
