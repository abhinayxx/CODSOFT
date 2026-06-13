import random
while True:
    choices = ["Rock", "Paper", "Scissors"]
    user = input("Enter Rock, Paper, or Scissors: ")
    computer = random.choice(choices)
    print("Computer chose:", computer)
    if user == computer:
        print("It's a tie!")
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        print("You win!")
    elif user in choices:
        print("Computer wins!")
    else:
        print("Invalid choice!")
    play_again = input("Play again? (yes/no): ")
    if play_again != "yes":
        print("Thanks for playing!")
        break
