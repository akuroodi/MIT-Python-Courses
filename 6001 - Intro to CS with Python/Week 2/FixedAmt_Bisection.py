balance = 999999

annualInterestRate = 0.18

lowerBound = balance / 12.0
upperBound = balance

def calculator (x, r, n, p, l, u):
    """
    Inputs:
    x = initial balance
    r = annual interest rate
    n = month counter
    p = fixed payment guess, starting with mid of two bounds
    l = lower bound
    h = upper bound

    Outputs: The monthly fixed payment to reduce x to <=0 in 12 months

    """
    
    for n in range(0,12):                               # calculates remaining balance after 12 months
        
        if (n == 0):
            balUnpaid = x - p
            balUnpaid = balUnpaid + balUnpaid*(r/12.0)
        else:
            balUnpaid = balUnpaid - p
            balUnpaid = balUnpaid + balUnpaid*(r/12.0)

        n += 1

    if (balUnpaid <=0 and abs(balUnpaid) < 1): return p      # return 'Goldilocks' payment p

    elif (balUnpaid > 0): 
        l = p
        return calculator(balance, r, 0, (l+u)/2, l, u) # increase payment, try again
    
    elif (balUnpaid < 0):                               # if you've paid TOO much
        u = p
        return calculator(balance, r, 0, (l+u)/2, l, u) # decrease payment, try again

 

z = calculator(balance, annualInterestRate, 0, (lowerBound+upperBound) / 2, lowerBound,upperBound)

print ("Lowest payment: " + str(round(z, 2)))
