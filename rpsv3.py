from random import randint

player1 = 0 
player2 = 0 


while player1 < 2 and player2 < 2: 

    print(f"player 1 score: {player1}")
    print(f"player 2 score: {player2}")

    print("rock...")
    print("paper...")
    print("scissor...")

    p1 = input ("player 1, make your move: ")
    print("**********no cheating! \n \n" * 100)
    p2 = input ("player 2, make your move: ")

    if p1 == p2:
        print("its a tie")
    elif p1 == "rock":
        if p2 == "scissors":
            print("player one wins")
            player1+=1
        elif p2 == "paper":
            print("player two wins")
            player2+=1
    elif p1 == "paper":
        if p2 == "rock":
            print("player 1 wins")
            player1+=1
        elif p2 == " scissors":
            print("player 2 wins")
            player2+=1
    elif p1 == "scissor":
        if p2 == "rock":
            print("playe 2 wins")
            player2+=1
        elif p2 == "paper":
            print("player 1 wins")
            player1+=1
    else: 
        print("something went wrong")
print(f"final scores: \n player 1 : {player1} \n player 2: {player2}")