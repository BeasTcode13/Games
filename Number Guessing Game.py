import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    guess = None
    tries = 0
    print('Welcome to the number guessing game')
    print("I'm thinking of the number between 1 and 100")
    print("Can you guess it?")

    while guess != secret_number:
        guess = int(input('Enter the number'))
        tries += 1
        if guess > secret_number:
            print("Too High!, Try Again")
        elif guess < secret_number:
            print("Too low!, Try Again")
        else:
            print("Congratulations! You guessed the right number in ",tries," attempts")

number_guessing_game()
