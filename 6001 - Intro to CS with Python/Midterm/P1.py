# Write a recursive function that counts how many "7"s appear in N

# x // 10 chops of last digit of a number

# x % 10 provides last digit of a number


def count7(N):
    '''
    N: a non-negative integer
    '''
    if (len(str(N)) == 1):
        if (N == 7): return 1
        return 0

    if (N % 10) == 7: return 1 + count7(N//10)

    else: return count7(N//10)

print (count7(124143445777))