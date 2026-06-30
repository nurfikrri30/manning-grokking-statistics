import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/thomasnield/"
              "training-data-repository/refs/heads/main/TORNADO_TRX.csv")

tor_width = df['TOR_WIDTH']

print("MEAN: ", np.mean(tor_width))          # MEAN:  215.18971962616823
print("MEDIAN: ", np.median(tor_width))      # MEDIAN:  100.0
print("ST DEV: ", np.std(tor_width, ddof=1)) # ST DEV:  315.83093225491433


print("25th PCT: ", np.percentile(tor_width, 25)) # 25th PCT:  50.0
print("75th PCT: ", np.percentile(tor_width, 75)) # 75th PCT:  250.0


print(df['TOR_F_SCALE'].value_counts())
# TOR_F_SCALE
# EF1    1250
# EF0    1047
# EFU     497
# EF2     323
# EF3      86
# EF4       7

# Create a histogram using matplotlib
plt.hist(tor_width, bins=60, edgecolor='black')  # Adjust bins as needed
plt.title('Histogram of Tornado Width')
plt.xlabel('Width')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.show()
