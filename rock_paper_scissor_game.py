print("rock...")
print("paper...")
print("scissor...")

p1 = input ("player 1, make your move: ")
p2 = input ("player 2, make your move: ")

if p1 == "rock" and p2 == "scissors":
    print("player1 wins")
elif p1 == "rock " and p2 == "paper":
    print("player 2 wins")
elif p1 == "paper" and p2 == "rock":
    print("player 1 wins")
elif p1 == "paper" and p2 == "scissors":
    print("player 2 wins")
elif p1 == "scissors" and p2 == "rock":
    print("player 2 wins")
elif p1 == "scissors" and p2 == "paper":
    print("player 1 wins")
elif p1 == p2:
    print("its a tie")
else: 
    print("something went wrong")