import time, sys, os, random, math

from deliveries import OrderInfo


#delivery_info = OrderInfo()

#Functions for fillagry
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.5)

def game_menu():
    print(""" 
    1. Get a new delivery 
    2. Look at your credit account
    3. Exit the simulator 
    """)
    choice = input("Please choose the corresponding number of what you'd like to do. ")
    while True:
        if choice == "1":
            print("Here is your first order")
            #Print("".format(delivery_info.order_amount, delivery_info.distance))
            confirmation = None
            while confirmation not in ["y", "n"]:
                confirmation = input("Would you like a different order?. Y/N ")
                if confirmation == "y":
                    print("Here is your second order results")
                    # genterate order results
                elif confirmation == "n":
                    print("Here are your delivery results.")
                    # genterate delivery results
                    game_menu()
                else:
                    print("Please enter Y/N") 
            game_menu()       
        elif choice == "2":
            print("You have money in your account.")
            # generate bank statment
            game_menu()
        elif choice == "3":
            print_slow("Thank you for your interest, dont forget CosaNostra's 30 minutes or else delivery gaurentee.")
            print("Goodbye!")
            exit()
        else:
            choice = False
            print("Please choose a number listed") 
            game_menu() 



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

print("Welcome to your option menu {}, below are a list of options to aid you".format(user_name))
time.sleep(.5)

game_menu()