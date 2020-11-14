from deliveries import Delivery

delivery_info = Delivery() 

class Wallet():
    
    def __init__(self, commission, **kwargs):
        self.commission = commission
        
    def payout(self):
        payout = delivery_info.order_amount * self.commission
        return payout
        
        

    def payout_deposit(self):
        account = []
        account = account.append()
        print(account)




