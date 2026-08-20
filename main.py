def check_guess(guess):
    global count
    count += 1

    if guess < number:
        return "Too low!"
    elif guess > number:
        return "Too high!"
    else:
        return "Congratulations!"