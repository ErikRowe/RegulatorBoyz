import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def task24Model(x,t):
    f = 2
    m = 1
    ut = None
    if t < 3:
        ut = 0
    else:
        ut = 1
    
    dxdt = -f/m * x + 1/m * ut
    return dxdt

x0 = 10
t = np.linspace(0,10)
x = odeint(task24Model, x0, t)

plt.plot(t, x)
plt.xlabel('time')
plt.ylabel('x(t)')
plt.show()