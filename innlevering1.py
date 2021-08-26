import numpy as np
import math
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from TK4225.functions import cisBoyz

def main():
    mainClass = cisBoyz()

    # define the initial condition
    y0 = [ 20, 5 ]

    # define the time points where the solution is computed
    n    = 100
    tmax = 20
    t    = np.linspace(0, tmax, n)

    # solve the ODE
    y = odeint(mainClass.LotkaVolterra, y0, t)

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
    

main()