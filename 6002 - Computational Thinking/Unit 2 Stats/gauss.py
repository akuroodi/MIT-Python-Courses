# Generate a discrete approximation for a Gaussian distribution with PyPlot

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sp
import random


dist = []

for i in range(100000):
    dist.append(random.gauss(50, 5))    #appending y values generating from random.gauss(mu, sigma)

mean = np.mean(dist)
sigma = np.std(dist)

y = sp.norm.pdf(mean,sigma)

plt.hist(dist, 50)      # quick histogram wtih 50 bins
plt.title("Discrete Approximation to Gaussian Distribution")


#plt.hist(y,50)



plt.show()