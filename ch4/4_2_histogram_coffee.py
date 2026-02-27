import numpy as np
from numpy.random import normal
from scipy.stats import norm
import matplotlib.pyplot as plt

# x = normal(loc=28, scale=3, size=78).astype(int)
x = np.array([27, 22, 28, 27, 26, 28, 31, 25, 25, 33, 24, 28, 28, 30,
              26, 25, 29, 28, 30, 30, 22, 28, 36, 27, 26, 31, 30, 25,
              27, 32, 25, 23, 27, 24, 28, 24, 27, 28, 30, 26, 33, 29,
              31, 29, 27, 31, 20, 23, 25, 29, 30, 24, 29, 28, 25, 25,
              30, 30, 27, 36, 26, 31, 24, 29, 34, 27, 23, 29, 27, 19,
              28, 30, 26, 29, 27, 30, 29, 28])

print(x.shape)

plt.hist(x, bins=np.arange(min(x), max(x) + 2) - 0.5, alpha=1.0, color='#002d8b')

plt.title('"Perfect" Amount of Coffee for 16 oz Cup')
plt.xlabel('Weight (grams)')
plt.ylabel('Barista Votes')
plt.xticks(range(min(x), max(x) + 1))

import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()
