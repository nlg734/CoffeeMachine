# coffee_machine.py
# written by Natasha Graham
# JetBrains Python academy


def main():
    print("Write how many cups of coffee you will need:")
    n_cups = int(input())
    print("For", n_cups, "cups of coffee you will need:")
    print((n_cups * 200), "ml of water")
    print((n_cups * 50), "ml of milk")
    print((n_cups * 15), "g of coffee beans")


main()
