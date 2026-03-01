import os

import pandas as pd
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

df = pd.read_csv('birdstrike.csv')

# remove records where no recorded height exists
df = df[df['HEIGHT'].isna() == False]

# bin up bird strikes by height, in buckets of 100 feet
max_height = int(df['HEIGHT'].max()
                 // 100 + 1) * 100

bins = list(range(0, max_height + 100, 100))
df['HEIGHT_BIN'] = pd.cut(df['HEIGHT'],
                          bins=bins, right=False)

incidents_by_bin = (df['HEIGHT_BIN']
                    .value_counts().sort_index())

# extract out x and y
x = np.arange(start=0, stop=max_height, step=100)
y = incidents_by_bin.to_numpy()

slope, intercept, r_value, p_value, std_err \
    = linregress(x, y)  #B

x_line = np.linspace(min(x), max(x), 100)  #C
y_line = slope * x_line + intercept  #C

plt.scatter(x, y, label='Data points')  #D

plt.plot(x_line,  #E
         y_line,  #E
         color='red',  #E
         label=f'Fit: y = {slope:.2f}x '
               f'{'-' if intercept < 0 else '+'}'
               f' {abs(intercept):.2f}')  #E

plt.title("Bird Strikes by Height")
plt.xlabel("Bird Strike Height (feet)")
plt.ylabel("Bird Strike Count")  #F
plt.legend()  #F

plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()  #G

print(f"Slope: {slope:.8f}")  #H
print(f"Intercept: {intercept:.8f}")  #H
print(f"Pearson Correlation: {r_value:.4f}")  #H
print(f"P-value (for slope): {p_value:.10f}")  #H
print(f"Standard error of slope: {std_err:.4f}")  #H