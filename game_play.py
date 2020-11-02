import time, sys, os

import deliveries

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

#Game play flow 
user_name = input("What is your name?   ")

print("Hello {}, Welcome to CosaNostra delivery simulation.\n".format(user_name))


while True:
    question = input("Would you like to continue? Y/N ")
    if question.lower() == "y":
        print("Here is your first order")
        break
    elif question.lower() == "n":
        print("Thank you")
        exit()
    else:
        print("Please enter Yes or No.")
        question




deliveries.order_info()


while True:
    accept = input("Would you like to accept this order?Y/N ")
    if accept.lower() == "y":
        break
    elif accept.lower() == "n":   #Issues with Loop
        accept
        break
    else:
        print("Please enter Yes or No.")

deliveries.order_completion()

deliveries.new_order()