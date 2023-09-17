from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
works = True

money_machine.report()
coffee_maker.report()

while works:
    options = menu.get_items()
    request = input(f"What would you like?: ({options})")
    if request == 'off':
        works = False
    elif request == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(request)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)