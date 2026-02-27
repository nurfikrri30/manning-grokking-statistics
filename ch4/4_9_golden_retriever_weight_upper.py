import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mu, sigma = 64, 3
x = np.linspace(mu - sigma * 4, mu + sigma * 4, 1000)
y = norm.pdf(x, mu, sigma)

lower,upper = mu-sigma*4, 63
A = norm.cdf(upper, mu, sigma) - norm.cdf(lower, mu, sigma)
print(f"Area under curve: {A:.4f}")
# Plot the distribution
plt.plot(x, y)

# Shade the area between lower and upper
shade_x = x[(x >= lower) & (x <= upper)]
shade_y = norm.pdf(shade_x, mu, sigma)
plt.fill_between(shade_x, shade_y, alpha=0.5, color='#002d8b')

mid_x = (lower + upper) / 1.86
mid_y = norm.pdf(mid_x, mu, sigma) / 2
plt.annotate(f'A = {A:.4f}',
            xy=(mid_x, mid_y),
            xytext=(mid_x + 2, mid_y + 0.02),
            arrowprops=dict(facecolor='white', shrink=0.05),
            bbox=dict(boxstyle='round,pad=0.5', fc='white', ec='gray', alpha=1.0))

plt.title("Weight Distribution of Golden Retrievers")
plt.xlabel("Weight (lbs)")
plt.ylabel("Probability Density")
plt.grid(True, alpha=0.3)

import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()