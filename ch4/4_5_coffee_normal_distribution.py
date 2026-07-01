from math import sqrt, exp, pi
import numpy as np
import matplotlib.pyplot as plt

def normal_pdf(x, mu, sigma):  #A
    return 1/(sigma * sqrt(2*pi)) * exp(-0.5 * ((x - mu)/sigma)**2)  #B

mu, sigma = 27.6, 3.18  #C

x_line = np.linspace(mu - sigma * 4, mu + sigma * 4, 1000)  #D
y = [normal_pdf(x, mu, sigma) for x in x_line]  #E
plt.plot(x_line, y)  #F

plt.title("Ideal Coffee Grounds Amount for 16 oz Cup")  #G
plt.xlabel("Weight (grams)")  #H
plt.ylabel("Probability Density")  #I
plt.grid(True, alpha=0.3)  #J

import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()  #K

#A Define function to calculate normal distribution PDF
#B Compute normal PDF using the formula
#C Set mean to 27.6 and standard deviation to 3.18
#D Generate 1000 evenly spaced points from mu - 4*sigma to mu + 4*sigma
#E Calculate PDF values for each x using normal_pdf function
#F Plot the normal distribution curve
#G Set plot title
#H Label x-axis
#I Label y-axis
#J Add grid with 0.3 opacity
#K Display the plot
