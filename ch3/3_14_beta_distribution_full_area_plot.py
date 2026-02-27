import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import beta

a, b = 7, 3 # successes, failures

x = np.linspace(0, 1)
y = beta.pdf(x, a, b)

lower_area_x, upper_area_x = 0, 1
x_area_range = (x >= lower_area_x) & (x <= upper_area_x)

area = beta.cdf(upper_area_x, a, b) - beta.cdf(lower_area_x, a, b)
print(f"AREA: {area}")

plt.plot(x, beta.pdf(x, a, b))
plt.fill_between(x[x_area_range], y[x_area_range], 0, alpha=.5,  color='grey')

# Add label in the center
plt.xlabel('Success Rate')
plt.ylabel('Probability Density')

# Calculate center position (x=0.5 for center of [0,1], y at half of max height)
center_x = 0.7
center_y = max(y) / 3
plt.text(center_x, center_y, 'A = 1.0',
         horizontalalignment='center',
         verticalalignment='center',
         size=20)

import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()
