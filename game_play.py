import time, sys, os, random, math

from deliveries import OrderInfo
from wallet import Wallet

# Original argument parameters 
distance = random.randint(7,35)
rate = random.randint(65, 75)
order_amount = random.randint(150, 350)

# Second argument paraments 
new_distance = random.randint(7,35)
new_rate = random.randint(65,75)
new_order_amount = random.randint(150,350)

# first order call 
delivery_info = OrderInfo(distance, rate)
account_info = Wallet(order_amount)

# second order call
new_delivery_info = OrderInfo(new_distance, new_rate)
new_account_info = Wallet(new_order_amount)



# Functions for fillagry
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.08)

    

def game_menu():
    print(""" 
    1. Get a new delivery 
    2. Look at your credit account
    3. Exit the simulator 
    """)
    choice = input("Please choose the corresponding number of what you'd like to do. ")
    # BEGINS MY INFINITE LOOP
    while True:
        if choice == "1":
            print_slow("Here is your first order" + "\n")
            delivery_info.generate_order()
            time.sleep(.5)
            account_info.generate_total()
            # begins the yes no while loop
            confirmation = None
            while confirmation not in ["y", "n"]:
                confirmation = input("Would you like accept this offer. Y/N ").lower()
                if confirmation == "y":
                    delivery_info.delivery_result()
                    print_slow("You delivered it in {} minutes.".format(delivery_info.delivery_time()) + "\n")
                    time.sleep(1)
                    break
                elif confirmation == "n":
                    print_slow("Here is you next order." + "\n")
                    new_delivery_info.generate_order()
                    time.sleep(.5)
                    account_info.generate_total()
                    time.sleep(1)
                    print_slow("You delivered it in {} minutes.".format(new_delivery_info.delivery_time()) + "\n")
                    time.sleep(1)
                    break
                else:
                    print("Please enter Y/N")  
            account_info.generate_deposit()           
            game_menu()       
        elif choice == "2":
            print_slow("You have ${} in your account".format(account_info.balance_total()) + "\n")
            game_menu()
        elif choice == "3":
            print_slow("Thank you for your interest, dont forget CosaNostra's 30 minutes or else delivery gaurentee.")
            time.sleep(1.75)
            print("   Goodbye!")
            sys.exit()
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

print_slow("Welcome to your option menu {}, below are a list of options to aid you".format(user_name) + "\n")
time.sleep(.5)

game_menu()