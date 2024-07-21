print("Guessing Game")
import random
def guess_game():
    number1=random.randint(a,b)
    print('i have guess a no. b/w',a,'and',b,'try and find what is it')
    guess=0
    attempt=0
    while guess!=number1:
        guess=input("enter your guess=")
        attempt+=1
        print('Attempts = ',attempt,'attempt.')
        if int(guess) < a:
            print("invalid input its under limit")
        elif int(guess) > b:
            print("invlid input its over limit")
        elif int(guess)<number1:
            print("too low")
        elif int(guess) > number1:
            print('too high')
        elif int(guess)==number1:
             print('Congratulations! You guessed the number',number1, 'in' ,attempt, 'attempts.')
             break              
a=int(input("Enter lower limit of guess game: "))
b=int(input("Enter higher limit of guess game: "))
guess_game()