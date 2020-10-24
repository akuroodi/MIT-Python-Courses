balance = 150

annualInterestRate = 0.2



def calculator (x, r, n, p):
    """
    Inputs:
    x = initial balance
    r = annual interest rate

    Outputs: The monthly fixed payment to reduce x to <=0 in 12 months

    """
    
    for n in range(0,12):
        
        if (n == 0):
            balUnpaid = x - p
            balUnpaid = balUnpaid + balUnpaid*(r/12.0)
        else:
            balUnpaid = balUnpaid - p
            balUnpaid = balUnpaid + balUnpaid*(r/12.0)

        n += 1

    if (balUnpaid <= 0): return p

    else: 
        return calculator(balance, r, 0, p+10)

z = calculator(balance, annualInterestRate, 0, p=10)

print ("Lowest payment: " + str(round(z, 2)))
