import numpy as np
from scipy.stats import linregress

x = np.array([51.5, 55.1, 63.0, 71.2, 73.0, 77.1, 88.1, 91.2, 93.0, 101.6])
y = np.array([100.98, 137.44, 237.8, 254.96, 263.45, 353.89, 450.32, 521.34, 503.13, 573.91])

m, b, r_value, p_value, std_err = linregress(x, y)

# Root mean squared error (RMSE): 23.4044
rmse = np.sqrt(np.sum((y - (m*x+b))**2) / len(x))
print(f"Root mean squared error (RMSE): {rmse:.4f}")
