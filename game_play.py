import time
import sys
import os


from deliveries import Delivery 



def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def try_again():
    pass

user_name = input("What is your name?   ")

print_slow("""
Hello {}
Welcome to CosaNostra delivery simulation. 
""".format(user_name))




## Program unexpectly stops 
question = input("Would you like to continue? Y/N ")
if question.lower() == "y":
    print_slow("Preparing simulation")
    return game_play()

elif question.lower() == "n":
    print_slow("Thank you for your interest")
else:
    print("Please enter Yes or No.")
    return question

def game_play():
    print("Let's being")

