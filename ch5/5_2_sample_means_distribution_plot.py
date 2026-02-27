import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from math import sqrt

mu, sigma = 98.2, .73  #A
n = 31  #B

mu_sample_means = mu  #C
mu_sample_sigma = sigma / sqrt(n)  #D

x = np.linspace(mu_sample_means - mu_sample_sigma * 4, mu_sample_means + mu_sample_sigma * 4, 1000)  #E
y = norm.pdf(x, mu_sample_means, mu_sample_sigma)  #F

lower, upper = mu_sample_means - mu_sample_sigma * 4, 98  #G
A = norm.cdf(upper, mu_sample_means, mu_sample_sigma) - norm.cdf(lower, mu_sample_means, mu_sample_sigma)  #H
print(f"Area under curve: {A:.4f}")  #I

plt.plot(x, y)  #J

shade_x = x[(x >= lower) & (x <= upper)]  #K
shade_y = norm.pdf(shade_x, mu_sample_means, mu_sample_sigma)  #L
plt.fill_between(shade_x, shade_y, alpha=0.5, color='#002d8b')  #M

plt.title("Sample Means Distribution")  #N
plt.xlabel("Body Temperature °F")  #O
plt.ylabel("Probability Density")  #P
plt.grid(True, alpha=0.3)  #Q

import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()  #R

#A Set population mean to 98.2 and standard deviation to 0.73
#B Set sample size to 31
#C Set mean of sample means to population mean
#D Calculate standard deviation of sample means
#E Generate 1000 evenly spaced points from mean - 4*std to mean + 4*std
#F Compute normal PDF values for x
#G Set lower bound to mean - 4*std and upper to 98
#H Calculate area under curve from lower to upper using CDF
#I Print area under curve formatted to four decimal places
#J Plot the distribution curve
#K Select x values for shading between lower and upper
#L Compute PDF values for shaded x
#M Shade the area with 0.5 transparency and blue color
#N Set plot title
#O Label x-axis
#P Label y-axis
#Q Add grid with 0.3 opacity
#R Display the plot