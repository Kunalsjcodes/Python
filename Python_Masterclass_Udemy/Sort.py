even = [2,4,6,8]
odd = [1,3,5,7,9]

even.extend(odd)
print(even)

even.sort()
print(even)

even.sort(reverse = True)
print(even)

pangram = "The quick brown box jumps over the lazy dog"
letter = sorted(pangram)
print(letter)

numbers = [2.3, 4.5, 8.7, 9.2, 1.6]
sorted_number = sorted(numbers)
print(sorted_number)
print(numbers)

numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown box jumped over the lazy dog")
print(missing_letter)


