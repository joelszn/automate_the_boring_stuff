import random

print('Hello, Enter your name:')
name = input()

print('Well, ' + name + ', I\'m thinking of a number between 1-20')
secret_number = random.randint(1, 20)

# wanna create a loop that keeps guessing 6 times
counter = 0
while counter < 6:
    print('Enter your guess: ')
    guess = input()
    if int(guess) > secret_number:
        print('Guess is too high')
    elif int(guess) < secret_number:
        print('Guess is too low')
    else:
        break # guess is correct
    counter +=1

if int(guess) == secret_number:
    print('Correct, ' + name + ' you guessed it correctly in ' + str(counter) + ' guesses')
