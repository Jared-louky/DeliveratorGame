import time, sys, os

from deliveries import GenerateOffer

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def game_menu():
    print("Welcome to your option menu {}, below are a list of options to aid you".format(user_name))
    time.sleep(0.5)
    print(""" 
        1. Get a new delivery 
        2. Look at your credit account
        3. Check your milage 
        4. Exit the simulator 
    """) 
    choice = input("Please choose the corresponding number of what you'd like to do. ")
    while True:
        if choice == "1":
            print("Here is your order.") 
            # import and print order_info()
            pass
        elif choice == "2":
            print("you've chosen 2") #remove before final version 
            # import and print credit_account()
            pass
        elif choice == "3": # remove before final version 
            # import and print odometer
            print("you've chosen 3") #remove before final version 
            pass
        elif choice == "4":
            print("Thank you for your interest, dont forget CosaNostra's 30 minutes or else delivery gaurentee. /n Gooodbye")
            exit()
        else:
            print("Please choose a number from above")       




# Begining of game play.
user_name = input("What is your name?   ")

print("""
Hello {},
Welcome to the CosaNostra Pizza Delivery Company's delivery simulator, here at
CosaNostra Pizza we strive for the highest employee retention. In order to do so we 
ask a potential drivers to meet our minimun delivery driver requirments. What are these
requirements? Well is simple really, deliver your order in 30 minutes or less, otherwise 
face termination
""".format(user_name))

time.sleep(1)

game_menu()

