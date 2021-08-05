# Python program to print Positive Numbers in a List
  
# list of numbers
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]
  
# using list comprehension
pos_nos_list1 = [num for num in list1 if num >= 0]
pos_nos_list2 = [num for num in list2 if num >= 0]
  
print("Positive numbers in the list 1: ", pos_nos_list1)
print("Positive numbers in the list 2: ", pos_nos_list2)
