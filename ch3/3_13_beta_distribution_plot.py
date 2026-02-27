import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import beta

a, b = 7, 3 # successes, failures

x = np.linspace(0, 1)
y = beta.pdf(x, a, b)

plt.plot(x, y)
plt.xlabel('Success Rate')
plt.ylabel('Probability of that Success Rate')

import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()
