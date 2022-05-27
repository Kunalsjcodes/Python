a = 12
b = 3

print (a + b)   #15
print (a - b)   #9
print (a * b)   #36
print (a / b)   #4
print (a % b)   #0 modulo: the remainder after integer division

print("\n")

for i in range(1,5): 
    print(i)

print("\n")

for j in range(1,a/b): 
    print(j)

print("\n")

#BODMAS
print(a + b / 3 - 4 *12) #or print(a +(b / 3) - (4 *12))
print((((a + b) / 3) - 4) * 12)


c = a + b
d = c /3
e = d - 4
f = e * 12
print(f)

print("\n")

print(a / (b * a) /b)
