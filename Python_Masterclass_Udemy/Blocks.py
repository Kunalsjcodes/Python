#Indentation
for i in range(1,5):
    print("Kunal Sharma")
    print("*" * 50)

print("\n")

for i in range(1,5):
    print("Kunal Sharma")
print("*" * 50)

#If, Else, Elif

name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age<18:
    print("Please come after {0} years".format(18-age))
elif age == 100:
    print("NICE Happy 100")
else:
    print("Eligible to vote!")


