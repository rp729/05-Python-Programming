'''This program is designed to calculate the subtotal of items purchased.'''

'''User input for additional items.'''
def user_input():
    user_interaction = input("Do you have an item (or additional items) that you would like to purchase?")
    return user_interaction

'''User input for price of item.'''
def price():
    return float(input("Enter price of item:"))

tax = 0.06
sub_total = 0.0

'''Where the magic happens.'''
while True:
    user = user_input()
    if user.lower() == 'y'or user.lower() == 'yes':
        total = price()
        sub_total += total*tax + total
        print("Your subtotal is ${:.2f}".format(sub_total))
    else:
        print("Your final subtotal is ${:.2f}".format(sub_total))
        break

