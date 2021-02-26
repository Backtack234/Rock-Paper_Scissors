from random import randint

computer = ["Rock", "Paper", "Scissors", randint(1,3)]


player = str.upper(input("Rock, Paper, Scissors!? "))

def game():
    while player == False:
        if player == computer:
            print("It was a tie")
      elif player == "Rock":
          if computer == "Paper":
            print("You lose! " + computer + " covers " + player)
        else:
            print("You win! " + player + " smashes " + computer)
      elif player == "Paper":
          if computer == "Rock":
            print("You win! " + player + " covers " + computer)
        else:
          print("You lose! " + computer + " cuts " + player)
      elif player == "Scissors":
        if computer == "Paper":
          print("You Win! " + player + " cuts " + computer)
        else:
          print("You lose! " + computer + " smashes " + player)
      else:
        print("Sorry invalid answer, check your spelling")
        

      
      

game()

