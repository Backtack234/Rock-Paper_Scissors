from random import randint
t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]
def game(player):
    while player == False:
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!! " + computer + " covers " + player)
            else:
                print("You win!" + player + " smashes" + computer)
        elif player == "Paper":
            if computer == "Rock":
                print("You win! " + player + " covers" + computer)
            else:
                print("You lose! " + computer + " smashes" + player)
        elif player == "Scissors":
            if computer == "Paper":
                print("You win! " + player + " cuts" + computer)
            else:
                print("You lose! " + computer + " smashes" + player)
        else:
            print("Sorry that's not a valid play! Check your spelling")
            int(input("Press 1 to quit..."))
            if player == chr(49):
                break

game(False)
