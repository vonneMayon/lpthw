formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
#why doesn't it have to have "" around the words? is it b/c it's boolion?
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format("Try your",
"Own text here",
"Maybe a poem",
"Or a song about fear"
))
