# coffee_machine.py
# written by Natasha Graham
# JetBrains Python academy


water_per = 200
milk_per = 50
beans_per = 15


def main():
    print("Write how many ml of water the coffee machine has:")
    ml_water = int(input())
    print("Write how many ml of milk the coffee machine has:")
    ml_milk = int(input())
    print("Write how many grams of coffee beans the coffee machine has:")
    g_beans = int(input())
    print("Write how many cups of coffee you will need:")
    n_cups = int(input())

    count = 0

    while ml_water > 0 and ml_milk > 0 and g_beans > 0:
        ml_water -= water_per
        ml_milk -= milk_per
        g_beans -= beans_per
        if ml_water >= 0 and ml_milk >= 0 and g_beans >= 0:
         count += 1

    if count == n_cups:
        print("Yes, I can make that amount of coffee")
    if count > n_cups:
        print("Yes, I can make that amount of coffee (and even",
              count - n_cups, "more than that)")
    if count < n_cups:
        print("No, I can only make", count, "cup(s) of coffee")

main()
