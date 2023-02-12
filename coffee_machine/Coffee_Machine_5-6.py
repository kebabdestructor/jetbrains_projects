# amount of ingredients needed for 1 cup of coffee and its price depending on its type
espresso = {'water': 250, 'beans': 16, 'money': 4}
latte = {'water': 350, 'milk': 75, 'beans': 20, 'money': 7}
cappuccino = {'water': 200, 'milk': 100, 'beans': 12, 'money': 6}

coffee_type = {1: espresso, 2: latte, 3: cappuccino}

# intial coffee machine stock
stock = {'water': 400, 'milk': 540, 'beans': 120, 'cups': 9, 'money': 550}

def buy_coffee(coffee):
    # checking if sufficient quantity of ingredients is available in stock
    for item, quantity in coffee.items():
        if item == 'money': 
            continue
        elif stock[item] < quantity:
            return print(f'Sorry, not enough {item}!')

    # deduct amount of respective ingredients in stock and add money
    for key, value in coffee.items():
        if key == 'money': 
            stock[key] = stock[key] + value
        else:
            stock[key] = stock[key] - value
    stock['cups'] -= 1

def print_stock():
    print('\nThe coffee machine has:')
    print(f'{stock["water"]} ml of water')
    print(f'{stock["milk"]} ml of milk')
    print(f'{stock["beans"]} g of coffee beans')
    print(f'{stock["cups"]} disposable cups')
    print(f'{stock["money"]} of money')
    return

def fill_coffee_machine():
    replenish = {'water': 0, 'milk': 0, 'beans': 0, 'cups': 0}
    print('Write how many ml of water you want to add:')
    replenish['water'] = int(input())
    print('Write how many ml of milk you want to add:')
    replenish['milk'] = int(input())
    print('Write how many grams of coffee beans you want to add:')
    replenish['beans'] = int(input())
    print('Write how many disposable cups you want to add:')
    replenish['cups'] = int(input())

    for key, value in replenish.items():
        stock[key] = stock[key] + value

def withdraw_cash():
    print(f'\nI gave you ${stock["money"]}')
    stock['money'] = 0

def select_coffee():
    print('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    try: 
        coffee = int(input())
        return buy_coffee(coffee_type[coffee])
    except ValueError:
        return main()

def main():
    print('\nWrite action (buy, fill, take, remaining, exit):')
    user_input = input()
    if user_input == 'buy':
        select_coffee()
    elif user_input == 'fill':
        fill_coffee_machine()
    elif user_input == 'take':
        withdraw_cash()
    elif user_input == 'remaining':
        print_stock()
    elif user_input == 'exit':
        exit()
    return main()

if __name__ == '__main__':
    main()