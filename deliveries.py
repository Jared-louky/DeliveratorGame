import time, sys, os, random, math


class Delivery():

    if __name__ == "__main__":

        def __init__(self, distance=random.randint(7, 35), rate=65, order_amount=round(random.randint(100,500), 2), **kwargs):
            self.distance = distance
            self.rate = rate
            self.order_amount = order_amount

        def payout(self): 
            payout = self.order_amount * .15
            return payout
            
        def generate_offer(self):
            print("Your delivery is for ${} and is {} miles away.".format(self.order_amount, self.distance))

        def confirm_offer(self):
            user_input = input("Would you like another delivery? Y?N  ")
            answer = False
            while answer == False:
                if user_input == "y" or user_input == "Y":
                    continue
                else:
                    answer = True
        

        def delivery_time(self):
            delivery_time = ((self.distance/self.rate)*60)
            return delivery_time

                
        def delivery_results(self):
                if  self.delivery_time <= 31:
                    print("The delivery has been conpeteled")
                    print("You have earned ${}.".format(self.payout))
                else:
                    print("You have not completed the delivery within 30 minutes, a termination team is on the way to your location.")
                    exit()