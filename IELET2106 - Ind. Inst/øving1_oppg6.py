import numpy as np
from scipy.stats import norm
import math
import matplotlib.pyplot as plt

# Script for task 6. excercize 1
data = [208.6, 208.3, 208.7, 208.5, 208.8, 207.6, 208.9, 209.1, 208.2, 208.4, 208.1, 209.2, 209.6, 208.6, 208.5, 207.4, 210.2, 209.2, 208.7, 208.4, 207.7, 208.9, 208.7, 208.0, 209.0, 208.1, 209.3, 208.2, 208.6, 209.4, 207.6, 208.1, 208.8, 209.2, 209.7]
numb_of_bins = round(math.sqrt(35))


mu, std = norm.fit(data)

plt.hist(data, bins=numb_of_bins, density=True, alpha=0.6, color='b', label='this 1')
xmin, xmax = plt.xlim()

x = np.linspace(xmin-0.5, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'r', linewidth=1)

legend1 = "Median: {:.2f}, Standard deviation: {:.2f}".format(mu, std)
plt.title("Histogram with normal distribution")
plt.show()