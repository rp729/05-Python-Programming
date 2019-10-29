'''Tax calculation'''

puchase_amount = float(input("Enter purhcase amount:"))
state_tax = 0.04
county_tax = 0.02

print(f"The state tax is ${state_tax*puchase_amount:.2f}\
      \nThe county tax is ${county_tax*puchase_amount:.2f}\
      \nThe total amount is ${state_tax*puchase_amount + county_tax*puchase_amount + puchase_amount:.2f}")