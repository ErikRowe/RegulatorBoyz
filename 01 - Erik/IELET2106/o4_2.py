import numpy as np
from sympy import symbols, Eq, solve
from scipy.stats import norm
import math
import matplotlib.pyplot as plt

# Datapoints
cm_data = [0.00,1.50,3.00,4.50,6.00,7.50,9.00,10.5,12.0,13.5,15.0]
V_increase_data = [0.00,0.35,1.42,2.40,3.43,4.35,5.61,6.50,7.77,8.85,10.2]
V_decrease_data = [0.14,1.25,2.32,3.55,4.43,5.70,6.78,7.80,8.87,9.65,10.2]
V_avg = []
xy = []
n = len(cm_data)
#Regresjonsanalyse
'''
Fra forelesning 07.09.2021
y(x) = bx + a
a*n + b*Sum (x) = sum(y)
a*sum(x) + b*sum(x**2) = sum(x*y)
'''
#Finner gjennomsnittet av måledataene og legger det i en egen liste
for i in range(len(V_increase_data)):
    sum = V_increase_data[i] + V_decrease_data[i]
    avg = sum/2
    V_avg.append(avg)

#Finner variabelen som tregs for å finne a og b til regresjon
sigma_x = math.fsum(cm_data)
sigma_x2 = math.fsum(i*i for i in cm_data)
sigma_y_avg = math.fsum(V_avg)
for i in range(len(V_increase_data)):
    xy.append(cm_data[i]*V_avg[i])
sigma_xy_avg = math.fsum(xy)
#Løser lignigssettet for a og b
A, B = symbols('A, B')
eq1 = Eq(A*n + B*sigma_x - sigma_y_avg)
eq2 = Eq(A*sigma_x + B*sigma_x2 - sigma_xy_avg)
sol_dict = solve((eq1,eq2), (A, B))
a = sol_dict[A]
b = sol_dict[B]
# Lager funksjon av linjen og lagrer datapunkt i en liste for plotting
def f1(t):
    return b*t +a
uavhengig = []
for i in cm_data:
    uavhengig.append(f1(i))

#Finner hysteresen som differansen mellom y_økende og y_avtakende
hysterese =[]
for i in range(len(V_increase_data)):
    diff = V_decrease_data[i]-V_increase_data[i]
    hysterese.append(diff)
størst_avvik = max(hysterese)
print(størst_avvik)

#Plotting
plt.plot(cm_data,V_increase_data,linestyle='-', marker='o', color='g', label='Stigende verdi')
plt.plot(cm_data,V_decrease_data,linestyle='-', marker='o', color='r', label='Synkende verdi')
plt.plot(cm_data, uavhengig,linestyle='-', color='k', label='Uavhengig ref.karakteristikk')
plt.plot(cm_data, hysterese,linestyle='-', marker='o', color='b', label='Hysterese')
plt.title('Kalibreringskurve for en kalibreringssyklus')
plt.xlabel('Nivå [cm]')
plt.ylabel('Volt [V]')
plt.grid()
plt.legend()
plt.show()