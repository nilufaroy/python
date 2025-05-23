import random

player_score = 0
computer_score = 0
choices = ['rock', 'paper', 'scissors']

print("Rock, Paper, Scissors Game")
print("First to 5 points wins the match.\n")

while player_score < 5 and computer_score < 5:
    player_choice = input("Enter rock, paper, or scissors: ").strip().lower()
    if player_choice not in choices:
        print("Invalid input. Try again.\n")
        continue

    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)

    if player_choice == computer_choice:
        print("It's a draw.\n")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        print("You win this round!\n")
        player_score += 1
    else:
        print("Computer wins this round.\n")
        computer_score += 1

    print("Score - You:", player_score, "| Computer:", computer_score)
    print("-----------------------------------")

if player_score == 5:
    print("Congratulations! You won the match.")
else:
    print("Game over. Computer won the match.")
