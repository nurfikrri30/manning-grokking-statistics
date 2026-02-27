import numpy as np
from scipy.stats import linregress

x = np.array([51.5, 55.1, 63.0, 71.2, 73.0, 77.1, 88.1, 91.2, 93.0, 101.6])
y = np.array([100.98, 137.44, 237.8, 254.96, 263.45, 353.89, 450.32, 521.34, 503.13, 573.91])

m, b, r_value, p_value, std_err = linregress(x, y)

# Print the regression results
print(f"Slope: {m:.2f} (sales increase per degree Fahrenheit)")
print(f"Intercept: {b:.2f}")
print(f"Pearson Correlation: {r_value:.4f}")
print(f"P-value (for slope): {p_value:.10f}")
print(f"Standard error of slope: {std_err:.4f}")

# R-square (using formula): 0.9779
r_square = 1 - (np.sum((y - (m*x+b))**2) / np.sum((y - np.mean(y))**2))
print(f"R-square (using formula): {r_square:.4f}")

# Root mean squared error (RMSE): 23.4044
rmse = np.sqrt(np.sum((y - (m*x+b))**2) / len(x))
print(f"Root mean squared error (RMSE): {rmse:.4f}")

