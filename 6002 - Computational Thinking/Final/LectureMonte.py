import random
        
class Lecture(object):
    def __init__(self, listen, sleep, fb):
        self.listen = listen
        self.sleep = sleep
        self.fb = fb
    def get_listen_prob(self):
        return self.listen
    def get_sleep_prob(self):
        return self.sleep
    def get_fb_prob(self):
        return self.fb
     
def get_mean_and_std(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std
        
def lecture_activities(N, aLecture):
    '''
    N: integer, number of trials to run
    aLecture: Lecture object
 
    Runs a Monte Carlo simulation N times.
    Returns: a tuple, (float, float)
             Where the first float represents the mean number of lectures it takes 
             to have a lecture in which all 3 activities take place,
             And the second float represents the total width of the 95% confidence 
             interval around that mean.
    '''
    count = []
    
    while N > 0:
        # Calculate probability of all 3 events ocurring in a lecture
        prob = aLecture.get_fb_prob() * aLecture.get_listen_prob() * aLecture.get_sleep_prob()

        numLectures = 1
        while True:                 # For each sim, keep trying lectures till you get one with all 3 events
            x = random.random()
            if x <= prob:
                count.append(numLectures)
                break
            else: numLectures +=1  

        N -= 1

    (mean,SD) = get_mean_and_std(count)

    width = abs(SD)*2

    return (mean,width*2)


b = Lecture(1, 1, 0.5)
print(lecture_activities(10000, b))