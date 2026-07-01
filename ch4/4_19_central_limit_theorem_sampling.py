import pandas as pd
from matplotlib import pyplot as plt
import numpy as np  #A

n_samples = 1000  #B
sample_size = 45  #C

df = pd.read_csv("https://raw.githubusercontent.com/thomasnield/"
                 "training-data-repository/refs/heads/main/TORNADO_TRX.csv")  #D

sample_means = [
    df['TOR_WIDTH'].sample(sample_size).mean() for _ in range(n_samples)
]  #E

print(f"SAMPLE MEANS MEAN: {np.mean(sample_means):.4f}, SAMPLE MEANS MEDIAN: {np.median(sample_means):.4f}")  #F

plt.hist(sample_means, bins=40, color='#002d8b')  #G

import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()  #H

#A Import NumPy for numerical operations
#B Set number of samples to 1000
#C Set size of each sample to 45
#D Load tornado data from CSV file hosted on GitHub
#E Generate a list of means from 1000 samples of tornado width data
#F Print mean and median of sample means formatted to four decimal places
#G Create histogram of sample means with 40 bins and blue color
#H Display the plot
