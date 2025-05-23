import random

while True:
    number = random.randint(1, 100)
    attempts = 10
    print("I have a number between 1 and 100. You have 10 attempts to guess it.")

    for i in range(attempts):
        guess = int(input(f"Attempt {i+1}: Enter your guess: "))
        if guess == number:
            print("You guessed it right!")
            break
        elif guess < number:
            print("Too low!")
        else:  # guess > number
            print("Too high!")
    else:
        print(f"Number was {number}. You lost.")

    answer = input("Want to play again? (yes/no): ").lower()
    if answer not in ['y', 'yes', 'ok']:
        print("Thanks for playing!")
        break
