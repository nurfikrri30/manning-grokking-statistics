import numpy as np

temps = [77,75,68,71,60,65,81,71,56,73,
       79,80,85,84,72,69,82,81,71,63,
       75,83,80,80,88,76,79,73,80,81,82]

mean = np.mean(temps)

print("MIN: ", np.min(temps), "MAX: ", np.max(temps))
# MIN:  56 MAX:  88

print("MEAN: ", mean)
# MEAN: 75.48387096774194

print("MEDIAN: ", np.median(temps))
# MEDIAN: 77.0
