# Write a function that returns the length of the longest run of increasing ints
# Monotonically increasing --> k+1 is >= k

def longestRun(L):
    """
    Input: a list L of integers

    Output: the length of the longest monotonically increasing run within L
    """
    counter = 1
    results = [1]
    for i in range (len(L)-1):
        if L[i] <= L[i+1]:
            counter += 1
        else: 
            results.append(counter)
            counter = 1
    
    results.append(counter)
    return max(results)



L = [-10, -5, 0, 5, 10]

print(longestRun(L))