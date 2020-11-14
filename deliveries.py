import time, sys, os, random, math


class OrderInfo():

    if __name__ == "__main__":
        
        def __init__(self, delivery_distance, delivery_rate, *args, **kwargs):
            self.delivery_distance = delivery_distance
            self.delivery_rate = delivery_rate
                    
            def order_amount(self):
                order_amount = round(self.distance * 25)
                return order_amount
            
            def generate_order(self):
                print("Your delivery is for ${} and is {} miles away.".format(self.order_amount, self.distance))

            def delivery_time(self):
                delivery_time = ((self.distance/self.rate)*60)
                return delivery_time

            def delivery_result(self):
                if delivery_time <= 31:
                    print("You completed your delivery in {} minutes.".format(self.delivery_time))
                else:
                    print("You did not complete your delivery in 30 min. Goodbye")
                                

