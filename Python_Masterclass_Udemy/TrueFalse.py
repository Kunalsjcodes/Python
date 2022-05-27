day = "Saturday"
temp = 30
raining = True

if day == "Saturday" and temp > 27 and not raining:
    print("Go Swimming")
else:
    print("Learn Python")

print("-" * 10)

if day == "Saturday" and temp > 27 or not raining:
    print("Go Swimming")
else:
    print("Learn Python")
