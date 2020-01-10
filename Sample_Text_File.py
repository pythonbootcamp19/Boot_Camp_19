#from sys import argv
#script, filename = argv
#print(script)
file_name = input("Enter your file name? :")
txt = open(file_name)

#print(f"Your file name is {filename}:")

#print(txt)
file_data = txt.read()
#print(file_data)

length_file_data = len(file_data)
#print(len(file_data))
print(f"Length of the filename is: , {length_file_data}")

