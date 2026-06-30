import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("https://raw.githubusercontent.com/thomasnield/"
  "training-data-repository/refs/heads/main/TORNADO_TRX.csv")

# Group by TOR_F_SCALE and calculate mean, median, standard deviation for TOR_WIDTH
grouped_stats = df.groupby('TOR_F_SCALE')['TOR_WIDTH'].agg(
   p25=lambda x: np.percentile(x, 25),  # 25th percentile (Q1)
   median='median',                     # median
   p75=lambda x: np.percentile(x, 75),  # 75th percentile (Q3)
   iqr=lambda x: np.percentile(x, 75) - np.percentile(x,25) # IQR
).reset_index()

# Round the results for readability
grouped_stats = grouped_stats.round(2)

# Print the results
print("TOR_WIDTH Statistics by TOR_F_SCALE:")
print(grouped_stats)
# TOR_WIDTH Statistics by TOR_F_SCALE:
#   TOR_F_SCALE     p25  median     p75    iqr
# 0         EF0    30.0    50.0   100.0   70.0
# 1         EF1    80.0   150.0   300.0  220.0
# 2         EF2   200.0   400.0   792.5  592.5
# 3         EF3   400.0   700.0  1387.5  987.5
# 4         EF4  1000.0  1320.0  1575.0  575.0
# 5         EFU    20.0    30.0    50.0   30.0
