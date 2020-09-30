import random
import pylab as plt

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    currentPop = CURRENTRABBITPOP

    for i in range(currentPop):   # for each rabbit in existing population
      x = random.random()
      rabbitProb = 1 - (CURRENTRABBITPOP/MAXRABBITPOP)

      if x <= rabbitProb:         # reproduce if within probability
        CURRENTRABBITPOP += 1

            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    currFox = CURRENTFOXPOP

    for i in range(currFox):

      if CURRENTRABBITPOP <= 10:    # fox wont hunt if 10 or less, so it might die
        x = random.random()
        if x <= 0.9 and CURRENTFOXPOP > 10: 
          CURRENTFOXPOP -= 1
          continue
      
      # If rabbit pop is sufficient, then the fox can hunt and might reproduce

      eatProb = (CURRENTRABBITPOP/MAXRABBITPOP)
      x = random.random()

      if x <= eatProb and CURRENTRABBITPOP > 10:
        CURRENTRABBITPOP -= 1
        if random.random() <= (1/3):
          CURRENTFOXPOP += 1
        
      
      else:
        # Fox failed to hunt purEly out of chance, so it might die also
        if random.random() <= 0.9 and CURRENTFOXPOP > 10: CURRENTFOXPOP -=1
      

def makePlot(x, y1, y2, title, xLabel, yLabel, logx = False, logy = False):
  plt.figure()
  plt.title(title)
  plt.xlabel(xLabel)
  plt.ylabel(yLabel)
  plt.plot(x, y1, 'b',)
  plt.plot(x,y2, 'k')
  plt.legend(y1, y2, loc = 'best')

  if logx: plt.semilogx()
  if logy: plt.semilogy()

  plt.show()      
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    rabList, foxList = [], []

    for i in range(numSteps):
      rabbitGrowth()
      foxGrowth()

      rabList.append(CURRENTRABBITPOP)
      foxList.append(CURRENTFOXPOP)
    
    return (rabList, foxList)

xVals = []
for i in range(200):
  xVals.append(i)
(a,b) = runSimulation(200)
makePlot(xVals, a, b, "Rabbit Fox Growth", "Timesteps", "Num Creatures")

coeffs1 = plt.polyfit(xVals,a,2)
coeffs2 = plt.polyfit(xVals,b,2)

y1,y2 = [], []

y1 = plt.polyval(coeffs1, xVals)
y2 = plt.polyval(coeffs2, xVals)

makePlot(xVals, y1, y2, "Rabbit Fox Growth from Model", "Timesteps", "Num Creatures")
