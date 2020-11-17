import random, math



class Wallet():
    
        
    def __init__(self, order_amount, *args, **kwargs):
        self.order_amount = order_amount
        self.balance = []

#sets the value for player pay       
    def pay_out(self):
        pay_out = round(random.randint(int(self.order_amount * .2), int(self.order_amount * .35)))# random reasonable tip percentant plus delivery charge
        return pay_out
    
    def generate_deposit(self):
            deposit = self.pay_out()
            self.balance.append(deposit)
            
    def balance_total(self):
        balance_statement = sum(self.balance)
        return balance_statement

    def generate_total(self):
        print("Here is your order total ${}".format(self.order_amount))
    
    def pay_alert(self):
        print("You have received ${}.".format(self.pay_out))  
        
