def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    if (len(L) == 0): return 0
    
    x = 0

    while (x < len(L)):
    
        if ( f(L[x]) == False):
            del(L[x])
            continue

        x += 1

    return x


def f(s):
    return 'a' in s

# L = ["a"]
# L = [""]
L = ["a", "b", "c", "d"]
# L = ["f", "b", "a", "d"]
# L = ["a", "b", "a", "d"]
# L = ["a", "b", "c", "a"]
# L = ["y", "b", "c", "d"]

print("Count is: " + str( satisfiesF(L) ) )






    