# Assume d1 and d2 are two dictionaries with integer keys and values

# Assume f(a,b) is a given function that takes in 2 ints and
# returns the result of an unknown operation on them

# Write function dict_interdiff(d1,d2) that returns a tuple of 2 dicts
# Dict1: Only common keys in d1,d2 where their values are f(k1,k2)
# Dict2: KV pairs that are only either in d1 or d2

def f(a,b):
    """
    Inputs: two integers a,b
    Output: result of a "random" operation on these two ints
    """
    return a+b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    
    # Get the common keys for d1, d2 to start your interest dict

    L = [key for key in d1.keys() if key in d2.keys()]
    
    # Assign each common key to a new value based on f(a,b)

    intersect = {}
    for key in L:
        intersect[key] = f(d1[key], d2[key])
    
    # Create your difference dictionary (all KV pairs for uncommon keys)
    diff = {}
    for key in d1.keys():
        if key not in d2.keys():
            diff[key] = d1[key]
    for key in d2.keys():
        if key not in d1.keys():
            diff[key] = d2[key]
    
    return (intersect, diff)     
    

d1 = {1:2, 2:4, 3:6, 4:8}
d2 = {0:1, 1:5, 4:4, 5:5}

print(dict_interdiff(d1,d2))
    
    