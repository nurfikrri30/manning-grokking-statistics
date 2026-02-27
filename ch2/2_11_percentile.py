import numpy as np

bar_tabs = [7, 18, 19, 20, 21, 22, 25, 120, 1500]

q25 = np.percentile(bar_tabs, 25)
q50 = np.percentile(bar_tabs, 50)
q75 = np.percentile(bar_tabs, 75)

# 19.0 21.0 25.0
print(q25, q50, q75)