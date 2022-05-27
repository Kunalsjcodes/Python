splitString = "This string has been\nsplit over\nseveral\nlines\n"
print(splitString)

tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

print("\n")

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
#or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")
#when we're using triple quote, there's no need to escape any quote inside the string.
print("""The pet shop owner said "No, no, 'e's uh,...he's resting". """)

print("\n")

anotherSplitString = """This string has been
already splited over
several
lines"""
print(anotherSplitString)

print("\n")

extraSplitString = """This string has been \
already splited over \
several \
lines"""
print(extraSplitString)

print("\n")
#If we want to add backslash in print statement.
print("C:\users\timber Sharma\notes\string.txt")
#here it is using \t and \n as escapechar, To avoid that check the next two method

#Add double backslash, first is for accepting the second \ in print
print("C:\\users\\timber Sharma\\notes\\string.txt")
#Prefix the string with letter r, r for raw
print(r"C:\users\timber Sharma\notes\string.txt")


