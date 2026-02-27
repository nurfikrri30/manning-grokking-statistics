import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mu, sigma = 64, 3
x = np.linspace(mu - sigma * 4, mu + sigma * 4, 1000)
y = norm.pdf(x, mu, sigma)

# Plot the distribution
plt.plot(x, y)

# Add vertical and horizontal lines for likelihood at 61.63 lbs
target_x = 61.63
target_y = norm.pdf(target_x, mu, sigma)
plt.axvline(x=target_x, color='k', linestyle='--', alpha=0.5)
plt.axhline(y=target_y, color='k', linestyle='--', alpha=0.5)

# Add label for the target y-value
plt.text(target_x - 4.5, target_y, f'y = {target_y:.4f}', verticalalignment='bottom')

# Add rotated label for the target x-value
plt.text(target_x, .065, f'x = {target_x}', rotation=270, verticalalignment='bottom')

plt.title("Weight Distribution of Golden Retrievers")
plt.xlabel("Weight (lbs)")
plt.ylabel("Probability Density")
plt.grid(True, alpha=0.3)

import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()