import pylab
import random

xVals, yVals = [], []

for i in range(10):
    xVals.append(random.randint(0,10))
    yVals.append(random.randint(0,10))

degs = [1,2]


fits = pylab.polyfit(xVals,yVals,1)

estYVals = []
estYVals.append(fits[0]*pylab.array(xVals) + fits[1])

#print(estYVals[0])
#print(yVals)

print(fits)
