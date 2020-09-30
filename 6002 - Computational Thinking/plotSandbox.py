
import numpy as np
import pylab as plt


Xvals = []
linear = []
quadratic = []

for i in range(30):
    Xvals.append(i)
    linear.append(i)
    quadratic.append(i*i)

plt.figure("quadratic")
plt.xlabel("sample points")
plt.ylabel("square values")
plt.semilogy()                          # sets y axis to semi log scale
plt.plot(Xvals, quadratic, 'k^')        # uses optional [fmt] arg to make color black, and marker = triangle
#plt.show()



# Helper function to make plots

def makePlot(x, y, title, xLabel, yLabel, style, logx = False, logy = False):
    plt.figure()
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.plot(x, y, style)

    if logx: plt.semilogx()
    if logy: plt.semilogy()

    plt.show()

title = "Exponential function"
makePlot(Xvals, quadratic, title, "Sample points", "Values", 'bo', logy = True)

