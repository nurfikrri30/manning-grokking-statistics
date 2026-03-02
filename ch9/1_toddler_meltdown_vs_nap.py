import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.1, 0.5, 0.7, 1.2, 1.2, 1.5, 1.6, 1.9,
              2.5, 2.5, 2.7, 3.2, 3.3, 3.7, 3.8, 4.1,
              4.5, 4.5, 4.5, 5.0, 5.1, 5.6, 5.7, 6.2, 6.3])

y = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
              1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0,
              1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])

print(x.shape)
# show in chart
plt.plot(x, y, 'o') # scatterplot
plt.xlabel("Hours without a nap")
plt.ylabel("Meltdown Observed?\n(0 = no, 1 = yes)")

import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()
