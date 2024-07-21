'''Writing a Python program that generates a
random number between 1 and 100. The
user should then try to guess the number.
The program should provide hints such as
"too high" or "too low" until the correct
number is guessed.
'''
print("Guessing Game")
import random
def guess_game():
    number1=random.randint(1,100)
    print('i have guess a no. b/w 1 and 100 try and find what is it')
    guess=0
    attempt=0
    while guess!=number1:
        guess=input("enter your guess=")
        attempt+=1
        print('Attempts = ',attempt,'attempt.')
        if int(guess) < 1:
            print("invalid input its under limit")
        elif int(guess) > 100:
            print("invlid input its over limit")
        elif int(guess)<number1:
            print("too low")
        elif int(guess) > number1:
            print('too high')
        elif int(guess)==number1:
             print('Congratulations! You guessed the number',number1, 'in' ,attempt, 'attempts.')
             break              
guess_game()