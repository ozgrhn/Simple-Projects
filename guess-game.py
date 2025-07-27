import random

comp_num = random.randrange(1, 100)
print(comp_num)
guess_count = 0

while True:
    user_guess= int(input("Guess the number (1-100): "))
    difference = abs(comp_num - user_guess)
    guess_count += 1
    try:
        if difference == 0:
            print("You Win!")
            print("The correct number was: ", comp_num)
            break

        elif difference < 5:
            print("Very Hot")

        elif difference < 10:
            print("Hot")

        elif difference < 15:
            print("Warm")

        elif difference > 15:
            print("Cold")

        if guess_count == 7:
            print("Game Over:")
            break
    except ValueError:
        print("Wrong Value. Try Again")