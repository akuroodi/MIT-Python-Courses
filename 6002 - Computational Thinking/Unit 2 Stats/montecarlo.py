import random
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    success = 0
    bucket = [1,1,1,0,0,0] # reds = 1, greens = 0
    for i in range(numTrials):
       
        picked = pickBalls(bucket)

        if sum(picked) == 0 or sum(picked) == 3:        #means you picked 3 of the same kind
            success+=1


    return success / numTrials


def pickBalls(bucket):
    """
    Takes in a list representing bucket of balls, and randomly picks 3 w/o replacement

    Returns a list of the picks
    """

    #picked = []
    #pick = 0

    # for i in range(3):
    #     pick = (random.choice(bucket))
    #     bucket.remove(pick)
    #     picked.append(pick)
    
    # Alternatively, can use random.sample() to sample without replacement
    picked = (random.sample(bucket, 3))
    
    return picked

        
    
print(noReplacementSimulation(5))