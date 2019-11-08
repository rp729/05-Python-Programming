'''Global Identifiers'''
BASE_HOURS = 40
OT_MULTIPLIER = 1.5

'''Main Function'''
def Main():
    hours_worked = float(input('Enter the number of hours worked:'))
    pay_rate = float(input('Enter the hourly pay rate:'))

    if hours_worked > BASE_HOURS:
        pay_OT = (hours_worked - BASE_HOURS) * OT_MULTIPLIER * pay_rate
        return F"You worked overtime! Your total pay is ${pay_OT + (BASE_HOURS*pay_rate):.2f}"
    else:
        return F"Your total pay is ${hours_worked*pay_rate:.2f}"

print(Main())