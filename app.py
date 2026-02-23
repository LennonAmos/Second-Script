import random

secret_number = random.randint(1, 10)
guess = int(input("What is your guess?"))
if guess == secret_number:
    print("You guessed correctly!")
else:
    print("Sorry, You were wrong!")

input("Press Enter to exit...")