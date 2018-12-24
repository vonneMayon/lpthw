tabby_cat = "\tI'm tabbed in {}.".format('Poe style')
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
# can you use .format or f in """

# what's the point of the prints below
print(tabby_cat)
print(persian_cat)
print (backslash_cat + f"{backslash_cat} it is")
print(fat_cat + "\n\t* all the others")
# the print allows the assigned variables to be printed
