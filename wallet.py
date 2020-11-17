import random, math



class Wallet():
    
        
    def __init__(self, order_amount, *args, **kwargs):
        self.order_amount = order_amount
        self.balance = []

#sets the value for player pay       
    def tip_out(self):
        tip_out = random.randint(30,150)
        return tip_out
    
    def pay_out(self):
        delivery_fee = 15.0
        pay_out = self.tip_out() + delivery_fee
        return pay_out
    
    def pay_out_alert(self):
        pay_out_alert = self.pay_out()
        return pay_out_alert
    
    def generate_deposit(self):
            deposit = self.pay_out_alert()
            self.balance.append(deposit)
            print("You earned ${}".format(deposit))
                    
    def balance_total(self):
        balance_statement = sum(self.balance)
        return balance_statement

    def generate_total(self):
        print("Here is your order total ${}".format(self.order_amount))
    
      
        
