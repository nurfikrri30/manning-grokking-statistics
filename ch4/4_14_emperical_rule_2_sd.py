import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mu, sigma = 0,1
x = np.linspace(mu - sigma * 4, mu + sigma * 4, 1000)
y = norm.pdf(x, mu, sigma)

lower,upper = mu-sigma*2, mu+sigma*2
A = norm.cdf(upper, mu, sigma) - norm.cdf(lower, mu, sigma)
print(f"Area under curve: {A:.4f}")

# Plot the distribution
plt.plot(x, y)

# Shade the area between lower and upper
shade_x = x[(x >= lower) & (x <= upper)]
shade_y = norm.pdf(shade_x, mu, sigma)
plt.fill_between(shade_x, shade_y, alpha=0.5, color='#002d8b')

mid_x = (lower + upper) / 2
mid_y = norm.pdf(mid_x, mu, sigma) / 2
plt.text(mid_x, mid_y, f'A = {A:.4f}',
         horizontalalignment='center',
         verticalalignment='center',
         bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))


plt.grid(True, alpha=0.3)

import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()