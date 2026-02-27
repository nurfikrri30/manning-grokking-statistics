from scipy.stats import expon
import numpy as np
from matplotlib import pyplot as plt

mu = 10 # mean views per minute

x = np.linspace(0, 1)
y = expon.pdf(x, scale=1/mu)

plt.plot(x, y)

# Add axis labels
plt.xlabel('Time (Minutes) Between Views')
plt.ylabel('Probability Density')

# Show the plot
import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()