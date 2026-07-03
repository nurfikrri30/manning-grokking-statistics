import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

x = np.array([0.1, 0.5, 0.7, 1.2, 1.2, 1.5, 1.6, 1.9,
              2.5, 2.5, 2.7, 3.2, 3.3, 3.7, 3.8, 4.1,
              4.5, 4.5, 4.5, 5.0, 5.1, 5.6, 5.7, 6.2, 6.3])

y = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
              1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0,
              1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])

model = LogisticRegression(penalty=None)
model.fit(x, y)

b1 = model.coef_.flatten()[0]
b0 = model.intercept_.flatten()[0]
print(b0, b1)

# show in chart
x_trace = 4.78
y_trace = 1.0 / (1.0 + np.exp(-(b0 + b1 * x_trace)))
print(y_trace)

plt.scatter([x_trace], [y_trace], s=100, zorder=5)
plt.axvline(x=x_trace, linestyle='--', alpha=0.7)
plt.axhline(y=y_trace, linestyle='--', alpha=0.7)

plt.plot(x, y, 'o') # scatterplot
plt.xlabel("Hours without a nap")
plt.ylabel("Meltdown Observed?\n(0 = no, 1 = yes)")
plt.plot(x, y, 'o', color='black') # scatterplot
x = np.linspace(0,7,num=1000)
plt.plot(x, 1.0 / (1.0 + np.exp(-(b0 + b1*x))), color='blue') # curve

import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()

