import time
import sys


from deliveries import Delivery 


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

user_name = input("What is your name?   ")

print_slow("""
Hello {}
Welcome to CosaNostra delivery simulation. 
""".format(user_name))

def try_again():
    pass



question = input("Would you like to continue?Y/N ")
if question == ("N").lower:
    print_slow("""
Thank you for your interest 
    """)
elif question == ("Y").lower:
    print_slow("Preparing simulation")
    time.sleep(.8)
    game_start()


def game_start(): 
    print_slow("""
    Here is the information about your first order
    """)
    if __name__ == "__main__":
        Delivery.delivery_info()
