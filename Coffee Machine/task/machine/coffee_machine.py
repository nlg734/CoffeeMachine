# coffee_machine.py
# written by Natasha Graham
# JetBrains Python academy


water_espresso = 250
milk_espresso = 0
beans_espresso = 16
cost_espresso = 4

water_latte = 350
milk_latte = 75
beans_latte = 20
cost_latte = 7

water_capp = 200
milk_capp = 100
beans_capp = 12
cost_capp = 6


def coffee_status(w, mi, b, c, mo):
    return "The coffee machine has:\n{} of water\n" \
           "{} of milk\n{} of coffee beans\n{} of disposable cups\n" \
           "{} of money".format(w, mi, b, c, mo)


def fill():
    fills = []
    print("Write how many ml of water do you want to add:")
    fills.append(int(input()))
    print("Write how many ml of milk do you want to add:")
    fills.append(int(input()))
    print("Write how many grams of coffee beans do you want to add:")
    fills.append(int(input()))
    print("Write how many disposable cups of coffee do you want to add:")
    fills.append(int(input()))

    return fills


def check_resources(w, mi, b, choice):
    if choice == 1:
        if w < water_espresso:
            return "Sorry, not enough water"
        if mi < milk_espresso:
            return "Sorry, not enough milk"
        if b < beans_espresso:
            return "Sorry, not enough beans"
        return -1
    elif choice == 2:
        if w < water_latte:
            return "Sorry, not enough water"
        if mi < milk_latte:
            return "Sorry, not enough milk"
        if b < beans_latte:
            return "Sorry, not enough beans"
        return -1
    else:
        if w < water_capp:
            return "Sorry, not enough water"
        if mi < milk_capp:
            return "Sorry, not enough milk"
        if b < beans_capp:
            return "Sorry, not enough beans"
        return -1

def main():
    avail_water = 400
    avail_milk = 540
    avail_beans = 120
    avail_cups = 9
    money = 550

    while True:
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        print()

        if action == "exit":
            break
        elif action == "remaining":
            print(coffee_status(avail_water, avail_milk, avail_beans, avail_cups, money))
            print()
        elif action == "take":
            print("I give you ${}".format(money))
            money = 0
        elif action == "fill":
            filler = fill()
            avail_water += filler[0]
            avail_milk += filler[1]
            avail_beans += filler[2]
            avail_cups += filler[3]
        elif action == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
            choice = input()
            if choice == "back":
                continue
            choice = int(choice)
            if avail_cups == 0:
                print("Sorry, not enough cups")
                continue
            result = check_resources(avail_water, avail_milk, avail_beans, choice)
            if choice == 1 and result == -1:
                avail_water -= water_espresso
                avail_beans -= beans_espresso
                avail_milk -= milk_espresso
                money += cost_espresso
                avail_cups -= 1
            elif choice == 2 and result == -1:
                avail_water -= water_latte
                avail_beans -= beans_latte
                avail_milk -= milk_latte
                money += cost_latte
                avail_cups -= 1
            elif choice == 3 and result == -1:
                avail_water -= water_capp
                avail_beans -= beans_capp
                avail_milk -= milk_capp
                money += cost_capp
                avail_cups -= 1
            else:
                print(result)

        print()


main()
