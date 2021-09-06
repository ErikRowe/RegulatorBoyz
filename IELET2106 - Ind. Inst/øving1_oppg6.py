import numpy as np
from scipy.stats import norm
import math
import matplotlib.pyplot as plt

data = [208.6, 208.3, 208.7, 208.5, 208.8, 207.6, 208.9, 209.1, 208.2, 208.4, 208.1, 209.2, 209.6, 208.6, 208.5, 207.4, 210.2, 209.2, 208.7, 208.4, 207.7, 208.9, 208.7, 208.0, 209.0, 208.1, 209.3, 208.2, 208.6, 209.4, 207.6, 208.1, 208.8, 209.2, 209.7]
numb_of_bins = round(math.sqrt(len(data)))
 # According to MatLab doc regarding histfit: histfit(data) plots a histogram of values in data using the number of bins equal 
 # to the square root of the number of elements in data and fits a normal density function.

mu, std = norm.fit(data)

plt.hist(data,bins=numb_of_bins,density=True,alpha=0.6,color='b')
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)

plt.plot(x, p, 'k', linewidth=2,color='r')
title = "Mid: {:.2f} and {:.2f}".format(mu, std)

plt.title(title)
  
plt.show()