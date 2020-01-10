from sys import argv
script, input_file = argv

def print_all(f):
    print(f.read())
    
#seek will go back to the position 0. Take the cursor to position 0. If you say f.seek(4) it'll print from character 5 (it starts with 0).    
def rewind(f):
       f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)
          
print("Now let's rewind, kind of like a tape.")
          
rewind(current_file)
          
print("Let's print three lines:")
          
current_line = 1
print_a_line(current_line, current_file)

#or you can write as current_line += 1

current_line = current_line + 1
#current_line + 1 is not doing anything except showing 1, 2, 3 before each sentence.
print_a_line(current_line, current_file)
          
current_line = current_line + 1
print_a_line(current_line, current_file)