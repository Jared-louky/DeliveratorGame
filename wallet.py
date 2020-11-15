import random, math


class Wallet():
        
        def __init__(self, order_amount, *args, **kwargs):
            self.order_amount = order_amount
            self.order_amount = order_amount
            self.account = []

        def generate_total(self):
            print("Here is your order total ${}".format(self.order_amount))
                
        def deposit(self):
            for deposit in range(0, 1000): 
                deposit = ((self.order_amount * .15), 2)
                self.account.append(deposit)
            
            
        
        def statement(self):
            print("You have ${} in your account".format(sum(self.account)))