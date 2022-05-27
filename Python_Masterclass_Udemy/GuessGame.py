answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Please guess a higher number")
    guess = int(input())
    if guess == answer:
        print("Well Done!")
    else:
        print("OOPS! Wrong Guess")
elif guess > answer:
    print("Please guess a lower number")
    guess = int(input())
    if guess == answer:
        print("Well Done!")
    else:
        print("OOPS! Wrong Guess")
else:
    print("Yooooo You got it right")
