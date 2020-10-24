# Use a generator to spit out a list of successive primes each time it's called



# def genPrimes():
#     primes = []
#     x = 2                   #
#     primes.append(x)        #initialize list with first prime number
#     while(True):
#         for i in reversed(primes):      # traverse list backwards

#             if (x % i == 0):            # x is divisible by i, proceed to next candidate
#                 break
#             if (i != 0 and i != 2):     # x isn't divisible by i, go down list to next prime
#                 continue
            
#             if (x % i != 0):
#                 yield x
#                 primes.append(x)

#         if (x == 2): yield x            # catch initial case where you start at 2
#         x += 1              


# Alternate implementation to genPrimes() using built-in all() function

def genPrimes():
    primes = []
    yield 2
    n = 3

    while True:
        if all((n % pri != 0) for pri in primes):  # n shouldn't be divisible by any prior primes
            primes.append(n)
            yield n
        n += 2  # even --> non-prime


x = genPrimes()

for i in range(9):
    print (x.__next__())


# def genFib():
#     fib1 = 1
#     fib2 = 0

#     while(True):
#         next = fib1 + fib2
#         yield next
#         fib2 = fib1
#         fib1 = next

# x = genFib()

# for i in range(3):
#     print (x.__next__())
