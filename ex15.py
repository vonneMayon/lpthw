from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())
print(txt.close())

print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())
print(txt.again.close())
