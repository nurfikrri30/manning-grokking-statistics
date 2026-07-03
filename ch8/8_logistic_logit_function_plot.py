import numpy as np
import matplotlib.pyplot as plt

b0 = -7.0587
b1 = 2.2047

x = np.linspace(0, 7, 500)

logistic = 1 / (1 + np.exp(-(b0 + b1*x)))
logit = b0 + b1*x

plt.plot(x, logistic, label='logistic')
plt.plot(x, logit, label='logit')
plt.ylim(-1, 2)
plt.axhline(y=0, color='black', linewidth=0.8)
plt.axhline(y=0.5, color='gray', linewidth=0.8, linestyle='--')
plt.axvline(x=-b0 / b1, color='gray', linewidth=0.8, linestyle='--')

plt.legend()

import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)


plt.show()