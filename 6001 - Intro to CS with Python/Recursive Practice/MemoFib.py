# Recursive implemntation of a Fibonacci algorithm using basic memoization to quicken run time

def fastFib(n, memo = {}):
    """ Assume n is an int >=0 and memo is used only by recursive calls """

    if n == 0 or n == 1: return 1       # base case

    try:
        return memo[n]
    
    except KeyError:                    # if fib(n) not in our dict, compute it and add it
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result


print(fastFib(12))