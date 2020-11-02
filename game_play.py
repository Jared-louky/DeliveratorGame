import time
import sys
import os

import deliveries

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def end_game():
    print("Thank you for your interest.")


#Game play flow 
user_name = input("What is your name?   ")

print("Hello {}, Welcome to CosaNostra delivery simulation.\n".format(user_name))


while True:
    question = input("Would you like to continue? Y/N ")
    if question.lower() == "y":
        print("Here is your first order")
        break
    elif question.lower() == "n":
        end_game()
    else:
        print("Please enter Yes or No.")
        question




deliveries.order_info()

accept = input("Would you like to accept this order?Y/N ")
while True:
    if accept.lower() == "y":
        break
    elif accept.lower() == "n":
        print("Here is another order")
        break
    else:
        print("Please enter Yes or No.")

deliveries.order_completion()



    



