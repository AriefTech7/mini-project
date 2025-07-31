MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

koin = {
    "quarters":0.25,
    "dimes":0.10,
    "nickles":0.05,
    "pennies":0.01
}

def callresources(bahan):
    income = 0
    air = bahan['water']
    susu = bahan['milk']
    kopi = bahan['coffee']
    return f"Water: {air}ml\nMilk: {susu}ml\nCoffee: {kopi}g\nMoney: ${income}"



def checkingredients(bahan, coffee):
    ingredients = MENU[coffee]['ingredients']
    for bahan2 in ingredients:
        if bahan[bahan2] > ingredients[bahan2]:
            return 'good'
        else:
            return 'not good'


def make_a_coffee(bahan, coffee):
    ingredients = MENU[coffee]['ingredients']
    for resep in ingredients:
        hasil = bahan[resep] - ingredients[resep]
        bahan[resep] = hasil

def terkecil(sumber):
    key, value = min(sumber.items(), key=lambda x: x[1])
    return key
# TODO: 5. Process coins.
def calculate_coin(querters, dimes, nickles, pennies):

    quarter = koin['quarters'] * float(querters)
    dime = koin['dimes'] * float(dimes)
    nickle = koin['nickles'] * float(nickles)
    pennie = koin['pennies'] * float(pennies)

    result = quarter + dime + nickle + pennie
    return f"${result}"

# TODO: 6. Check transaction successful?
def check_transaction(money, mymoney):
    if money <  MENU['latte']['cost']:
        return "Sorry that's not enough money. Money refunded."
    else:




def machinecoffee():
    start = True
    income = 0
    while start:
        # TODO: 1.Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
        menu = input("What would you like? (espresso/latte/cappuccino): ").lower()
        # TODO: 2.Turn off the Coffee Machine by entering “ off ” to the prompt.
        if menu == 'off':
            start = False
        # TODO: 3.Print report
        elif menu == 'report':
            print(callresources(resources))
        # TODO: 4. Check resources sufficient?
        elif menu == 'latte':
            print("Please insert coins.")
            koin_q = input("How many quarters?: ")
            koin_d = input("How many dimes?: ")
            koin_n = input("How many nickles?: ")
            koin_p = input("How many pennies?: ")

            money_customer = calculate_coin(koin_q, koin_d, koin_n, koin_p)
            check_transaction(money_customer, income)
            if checkingredients(resources, 'latte') == 'good':
                make_a_coffee(resources, 'latte')
            elif checkingredients(resources, 'latte') == 'not good':
                print(f"Sorry there is not enough {terkecil(resources)}.")

        elif menu == 'espresso':
            print("Please insert coins.")
            koin_q = input("How many quarters?: ")
            koin_d = input("How many dimes?: ")
            koin_n = input("How many nickles?: ")
            koin_p = input("How many pennies?: ")
            money_customer = calculate_coin(koin_q, koin_d, koin_n, koin_p)
            if checkingredients(resources, 'espresso') == 'good':
                make_a_coffee(resources, 'espresso')
            elif checkingredients(resources, 'espresso') == 'not good':
                print(f"Sorry there is not enough {terkecil(resources)}.")

        elif menu == 'cappuccino':
            print("Please insert coins.")
            koin_q = input("How many quarters?: ")
            koin_d = input("How many dimes?: ")
            koin_n = input("How many nickles?: ")
            koin_p = input("How many pennies?: ")
            money_customer = calculate_coin(koin_q, koin_d, koin_n, koin_p)
            if checkingredients(resources, 'cappuccino') == 'good':
                make_a_coffee(resources, 'cappuccino')
            elif checkingredients(resources, 'cappuccino') == 'not good':
                print(f"Sorry there is not enough {terkecil(resources)}.")



machinecoffee()