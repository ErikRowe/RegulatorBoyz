import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# parameters
alpha = 1/5
beta  = 1/10
gamma = 1/3
delta = 1/30
humanprey = 1
humanpred = 0.2

# define the time points where the solution is computed
n    = 100
tmax = 50
t    = np.linspace(0, tmax, n)


prey_verdier = [14.57]  # Initially includes only initial value of prey
pred_verdier =[1.31]    # Initially includes only initial value of predators

delta_t = 0.5

for k in range(1,100):
    prey_slope  =   alpha * prey_verdier[k-1] - beta  * prey_verdier[k-1] * pred_verdier[k-1] - humanprey
    pred_slope  = - gamma * pred_verdier[k-1] + delta * prey_verdier[k-1] * pred_verdier[k-1] - humanpred

    prey_k = prey_verdier[k-1] + prey_slope*delta_t
    prey_verdier.append(prey_k)

    pred_k = pred_verdier[k-1] + pred_slope*delta_t
    pred_verdier.append(pred_k)
    

# plot the time evolution
plt.subplot(1,1,1)
plt.plot(t, prey_verdier, label='prey', linewidth=1)
plt.plot(t, pred_verdier, label='predator', linewidth=1)
plt.grid()
plt.legend(loc = 'upper right')
plt.xlabel('time evolution')

plt.show()
