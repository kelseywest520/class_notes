#First way to open a file


open_file = open("data_file.txt")
contents = open_file.read()
#contents=open_file.readlines() reads the lines. line for 1st line.
print(contents)
open_file.close()
print(help(open_file))


#second way to open a file
with open ("data_file.txt") as better_open_file:
    better_contents = better_open_file.read()

print(better_contents)
    #automatically closes when the indent ends 
