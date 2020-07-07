import matplotlib.pyplot as plt
import numpy as np
import math # For testing alternate hump (inverse parabolic) functions

# Initialise arrays that will hold data points
# p is a vector of r values for the parameter from 1 - 4
p = np.linspace(1.5,4.5,200000)
# eq_value is an array that will hold the 'equilibrium' values of the function after a large number of iterations
eq_value = [] # Y takes final "equilibrium" population value for each value (u) in P

for x in p:
    # Add one value to X instead of resetting it.
    m = np.random.random() # initial population, use random one each time to prevent sticking to one branch in diagram
    for n in range(300):
      m = x*math.sin(m) # experiment with various parabolic-like functions
    # Collection of data in Y must be done once per value of u
    eq_value.append(m)

# Remove the line between successive data points, this makes
# the plot illegible. Use a small marker instead.

fig = plt.figure()
fig.patch.set_facecolor('grey')
plot = fig.add_subplot(111)
plot.set_facecolor('black')


plt.plot(p, eq_value,'w',  ls='', marker=',', ms=5)
plt.xlabel("Growth Parameter")
plt.ylabel("Equilibrium Value")

fig.savefig('logistic.png', Transparent = True)

plt.show()