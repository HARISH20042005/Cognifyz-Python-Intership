import random

start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

secret_number = random.randint(start, end)

while True:
    guess = int(input(f"Guess a number between {start} and {end}: "))

    if guess < secret_number:
        print("Too Low!")
    elif guess > secret_number:
        print("Too High!")
    else:
        print("Congratulations! You guessed the correct number.")
        break