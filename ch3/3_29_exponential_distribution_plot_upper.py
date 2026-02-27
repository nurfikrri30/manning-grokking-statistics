from scipy.stats import expon
import numpy as np
import matplotlib.pyplot as plt

mu = 10 # mean views per minute

x = np.linspace(0, 1)
y = expon.pdf(x, scale=1/mu)

# Calculate and plot the area under the curve
lower_area_x, upper_area_x = 0, .4
x_area_range = (x >= lower_area_x) & (x <= upper_area_x)
area = expon.cdf(upper_area_x, scale=1/mu) - expon.cdf(lower_area_x, scale=1/mu)
print(f"AREA: {area}")


# Add axis labels
plt.plot(x, y)
plt.fill_between(x[x_area_range], y[x_area_range], 0, alpha=.5, color="#002d8b")

plt.xlabel('Time (Minutes) Between Views')
plt.ylabel('Probability Density')

# Show the plot
import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()
# Show the plot
