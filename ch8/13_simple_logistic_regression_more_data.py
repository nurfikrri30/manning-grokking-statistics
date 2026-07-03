import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Declare and reshape X column
x = np.array([0.1, 0.13, 0.22, 0.31, 0.38, 0.38,
              0.46, 0.5, 0.50, 0.56, 0.64, 0.7,
              0.70, 0.85, 0.96, 0.97, 1.06, 1.06,
              1.15, 1.2, 1.2, 1.22, 1.23, 1.24,
              1.31, 1.33, 1.33, 1.41, 1.5, 1.6,
              1.70, 1.78, 1.84, 1.9, 1.90, 1.91,
              1.98, 1.98, 2.03, 2.11, 2.31, 2.37,
              2.42, 2.5, 2.5, 2.50, 2.7, 2.77,
              2.82, 2.92, 3.17, 3.2, 3.28, 3.3,
              3.32, 3.35, 3.46, 3.48, 3.7, 3.77,
              3.8, 3.80, 3.81, 3.82, 3.86, 3.89,
              4.1, 4.20, 4.34, 4.48, 4.49, 4.5,
              4.5, 4.5, 4.63, 4.88, 4.90, 4.96,
              5., 5.07, 5.1, 5.11, 5.15, 5.23,
              5.26, 5.47, 5.6, 5.64, 5.7, 5.73,
              5.81, 5.92, 5.98, 5.99, 6.08, 6.11,
              6.11, 6.2, 6.21, 6.3]) \
    .reshape(-1, 1)  #A

y = np.array([0., 0., 0., 0., 0., 0., 0.,
              0., 0., 0., 0., 0., 0., 0.,
              0., 0., 0., 0.,0., 0., 0.,
              0., 0., 0., 0., 0., 0., 0.,
              0., 0.,0., 0., 1., 0., 0.,
              0.,0., 0., 0., 1.,0., 0.,
              0., 0., 1., 0., 0., 0., 0.,
              0.,1., 0., 1., 1.,1., 0., 0.,
              1., 1., 1.,0., 1., 0., 1., 1.,
              1., 1., 1., 1., 1.,1., 1.,1.,
              1., 1., 1., 1., 1., 0., 1.,1.,
              1., 1., 1., 0., 1., 1., 1., 1.,
              1.,1., 1., 1., 1., 1., 1., 1.,
              1., 1., 1.])  #B


# Declare and fit the logistic regression
model = LogisticRegression(penalty=None)
model.fit(x, y)

b1 = model.coef_.flatten()[0]
b0 = model.intercept_.flatten()[0]

# show in chart
plt.plot(x, y, 'o') # scatterplot
plt.xlabel("Hours without a nap")
plt.ylabel("Meltdown Observed?\n(0 = no, 1 = yes)")
plt.plot(x, y, 'o') # scatterplot
x = np.linspace(0,7,num=1000)
plt.plot(x, 1.0 / (1.0 + np.exp(-(b0 + b1*x)))
         ,color="blue") # curve

import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()

