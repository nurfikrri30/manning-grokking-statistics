import numpy as np
from scipy.stats import poisson

mean = 5  #A

x = np.arange(0, 21, 1)  #B

y = poisson.pmf(x, mu=mean)  #C

for _x, _y in zip(x, y):  #D
    print(f"The probability of {_x} views within 1 minute is {_y:.4f}")  #E


# Create a bar chart of the PMF values
import matplotlib.pyplot as plt

plt.bar(x, y, align='center', color='#002d8b')

# Set the title and labels
plt.title('Poisson Distribution (μ = 5)')
plt.xlabel('Number of Views (within 1 minute)')
plt.ylabel('Probability')

import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()  #K

# Show the plot
plt.show()

