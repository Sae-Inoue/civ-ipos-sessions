import random

#MAX_NUMBER = int(input('Define max number!>>'))

def generate_random_number(n):
    return random.randint(1, n)

def guess_number(guess, number):
    if guess > number:
        return 'Too high'
    if guess < number:
        return 'Too low'
    if guess == number:
        return 'Correct'

    #return ('Too high' ,'Too low', 'Correct')

def play():
    MAX_NUMBER = int(input('Define max number!>>'))
    number = generate_random_number(MAX_NUMBER)
    tries = 1
    while True:
        print(f'Attempts: {tries} ')
        # 2. dynamically narrow the range

        # 3. Play against an AI

        print(f'Guess a number between 1 and {MAX_NUMBER}')
        guess = int(input('Guess a number>'))

        tries += 1
        print(f'Your guess was {guess_number(guess, number)}')
        if guess_number(guess,number) == 'Correct':
            print(f"Well done! You took {tries} tries\n")
            again = str(input("If you want try again, type y>>"))
            if again != 'y':
                print("\nThank you for playing the game!")
                break
            else:
                return play()

play()