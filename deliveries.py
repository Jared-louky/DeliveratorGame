import random, time, math

# 
class GenerateOffer():
    distance = random.randint(7, 35)
    rate = 65
    time = math.ceil((distance / rate ) * 60)
    order_amount = round(random.randint(100,500), 2)
    payout = order_amount * .15
    bank = ["0"]
    milage = ["0"]
    
    if __name__ == "__main__":

        # Give the player information about the deliver 
        def order_info(self, distance, order_amount):
            print("Your destination is {} miles away.".format(distance))
            print("The order is for ${}.".format(order_amount))
        
        # Allows the player to decide if they would like to continue with the order or choose another
        def order_conformation(self, order_info):
            confirm = input("Woudl you like to accept this delivery? Y/N  ").lower 
            while False:
                if confirm == "y":
                    continue
                elif confirm == "n":
                    order_info()
                else:
                    print("Please choose Y or N")
        
        # informs the player how well they did with the order, and if they completed it in the right amountof time
        def order_completion(self, payout, bank, distance, time):
            if time < 30:
                print("Congradulations you completed your delivery and made ${}.".format(payout))
                bank = bank.append(bank)
                milage = milage.append(distance)
            else:
                print("I'm sorry you did not cmplete the delivery in the time alotted, our termination team is on the way to you location")
                exit()
        # 
        def bank_statement(self, bank):
            pass
            #print("You currently have ${} credits in your account.".format.sum(bank))

        def odometer(self, milage):
            pass
            #print("You have traveled {} miles.".format(milage)) 
            


