import random

random_number = random.randint(1,10)

guess = None

while guess != random_number:
    guess = input("pick a number from 1 - 10: ")
    guess = int(guess)
    if guess < random_number:
        print("too low")
    elif guess>random_number: 
        print("too high")
    else:
        print("you won")
    
print(f"the number was {random_number}")