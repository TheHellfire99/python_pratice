from random import randint
rand_num = randint(0,2)

print("Rock.........")
print("Paper........")
print("Scissors......")

p1 = input("player 1, make your move: ").lower()

if rand_num == 0:
    computer = "rock"
elif rand_num == 1: 
    computer = "papers"
else: 
    computer = "scissors"

print("computer played, " + computer)


if p1 == computer:
    print("its a tie")
elif p1 == "rock":
    if computer == "scissors":
        print("player one wins")
    elif computer == "paper":
        print("player two wins")
elif p1 == "paper":
    if computer == "rock":
        print("player 1 wins")
    elif computer == "scissors":
        print("player 2 wins")
elif p1 == "scissors":
    if computer == "rock":
        print("playe 2 wins")
    elif computer == "papers":
        print("player 1 wins")
else: 
    print("something went wrong")