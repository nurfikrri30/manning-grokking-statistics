import numpy as np
from numpy import sum

x = np.array([51.5, 55.1, 63.0, 71.2, 73.0, 77.1,
              88.1, 91.2, 93.0, 101.6])

y = np.array([100.98, 137.44, 237.8, 254.96, 263.45,
              353.89, 450.32, 521.34, 503.13, 573.91])

n = len(x)
m = (n*sum(x*y) - sum(x)*sum(y)) / (n*sum(x**2) - sum(x)**2)
b = (sum(y) / n) - m * sum(x) / n

print(m, b)
# 9.740870543251257 -405.259779147856