shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in shopping_list:
    print("Buy " + item)

print("\n")
#Continue
for item in shopping_list:
    if  item == "spam":
        continue
    
    print("Buy " + item)

print("\n")
#Break
for item in shopping_list:
    if  item == "spam":
        break
    
    print("Buy " + item)

print("\n")
#Searching
item_to_find = "XYZ"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
  
if found_at is not None:
    print("Item found at position {0}".format(found_at))
else:
    print("{} not found".format(item_to_find))
