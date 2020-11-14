import time, sys, os, random, math


class OrderInfo():
    
    if __name__ == "__main__":
    
        def __init__(self, *args, **kwargs):
                    
            def distance(self):
                distance = random.randint(7, 35)
                print(distance)

            def rate(self):
                rate = 65
                print(rate)
            
            def order_amount(self):
                order_amount = round(random.randint(100,500), 2)
                print(order_amount)

            def delivery_time(self):
                delivery_time = ((distance/rate)*60)
                print(delivery_time)
            
            def delivery_result():
                if delivery_time <= 31:
                    print("You completed your delivery in {} minutes.".format(delivery_time))
                else:
                    print("You did not complete your delivery in 30 min. Goodbye")
                    
OrderInfo.distance()
OrderInfo.rate()
OrderInfo.order_amount()
OrderInfo.delivery_time()
OrderInfo.delivery_result()
