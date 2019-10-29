'''Restaurant Bill'''

'''User input'''
food_cost = float(input("Enter the price of the food you ate:"))

'''Output'''
print(F"Your tip amount will be ${food_cost*0.15:.2f}\
      \nYour tax amount will be ${food_cost*0.07:.2f}\
      \nYour total amount is ${food_cost*0.15 + food_cost*0.07 + food_cost:.2f}")