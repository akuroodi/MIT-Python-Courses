import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title:
        pylab.title(title)

    pylab.show()
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    runs = []
    while numTrials > 0:
        # For each trial, simulate rolling the die and tally the longest run you get
        counter = 1
        currvalue = die.roll()
        valueList = [1]

        for i in range(numRolls-1):     # for each remaining roll
            newRoll = die.roll()
            if newRoll == currvalue:
                counter += 1
                if i == numRolls-2: valueList.append(counter)
                continue
            else:
                valueList.append(counter)       # keep track of multiple streaks in 1 sim
                currvalue = newRoll
                counter = 1
        
        runs.append(max(valueList))
        numTrials -=1
    
    makeHistogram(runs, 10, "Longest Run", "Frequency", "Die Run Distribution")

    return round(getMeanAndStd(runs)[0], 3)
                
            

    
# One test case
print (getAverage(Die([1]), 10, 1000))


