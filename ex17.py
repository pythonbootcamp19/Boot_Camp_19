#More Files
#We’ll write a Python script to copy one file to another. It’ll be very short but will give you ideas about other things you can #do with files.

from sys import argv

#os.path is built in Python library. exists is a function
#
#type os.listdir()
#
from os.path import exists

script,from_file,to_file = argv

print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how?

in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")
out_file.close()
in_file.close()