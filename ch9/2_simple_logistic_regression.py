import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

x = (np.array([0.1, 0.5, 0.7, 1.2, 1.2, 1.5, 1.6, 1.9, 2.5, 2.5,
              2.7, 3.2, 3.3, 3.7, 3.8, 4.1, 4.5, 4.5, 4.5, 5.0,
              5.1, 5.6, 5.7, 6.2, 6.3])
     .reshape(-1, 1))  #A

y = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0,
              0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0,
              1.0, 1.0, 1.0, 1.0, 1.0])  #B

model = LogisticRegression(penalty=None)  #C
model.fit(x, y)  #C

b1 = model.coef_.flatten()[0]  #D
b0 = model.intercept_.flatten()[0]  #D

plt.plot(x, y, 'o')  #E
plt.xlabel("Hours without a nap")  #E
plt.ylabel("Meltdown Observed?\n(0 = no, 1 = yes)")  #E
x = np.linspace(0,7,num=1000)  #E
plt.plot(x, 1.0 / (1.0 + np.exp(-(b0 + b1*x))))  #E

import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()  #E


#A Declare and reshape X column
#B Declare Y column
#C Declare and fit the logistic regression
#D Extract coefficients
#E Show in the chart
