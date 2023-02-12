print("Write how many ml of water the coffee machine has:")
water = int(input())
print("Write how many ml of milk the coffee machine has:")
milk = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
beans = int(input())
print("Write how many cups of coffee you will need:")
cups = int(input())

one_cup_supply = {water: 200, milk: 50, beans: 15}

water = water // one_cup_supply[water]
milk = milk // one_cup_supply[milk]
beans = beans // one_cup_supply[beans]

coffee_supply = min((water, milk, beans))

if coffee_supply == cups:
    print("Yes, I can make that amount of coffee")
elif coffee_supply > cups:
    print(f"Yes, I can make that amount of coffee (and even {coffee_supply - cups} more than that)")
else:
    print(f"No, I can make only {coffee_supply} cups of coffee")