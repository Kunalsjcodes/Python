letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]
print(backwards)

backwards = letters[25::-1] #to include a #or [::-1]
print(backwards)

print(letters[4::-1])       #edbca
print(letters[16:13:-1])    #qpo
print(letters[:-9:-1])      #last 8 char in reverse order
print(letters[-4:])         #wxyz
print(letters[:1])          #a
print(letters[0])           #a

