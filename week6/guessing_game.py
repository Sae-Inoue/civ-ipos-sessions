import random

MAX_NUMBER = 100
def generate_random_number(n):
    return random.randint(1, n+1)

def guess_number(guess, number):
    if guess > number:
        return 'Too high'
    if guess < number:
        return 'Too low'
    if guess == number:
        return 'Correct'

    #return ('Too high' ,'Too low', 'Correct')

def play():
    number = generate_random_number(MAX_NUMBER)
    tries = 0
    while True:
        # 2. dynamically narrow the range
        # 3. Play against an AI
        print(f'Guess a number between 1 and {MAX_NUMBER}')
        guess = int(input('Guess a number>'))
        #
        tries += 1
        print(f'Your guess was {guess_number(guess, number)}')
        if guess_number(guess,number) == 'Correct':
            print("Well done!")
            print(f'It took you {tries} tries')
            break


play()