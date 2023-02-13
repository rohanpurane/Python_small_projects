#******************** Password Cracker ********************#

from random import *

user_input = input('Enter Your Password : ')

a_string = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','@']
guess = ""

while(guess != user_input):
    guess = ""
    for letter in range(len(user_input)):
        guess_letter = a_string[randint(0,25)]
        guess = str(guess_letter)+ str(guess)
        print(guess)
print(f"Your Password is {guess}")