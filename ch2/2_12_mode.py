import numpy as np
from scipy import stats

group_sizes = np.array([2, 4, 2, 3, 6, 2, 5, 4, 2, 3, 2])
mode, ct = stats.mode(group_sizes)

# MODE: 2, COUNT: 5
print(f"MODE: {mode}, COUNT: {ct}")