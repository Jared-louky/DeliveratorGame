import time, sys, os, random, math


class OrderInfo():

        def __init__(self, distance, rate):
            self.distance = distance
            self.rate = rate
        
        def generate_order(self):
            print("Your delivery is {} miles away.".format(self.distance))
            

        def delivery_time(self):
            delivery_time = ((self.distance/self.rate)*60)
            return delivery_time

        def delivery_result(self):
            if self.delivery_time <= 30:
                print("You completed your delivery in {} minutes.".format(self.delivery_time))
            else:
                print("You did not complete your delivery in 30 min. Goodbye")
                exit()
                            

