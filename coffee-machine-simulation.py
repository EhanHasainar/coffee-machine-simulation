MENU = {
    "espresso": {"ingredients": {"water": 50, "milk":0, "coffee": 18},"cost": 1.5,},
    "latte": {"ingredients": {"water": 200,"milk": 150,"coffee": 24,},"cost": 2.5,},
    "cappuccino": {"ingredients": {"water": 250,"milk": 100,"coffee": 24,},"cost": 3.0,}
}

resources = {'water': 800, 'milk': 500, 'coffee': 200, 'money': 0,}

off = True

promt = input("What would you like? (espresso/latte/cappuccino): ")
print()

while off is True:
    if promt == 'report':
        for key in resources:
            print(f"{key}: {resources[key]}")
            print()
    else:
        money = float(input('Input the money: $'))
        print()

        # Check if we have enough resource for coffee

        if promt == 'latte' or promt == 'espresso' or promt == 'cappuccino':
            resources_enough = True
            if promt == "espresso":
                if resources['water'] < MENU[promt]['ingredients']['water']:
                    print('Water not enough for espresso')
                    resources_enough = False
                    print()
                if resources['coffee'] < MENU[promt]['ingredients']['coffee']:
                    print('Coffee not enough for espresso')
                    resources_enough = False
                    print()

            elif promt == "latte":
                if resources['water'] < MENU[promt]['ingredients']['water']:
                    print('Water not enough for latte')
                    resources_enough = False
                    print()
                if resources['coffee'] < MENU[promt]['ingredients']['coffee']:
                    print('Coffee not enough for latte')
                    resources_enough = False
                    print()
                if resources['milk'] < MENU[promt]['ingredients']['milk']:
                    print("Milk not enough for latte")
                    resources_enough = False
                    print()

            elif promt == "cappuccino":
                if resources['water'] < MENU[promt]['ingredients']['water']:
                    print('Water not enough for cappuccino')
                    resources_enough = False
                    print()
                if resources['coffee'] < MENU[promt]['ingredients']['coffee']:
                    print('Coffee not enough for cappuccino')
                    resources_enough = False
                    print()
                if resources['milk'] < MENU[promt]['ingredients']['milk']:
                    print('Milk not enough for cappuccino')
                    resources_enough = False
                    print()

        else:
            print("Didn't Get that")
            resources_enough = False
            print()

        # Check if the money provided is enough or is there any change to give back

        money_enough = False

        if resources_enough is True:
            if money < MENU[promt]['cost']:
                print("Money not enough for", promt)
                money_enough = False
                print()
            elif money > MENU[promt]['cost']:
                print(f"Your change is ${money-(MENU[promt]['cost'])}")
                resources['money'] +=MENU[promt]['cost']
                money_enough = True
                print()
            elif money == MENU[promt]['cost']:
                print('Perfect amount')
                resources['money'] +=money
                money_enough = True
                print()
            else:
                print("Didn't get that")
                money_enough = False
                print()

        # Make coffee and then consume the resources
        if money_enough is True:
            resources['water'] -= MENU[promt]['ingredients']['water']

            resources['milk'] -= MENU[promt]['ingredients']['milk']

            resources['coffee'] -= MENU[promt]['ingredients']['coffee']

            print(f"Here is your hot {promt}")
            print()

    promt = input("What would you like? (espresso/latte/cappuccino): ")
    print()

    if promt == 'off':
        off = False



