secret = 25

while True:
    guess = int(input("Guess the number: "))

    if guess == secret:
        print("Congratulations! Correct Guess")
        break

    elif guess > secret:
        print("Too High! Try Again")

    else:
        print("Too Low! Try Again")
