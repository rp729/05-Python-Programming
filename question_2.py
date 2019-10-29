'''This program is designed to calculate the total profit of the projected sales'''


'''Receive user input and initialize variables.'''
projected_sales = float(input("Enter your projected amount of total sales:"))
profit = 0.23
total_profit = projected_sales*profit
revenue = projected_sales*profit + projected_sales

'''This is where the magic happens'''
print("Your projected profit will be ${:.2f} and your projected revenue will be ${:.2f}".format(total_profit,revenue))
