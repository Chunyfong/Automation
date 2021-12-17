from optionprice import Option

# Quick Calculation check for Long Side call or put option  
# Use HSI.388 for Example
HSI388 = Option(european=True,
                    kind='put',
                    s0 = 450,
                    k = 460,
                    t = 6,
                    sigma = 0.33,
                    r = 0.01,
                    dv = 0)
price = HSI388.getPrice()
print(f'{price:.2f}')
