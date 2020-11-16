import random, math
from math import fsum


class Wallet():
    
        
    def __init__(self, order_amount, *args, **kwargs):
        self.order_amount = order_amount
        self.balance = []
        
    def pay_out(self):
        pay_out = round(self.order_amount * .15, 2)
        return pay_out

    def generate_total(self):
        print("Here is your order total ${}".format(self.order_amount))
    
    def pay_alert(self):
        print("You have received ${}.".format(self.balance))    
            
    def deposit(self):
        for d in self.balance:      
            deposit = self.pay_out
            self.balance.append(deposit)
            
    def statement(self):
        statement = sum(self.balance)
        return statement
    