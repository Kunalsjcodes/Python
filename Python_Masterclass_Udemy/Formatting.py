for i in range(1,13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i*i, i*i*i))
    #.format(i, i**2, i**3) is also right.

print("\n")

for i in range(1,13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i*i, i*i*i))
    #Right Alligned

print("\n")

for i in range(1,13):
    print("No. {0:<2} squared is {1:<3} and cubed is {2:<4}".format(i, i*i, i*i*i))
    #left Alligned
