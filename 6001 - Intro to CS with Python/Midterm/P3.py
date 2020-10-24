# Write a function that returns a list of keys with the target value in aDict
# Assume both keys and values are integers
# The list should be sorted in increasing order
# Return empty list of aDict does not contain target value



def keysWithValue(aDict, target):
    '''
    Inputs:

        aDict: a dictionary
        target: an integer

    Outputs:
        L: a list of keys mapped to the target, sorted in ascending order
    '''
    L = []
    for key in aDict.keys():
        if (aDict[key] == target):
            L.append(key)
            
    L.sort()
    return L


d = { 1:4, 2:5, 3:6, 0:4, -3:4, 5:-5}
c = { 1:2, 0:0, -4:1}

print( keysWithValue(c, 4) )

