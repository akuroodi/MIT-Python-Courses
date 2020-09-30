# Example of a recursive search tree algorithm that can be used to find global max to a 0/1 knapsack problem
# Note that we don't actually need to build the tree with node objects and such, just use result to house best result so far
# This is an exponential 2^n complexity search

def maxVal(toConsider, avail):
    """
    Assumes toConsider a list of items, avail a weight
    Returns a tuples of the total value of a solution to the 0/1 knapsack
    problem and the items of that solution
    """

    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        # Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        # Explore left branch
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getCost())
        withVal += nextItem.getValue()
        # Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        # Explore better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result