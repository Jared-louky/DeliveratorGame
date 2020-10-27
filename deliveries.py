import random 
import time 
import math 

# Sets the information needed for Delivery and Fuel
distance = random.randint(5, 35)
rate = 65
time = math.ceil((distance / rate ) * 60)
cash = ""


# Contains all the information and caculations needed for one delivery 
class Delivery():
    def __init__(self, distance, rate, time, credits, **kwargs):
        self.distance = distance
        self.rate = rate 
        self.time = time
        self.cash = cash

# Returns length of drive time 
    def delivery_time(self):
        return self.time

# Returns the amount of order 
    def order_amount(self):
        print("The order is for ${}".format(random.randint(100,500)))
        
# Prints out all the order information
    def delivery_info(self):
        print("Your delivery is {} miles away.".format(self.distance))
        print(self.order_amount())
        
# Returns the amount of cash player recives for delivery 
    def pay_out(self):
        # pay = (distance * 10)
        # tip = (order_amount * .2)
            #if self.time =< 27:
                # tip = (order_amount * .2)
            #else:
                # tip == 0
        pass
        
        




