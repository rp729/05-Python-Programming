'''This program is designed to find the distance of a car with an alloted time.'''

'''Variable initialization'''
speed = 60
hours_5 = speed*5
hours_8 = speed*8
hours_12 = speed*12

'''User input'''
user_input = input("Would you like to see the distance of a car traveled in 5, 8, and 12 hours?:")
time = user_input

if time.lower() == 'y' or time.lower() == 'yes':
    print(F"Distance in 5 hours is {hours_5}\
          \nDistance in 8 hours is {hours_8}\
          \nDistance in 12 hours is {hours_12}")
else:
    print("Good bye.")