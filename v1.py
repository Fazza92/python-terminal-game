print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1 make your choice ")
print("********************No Cheating\n\n" * 15)
player2 = input("Player 2 make your choice ")

if player1 == player2:
  print("It's a tie!")
elif player1 == "rock":
    if player2 == "scissors":
      print("player1 wins!")
    elif player2 == "paper":
      print("player2 wins!")
elif player1 == "paper":
    if player2 == "rock":
      print("player1 wins!")
    elif player2 == "scissors":
      print("player2 wins!")
elif player1 == "scissors":
    if player2 == "paper":
      print("player1 wins!")
    elif player2 == "rock":
      print("player2 wins!")
else:
    print("Something went wrong.")