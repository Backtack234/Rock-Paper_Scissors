from random import randint
def random_numer():
  random_numer = randint(1,3)
  if random_numer == 1:
    print("Rock")
  elif random_numer == 2: 
    print("Paper")
  elif random_numer == 3:
    return 
random_numer()

player = str.upper(input("Rock, Paper, Scissors!? "))

def game():
    while player == False:
      if player == random_numer:
        print("It was a tie")
      elif player == "Rock":
        if random_numer == "Paper":
          print("You lose! " + random_numer + " covers " + player)
        else:
          print("You win! " + player + " smashes " + random_numer)
      elif player == "Paper":
        if random_numer == "Rock":
          print("You win! " + player + " covers " + random_numer)
        else:
          print("You lose! " + random_numer + " cuts " + player)
      elif player == "Scissors":
        if random_numer == "Paper":
          print("You Win! " + player + " cuts " + random_numer)
        else:
          print("You lose! " + random_numer + " smashes " + player)
      else:
        print("Sorry invalid answer, check your spelling")
        

      
      

game()
