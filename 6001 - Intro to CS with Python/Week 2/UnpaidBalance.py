balance = 484

annualInterestRate = 0.2

monthlyPaymentRate = 0.04

numMonth = 0

# Write a program to calculate balance after one year if you only pay the monthly min

def calculator (x, r, p, n):
    """
    Inputs:
    
    x = initial balance on statement
    r = annual interest rate
    p = minimum monthly payment rate

    Outputs: Total remaining balance after 1 year (12 months) of paying the minimum

    """


    MinPayment = p*x

    RemBalance = x - MinPayment

    RemBalance = RemBalance + (r/12.0)*RemBalance
    
    n += 1
    if (n == 12): 
        return RemBalance

    else:
        return calculator(RemBalance, annualInterestRate, monthlyPaymentRate, n)

z = calculator(balance, annualInterestRate, monthlyPaymentRate, numMonth)

print("Remaining balance: " + str(round(z, 2)))



    



