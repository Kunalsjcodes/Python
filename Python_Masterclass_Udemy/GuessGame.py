import random

highest = 10
answer = random.randint(1,highest)
guess = 0
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())

    if guess == 0:
        break
    if guess == answer:
        print("Well Done")
        break
    else:
        if guess < answer:
            print("Please guess a higher number")
        else:
            print("Please guess a lower number")
    
