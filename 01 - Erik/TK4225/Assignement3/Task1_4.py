# load the necessary packages
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# define the function that returns dz/dt
def myModel(y, t):
    #
    # parameters
    alpha = 1/5
    beta  = 1/10
    gamma = 1/3
    delta = 1/30
    humanprey = 1
    humanpred = 0.2
    #
    # get the individual variables - for readability
    yPrey =  y[0]
    yPred = y[1]
    #
    # individual derivatives
    dyPreydt  =   alpha * yPrey - beta  * yPrey * yPred - humanprey
    dyPreddt  = - gamma * yPred + delta * yPrey * yPred - humanpred
    #
    return [ dyPreydt, dyPreddt ]

# define the initial condition
y0 = [ 20, 5 ]

# define the time points where the solution is computed
n    = 100
tmax = 50
t    = np.linspace(0, tmax, n)

# solve the ODE
y = odeint(myModel, y0, t)

# get the individual variables
yPrey = y[:,0]
yPred = y[:,1]

# plot the time evolution
plt.subplot(1,2,1)
plt.plot(t, yPrey, label='prey', linewidth=1)
plt.plot(t, yPred, label='predator', linewidth=1)
plt.grid()
plt.legend(loc = 'upper right')
plt.xlabel('time evolution')

# plot the phase portrait
plt.subplot(1,2,2)
plt.plot(yPrey, yPred, linewidth=1)
plt.grid()
plt.xlabel('prey')
plt.ylabel('predator')
plt.title('phase portrait')

plt.show()

