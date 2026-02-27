import numpy as np

from scipy.stats import binom

n = 10  #A
p = 0.9  #B

k = np.arange(0, n + 1)  #C
y = binom.pmf(k, n, p)  #D

for _k, _y in zip(k, y):  #E
    print(f"The probability of {_k}/{n} successes is {_y:.4f}")  #F

#A Set number of trials to 10
#B Set probability of success to 0.9
#C Generate array of possible success counts from 0 to n
#D Calculate binomial probability for each k
#E Iterate through k and y values in pairs
#F Print probability of each success count formatted to four decimal places


# APPEND TO PREVIOUS CODE
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 6))  #A

bars = ax.bar(k, y, color='#002d8b', edgecolor='black', alpha=0.7)  #B

ax.set_title('Binomial Distribution (n=10, p=0.9)', pad=20, fontsize=12)  #C
ax.set_xlabel('Number of Successes')  #D
ax.set_ylabel('Probability')  #E

ax.grid(True, linestyle='--', alpha=0.3)  #F

ax.set_xticks(k)  #G

for bar in bars:  #H
    height = bar.get_height()  #I
    ax.text(bar.get_x() + bar.get_width()/2., height, f'{height:.3f}', ha='center', va='bottom')  #J

plt.tight_layout()

plt.show()

#A Create a figure and axis with size 12x6
#B Create bar plot with light gray bars, black edges, and 0.7 transparency
#C Set plot title with n=10, p=0.9, padding, and font size
#D Label x-axis as Number of Successes
#E Label y-axis as Probability
#F Add dashed grid with 0.3 opacity
#G Set x-axis ticks to match k values
#H Iterate through bars to add value labels
#I Get the height of each bar
#J Add text label above each bar showing height to three decimal places


# ===========================================
# APPEND THE PLOT BELOW
# ===========================================
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 6))

# Create bars with colors based on condition
colors = ['#404040' if x <= 8 else '#D3D3D3' for x in k]

# Create bars
bars = ax.bar(k, y,
             color=colors,
             edgecolor='black',
             alpha=0.7)

# Customize the plot
ax.set_title('Binomial Distribution (n=10, p=.9)',
            pad=20, fontsize=12)
ax.set_xlabel('Number of Successes')
ax.set_ylabel('Probability')

# Add grid
ax.grid(True, linestyle='--', alpha=0.3)

# Set x-axis ticks
ax.set_xticks(k)

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.3f}',
            ha='center', va='bottom')

# Adjust layout
plt.tight_layout()

# Save and show plot
import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()