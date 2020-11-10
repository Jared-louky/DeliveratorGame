import random, time, math


# These are my global variables, the do not hinge on any other varibale but are used in mutilple functions therefore should nor be localized 
distance = random.randint(7, 35) # global variable 
rate = 65 # global variable 
order_amount = round(random.randint(100,500), 2) # global variable 
payout = order_amount * .15

cash = [""] # a string with the ability to ammend and get a sum of all the numbers 
mileage = [""] # a string with the ability to ammend and get a sum of all the numbers 




class Delivery():

    def delivery_time(self):
        time = math.ceil((distance/rate)*60)
        return time 

    def delivery_info(self, order_amount, distance):
        print("The delivery total is ${} and is {} miles away".format(order_amount, distance))

    def delivery_outcome(self, payout):
        print("Congradulations you have completed and have earned ${}.".format(payout))

    def delivery_results(self, delivery_time, delivery_outcome):
        if delivery_time > 30:
            delivery_outcome()
        else:
            print("You have not completed the delivery within 30 minutes, a termination team is on the way to your location.")
            exit()

# class Wallet():
#     account = cash.append(payout)
#     statement = sum(account)
#     print("You have ${} in your account".format(statement))