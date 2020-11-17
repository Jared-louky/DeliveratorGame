import time, sys, os, random, math

from wallet import Wallet



class OrderInfo():

        def __init__(self, distance, rate):
            self.distance = distance
            self.rate = rate
        
# lets the player know how far the delivery is         
        def generate_order(self):
            print("Your delivery is {} miles away.".format(self.distance))
            
            
# sets the time it took to deliver the order
        def delivery_time(self):
            delivery_time = int(self.distance/self.rate *60)
            return delivery_time

# determinds if the delivery is within the delivery time alotted 
        def delivery_result(self):
            if self.delivery_time() < 31:
                print("Delivery complete")
            else:
                print("You did not complete your delivery in 30 min.")
                sys.exit()
                            

