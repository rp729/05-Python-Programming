'''Joe's Stocks'''
commission = 0.02
shares_purchased = 1000
share_price = 32.87
shares_sold = 1000
sold_price = 33.92

print(F"The amount of money Joe paid for the stock is ${shares_purchased*share_price:.2f}\
      \nThe amount of money Joe paid for the commission is ${shares_purchased*share_price*commission:.2f}\
      \nThe amount of money that Joe sold the stock is ${shares_sold*sold_price:.2f}\
      \nThe amount of commission Joe paid his broker when stocks sold is ${shares_sold*sold_price*commission:.2f}\
      \nThe net amount of Joe's investment is $\
{(shares_purchased*share_price*commission + shares_purchased*share_price) - (shares_sold*sold_price - shares_sold*sold_price*commission):.2f}")