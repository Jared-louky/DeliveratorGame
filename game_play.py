import time, sys, os, random, math


# Functions and variable for game play 

# These are my global variables, the do not hinge on any other varibale but are used in mutilple functions therefore should nor be localized 
distance = random.randint(7, 35) # global variable 
rate = 65 # global variable 
order_amount = round(random.randint(100,500), 2) # global variable 
delivery_time = math.ceil((distance/rate)*60)
account = [""] # a string with the ability to ammend and get a sum of all the numbers 
mileage = [""] # a string with the ability to ammend and get a sum of all the numbers 
payout = order_amount * .1


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
            return generate_offer()
        elif choice == "2":
            return balance()
        elif choice == "3":
            print("""Thank you for your interest, dont forget CosaNostra's 30 minutes or else delivery gaurentee. 
            Gooodbye.""")
            exit()
        else:
            print("Please choose a number listed") 
            return game_menu()           

def generate_offer():
    print("Your delivery is for ${} and is {} miles away.".format(order_amount, distance))

def new_offer():
    new_order_amount = round(random.randint(100,500), 2)
    new_distance = random.randint(7, 35)
    print("Your delivery is for ${} and is {} miles away.".format(new_order_amount, new_distance))

def confirm_offer():
    user_input = input("Would you like another delivery? Y?N  ").lower
    answer = False
    while answer == False:
        if user_input == "y":
            continue
        else:
            answer = True
        
        
def delivery_results():
        if  delivery_time <= 31:
            print("The delivery has been conpeteled")
            print("You have earned ${}.".format(payout))
        else:
            print("You have not completed the delivery within 30 minutes, a termination team is on the way to your location.")
            exit()
# has to do with player wallet
def balance():
        balance = sum(account.append(payout))
        print(balance)



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
time.sleep(1)

game_menu()





