#                   1
#         012345678901234
parrot = "Norwegian Blue"

print(parrot)

print("\n")
#we win
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print("\n")

print(parrot[-1])
print(parrot[-14])

print("\n")

#we win (negative indexing)
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print("\n")

print(parrot[0:6]) #upto but not including 6 i.e, #Norweg
print(parrot[:6]) #start from 0 upto 6
print(parrot[6:]) #start from 6 end till last.
print(parrot[:]) #start from 0 and run till end as no value given.
print(parrot[:6] + parrot[6:])

print("\n")
print(parrot[-4:12]) #Bl
print(parrot[-4:-2]) #Bl

print(parrot[0:9:2]) #Step in a Slice (start 0: End upto 9: mark with jump of 2) #Nrein
print(parrot[:6:3]) #(start 0: End upto 6: mark with jump of 3) #Nw

print("\n")
number = "9,223;372,036 854:775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])


