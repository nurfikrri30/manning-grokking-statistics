import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mu, sigma = 64, 2.5

x = np.linspace(mu-sigma*4, mu+sigma*4, 1000)
y = norm.pdf(x, mu, sigma)

# Plot the distribution
plt.plot(x, y)
plt.title("Height Distribution of US Women")
plt.xlabel("Height (inches)")
plt.ylabel("Probability Density")
plt.grid(True, alpha=0.3)

import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()
