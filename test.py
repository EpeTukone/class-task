GOLD = 'Gold'
SILVER = 'Silver'
def money_add(dict_, name_of_money, quantity):
    if name_of_money == GOLD:
        quantity_money = dict_.get(GOLD) + quantity
        print quantity, quantity_money
        dict_[GOLD] = 300

    if name_of_money == SILVER:
        quantity_money = dict_.get(SILVER) + int(quantity)
        dict_.get(SILVER, quantity_money)
    return dict_


dict_ = {'Silver': 100, 'Gold': 100}
print money_add(dict_, GOLD, 200)

