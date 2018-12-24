from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that hit, RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')
# if the 'w' wasn't there it would be assumed that it would bea read online to the opened file
# the 'w' basically is giving the command to write

print("Truncating the file. Goodbye!")
target.truncate()
# truncate means to delete or erase things that are in the file that has been opened

print("Now I'm going to ask for three lines.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file.")

target.write("""
line1 \n
line2 \n
line3 \n
""")
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally, we close it.")
target.close()
