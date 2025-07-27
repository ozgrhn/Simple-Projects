import random

win_count = 0
lose_count = 0

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Select rock, paper or scissors. For quit 'q' : ").lower()

    if user_choice == "q":
        print(f"Game is over. Win = {win_count} Lose = {lose_count}")
        break
    if user_choice not in choices:
        print("Invalid choice. Try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer Choice : {computer_choice}")

    if computer_choice == user_choice:
        print ("It's a tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        win_count += 1
    else:
        print("You lose!")
        lose_count += 1
