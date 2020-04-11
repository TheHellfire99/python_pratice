print("rock...")
print("paper...")
print("scissor...")

p1 = input ("player 1, make your move: ")
p2 = input ("player 2, make your move: ")

if p1 == p2:
    print("its a tie")
elif p1 == "rock":
    if p2 == "scissors":
        print("player one wins")
    elif p2 == "paper":
        print("player two wins")
elif p1 == "paper":
    if p2 == "rock":
        print("player 1 wins")
    elif p2 == " scissors":
        print("player 2 wins")
elif p1 == "scissor":
    if p2 == "rock":
        print("playe 2 wins")
    elif p2 == "paper":
        print("player 1 wins")
else: 
    print("something went wrong")