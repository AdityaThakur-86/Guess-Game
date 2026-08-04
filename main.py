import random

number = random.randint(1,100)
count = 0

def check_guess(guess):
    global count
    count += 1

    if guess < number:
        return "Too low!"
    elif guess > number:
        return "Too high!"
    else:
        return "Congratulations! You guessed the number."

check_guess(0)  # Initialize the count