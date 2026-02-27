import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import beta

a, b = 7, 3  #A

x = np.linspace(0, 1)  #B
y = beta.pdf(x, a, b)  #C

lower_area_x, upper_area_x = .4, .7  #D
x_area_range = (x >= lower_area_x) & (x <= upper_area_x)  #E

area = beta.cdf(upper_area_x, a, b) - beta.cdf(lower_area_x, a, b)  #F
print(f"AREA: {area}")  #G

plt.plot(x, beta.pdf(x, a, b))  #H
plt.fill_between(x[x_area_range], y[x_area_range], 0, alpha=.5, color='grey')  #I
plt.text(.55, .3, f"Area = {area:.4f}", horizontalalignment='center', verticalalignment='bottom', fontsize=10)  #J

import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()  #K

#A Set parameters with 7 successes and 3 failures
#B Generate 100 evenly spaced points between 0 and 1
#C Compute beta distribution PDF for given x values
#D Define bounds for area calculation between 0.4 and 0.7
#E Create boolean mask for x values within the specified range
#F Calculate area under the curve between lower and upper bounds using CDF
#G Print the calculated area
#H Plot the beta distribution PDF
#I Shade the area under the curve between 0.4 and 0.7 with grey fill and 0.5 transparency
#J Add text label showing the area to four decimal places at position (0.55, 0.3)
#K Display the plot
