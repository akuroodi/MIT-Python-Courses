# Write a recursive function that gives sum of the digits in N



def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    if (len(str(N)) == 1):
        return N

    else: 
        return (N % 10) + sumDigits(N//10)

print ( sumDigits(15423) )
    