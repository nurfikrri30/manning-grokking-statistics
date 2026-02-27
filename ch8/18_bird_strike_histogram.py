import os

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('birdstrike.csv')

x = df['HEIGHT'].values

# Add histogram
plt.hist(x, bins=31, alpha=.4, color='#002d8b')

# Add labels and show
plt.title("Bird strike Count vs Height (feet)")
plt.xlabel("Height (feet)")
plt.ylabel("# Bird Strikes")
plt.grid(True, alpha=0.3)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)
plt.show()

