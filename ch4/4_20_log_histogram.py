import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/thomasnield/"
                 "training-data-repository/refs/heads/main/TORNADO_TRX.csv")  #A

tor_width = df['TOR_WIDTH']  #B

log_tor_width = np.log10(tor_width)  #C

plt.hist(log_tor_width, bins=20, edgecolor='black')  #D
plt.title('Histogram of Log-Transformed Tornado Width')  #E
plt.xlabel('Log(Width)')  #F
plt.ylabel('Frequency')  #G
plt.grid(True, alpha=0.3, color='#002d8b')  #H

import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()  #I

print("Log-transformed tornado width:")  #J
print("MEAN: ", np.mean(log_tor_width))  #K
print("MEDIAN: ", np.median(log_tor_width))  #L

#A Load tornado data from CSV file hosted on GitHub
#B Extract tornado width column
#C Apply log transformation with base 10 to tornado width data
#D Create histogram of log-transformed data with 20 bins and black edges
#E Set plot title
#F Label x-axis
#G Label y-axis
#H Add grid with 0.3 opacity and blue color
#I Display the plot
#J Print header
#K MEAN:  2.0056436474610417
#L MEDIAN:  2.0
