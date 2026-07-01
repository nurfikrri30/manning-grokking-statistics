import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mu, sigma = 50000, 7500
x = np.linspace(mu - sigma * 8, mu + sigma * 8, 1000)
y = norm.pdf(x, mu, sigma)

# Plot the distribution
plt.plot(x, y)

# Add point at 6 sigma
six_sigma_point = mu - (6 * sigma)
point_y = norm.pdf(six_sigma_point, mu, sigma)

# Plot the point
plt.plot(six_sigma_point, point_y, 'ro')  # Red dot

# Add label with arrow
plt.annotate('"This was a six-sigma event!"',
            xy=(six_sigma_point, point_y),  # Point to label
            xytext=(six_sigma_point - sigma*2, point_y + 0.00005),  # Text position
            arrowprops=dict(facecolor='black', shrink=0.05),
            bbox=dict(facecolor='white', edgecolor='red', alpha=0.8))

plt.grid(True, alpha=0.3)

import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()