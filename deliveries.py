import random 
import time 
import math 
import datetime

#class Delivery():
distance = random.randint(7, 35)
rate = 65
time = math.ceil((distance / rate ) * 60)
order_amount = random.randint(100,500)
payout = order_amount * .15

#    def __init__(self, distance, rate, time, order_amount, payout, *args, **kwargs):
#        self.distance = distance
#        self.rate = rate
#        self.time = time
#        self.order_amount = order_amount
#        self.payout = payout


def order_info():
    print("Your destination is {} miles away.".format(distance))
    print("The order total is ${}.".format(order_amount))

def order_completion():
    while True:
        if time <= 30:
            print("Congradulations you have completed the order, and you have earned ${}.".format(payout))
            break
        else:
            print("You have gone over the delivery time, prepare for termination")
            break

def new_order():
    print("Your destination is {} miles away.".format(distance))
    print("The order total is ${}.".format(order_amount))
