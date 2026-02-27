import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

x = np.array([27, 22, 28, 27, 26, 28, 31, 25, 25, 33, 24, 28, 28, 30,
             26, 25, 29, 28, 30, 30, 22, 28, 36, 27, 26, 31, 30, 25,
             27, 32, 25, 23, 27, 24, 28, 24, 27, 28, 30, 26, 33, 29,
             31, 29, 27, 31, 20, 23, 25, 29, 30, 24, 29, 28, 25, 25,
             30, 30, 27, 36, 26, 31, 24, 29, 34, 27, 23, 29, 27, 19,
             28, 30, 26, 29, 27, 30, 29, 28])  #A

mu, sigma = x.mean(), x.std()  #B

x_line = np.linspace(mu - sigma * 4, mu + sigma * 4, 1000)  #C
y = norm.pdf(x_line, mu, sigma)  #D
plt.plot(x_line, y)  #E

plt.hist(x, bins=np.arange(min(x), max(x) + 2) - 0.5, alpha=.4, color='#002d8b', density=True)  #F

plt.title("Ideal Coffee Grounds Amount for 16 oz Cup")  #G
plt.xlabel("Weight (grams)")  #H
plt.ylabel("Probability Density")  #I
plt.grid(True, alpha=0.3)  #J

import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()  #K

#A Define array of coffee grounds weight measurements in grams
#B Calculate mean and standard deviation of the data
#C Generate 1000 evenly spaced points from mu - 4*sigma to mu + 4*sigma
#D Compute normal distribution PDF for the generated x values
#E Plot the normal distribution curve
#F Create histogram of data with density normalization, 0.4 transparency, and blue color
#G Set plot title
#H Label x-axis
#I Label y-axis
#J Add grid with 0.3 opacity
#K Display the plot
