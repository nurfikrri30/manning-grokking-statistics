import numpy as np
import matplotlib.pyplot as plt

def logistic(x, b0, b1):
    return 1.0 / (1.0 + np.exp(-(b0 + b1*x)))

b0 = -7.0587
b1 = 2.2047
x = np.linspace(0,7,num=1000)
y = logistic(x, b0, b1)

plt.plot(x, y, color='blue')

import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()