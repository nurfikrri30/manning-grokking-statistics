import numpy as np

temps = [77,75,68,71,60,65,81,71,56,73,
      79,80,85,84,72,69,82,81,71,63,
      75,83,80,80,88,76,79,73,80,81,82]

# calculate mean
mean = sum(temps) / len(temps)

# sum all the squared differences
squared_diffs = 0
for t in temps:
  squared_diffs += (t - mean) ** 2

# take the average of the squared differences
variance = squared_diffs / (len(temps) - 1)

# Variance:  57.65806451612904
print("Variance: ", variance)

# From NumPy:  57.65806451612903
print("From NumPy: ", np.var(temps, ddof=1))
