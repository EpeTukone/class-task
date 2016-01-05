import json
import datetime

GOLD = 'Gold'
SILVER = 'Silver'
Log_pass = {'mail.@tut.by': '12WW34e'}

class Player(object):

    def __init__(self, email, password, name):
        self.email = str(email)
        self.password = str(password)
        self.name = str(name)
        self.session = []
        self.wallet = {}
        self.counter = {}

    def log_in(self, email, password):
        if email not in Log_pass:
            result = 'wrong email'
        if email in Log_pass:
            if Log_pass.get(email) != password:
                result = 'wrong password'
            if Log_pass.get(email) == password:
                result = 'the authentication is successful'
 #               session_begin = 
        return result




    def init_money(self, ):
        money_gold = Money(GOLD, 100)
        quantity_gold = money_gold.as_dict()
        money_silver = Money(SILVER, 100)
        quantity_silver = money_silver.as_dict()
        self.wallet = {GOLD: quantity_gold.get(GOLD),
                       SILVER: quantity_silver.get(SILVER)}



    def money_add(self, name_of_money, quantity):
        if name_of_money == GOLD:
            quantity_money = self.wallet.get(GOLD) + quantity
            self.wallet[GOLD] = quantity_money
        if name_of_money == SILVER:
            quantity_money = self.wallet.get(SILVER) + quantity
            self.wallet[SILVER] = quantity_money


    def money_remove(self, name_of_money, quantity):
        if name_of_money == GOLD:
            quantity_money = self.wallet.get(GOLD) - quantity
            self.wallet[GOLD] = quantity_money
        if name_of_money == SILVER:
            quantity_money = self.wallet.get(SILVER) - quantity
            self.wallet[SILVER] = quantity_money


    def __str__(self):
        format_str = 'email= "{}", password= "{}", name= "{}", wallet= "{}"'
        return format_str.format(self.email, self.password, self.name, self.wallet)

class Session(object):
    def __init__(self, id):
        self.id = int(id)
        self.start_time = None
        self.finish_time = None

    def start(self):
        self.start_time = datetime.datetime.now()

    def finish(self):
        self.finish_time = datetime.datetime.now()

class Money(object):
    def __init__(self, name_of_money, counter):
        self.name_of_money = name_of_money
        self.counter = counter

    def as_dict(self):
        dict_ = {
            str(self.name_of_money): self.counter
        }
        return dict_

    def __str__(self):
        return 'name of money: {}, quantity: {}'.format(self.name_of_money, self.counter)



if __name__ == "__main__":

####### create a new player ######
    player = Player('mail.@tut.by', '12WW34e', 'drednout')
    print 'Create new player:\n', player

###### authentication ######
    print player.log_in('mail.@tut.by', '12WW34e')

###### add money for a player with new account ######
    player.init_money()
    print 'Add money for a player with new account:\n', player

###### add money to player ######
    player.money_add(GOLD, 200)
    player.money_add(SILVER, 2000)
    print 'Add money to player:\n', player

###### remove money from player ######
    player.money_remove(GOLD, 50)
    player.money_remove(SILVER, 500)
    print 'Remove money from player:\n', player
