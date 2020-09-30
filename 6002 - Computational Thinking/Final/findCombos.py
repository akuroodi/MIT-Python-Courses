import pylab

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """

    result = pylab.zeros(len(choices), dtype=int)
    choices2 = choices[:]

    sum = 0 

    while (sum <= total and choices2):
        maxnum = max(choices2)
        maxIndex = choices.index(maxnum)

        if (sum + maxnum) <= total:
            sum += maxnum
            result[maxIndex] = 1
            choices[maxIndex] = 0
            choices2.remove(maxnum)
        else:
            choices2.remove(maxnum)


    
    return result

choices = [10, 10, 11, 11, 11]      # the greedy algorithm above doesn't work for this list
total = 20

print(find_combination(choices,total))
