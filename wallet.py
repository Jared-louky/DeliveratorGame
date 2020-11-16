import random, math


class Wallet():
    
        
    def __init__(self, order_amount, *args, **kwargs):
        self.order_amount = order_amount
        self.balance = []
        

    def generate_total(self):
        print("Here is your order total ${}".format(self.order_amount))
        
    def payout(self):
        payout = (self.order_amount * .15)
        return payout
    
    def pay_alert(self):
        print("You have received ${}.".format(self.payout))    
            
    def deposit(self):
        for deposit in self.balance:      
            amount = self.payout
            self.balance.append(amount)
        return self.balance
        
        
    def statement(self):
        print("You have ${} in your account".format(sum(self.balance)))