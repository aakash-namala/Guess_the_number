#program to guess the number

import random
print('Guess a number and check it')
guess=int(input('Guess the number:'))
n=random.randint(1,10)
if (guess==n):
    print(f'The number is {n}')
    print('the number you have guessed is correct,You won')
else:
    print(f'The number is {n}')
    print('the number you have guessed is wrong,Better luck next time')
