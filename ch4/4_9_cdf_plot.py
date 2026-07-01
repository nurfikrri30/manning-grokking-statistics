import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mu, sigma = 64, 3  #A
x = np.linspace(mu - sigma * 4, mu + sigma * 4, 1000)  #B
y = norm.cdf(x, mu, sigma)  #C

target_x = 63  #D
target_y = norm.cdf(target_x, mu, sigma)  #E

xmin = mu - sigma * 4
xmax = mu + sigma * 4

plt.plot(x, y, color='#1f77b4', linewidth=2)  #F

# Set boundaries (Starting ylim at 0 ensures the line touches the x-axis frame)
plt.xlim(xmin, xmax)  #G
plt.ylim(0, 1.05)  #H

# Draw perpendicular dashed lines meeting at the curve
plt.vlines(target_x, 0, target_y, colors='#002d8b', linestyles='dashed', alpha=0.8)  #I
plt.hlines(target_y, xmin, target_x, colors='#002d8b', linestyles='dashed', alpha=0.8)  #J

# Plot a point at the intersection on the curve
plt.scatter(target_x, target_y, color='#002d8b', zorder=5)  #K

# Add a text label for the retrieved value just above the horizontal line
plt.text(xmin + 0.3, target_y + 0.02, f"    A = {target_y:.4f}", color='#002d8b', fontweight='bold')  #L

plt.title("Weight Distribution of Golden Retrievers (CDF)")  #M
plt.xlabel("Weight (lbs)")  #N
plt.ylabel("Cumulative Probability")  #O
plt.grid(True, alpha=0.3)  #P

import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()  #Q

#A Set mean to 64 and standard deviation to 3
#B Generate 1000 evenly spaced points from mu-4*sigma to mu+4*sigma
#C Compute normal distribution CDF for given x values
#D Define the target weight of 63 lbs
#E Calculate the cumulative probability at 63 lbs
#F Plot the main CDF curve
#G Match x-axis limits exactly to data range
#H Set y-axis lower limit to exactly 0 so the vertical line touches the bottom axis
#I Draw a vertical dashed line from the x-axis (0) up to the curve at 63
#J Draw a horizontal dashed line from the y-axis up to the curve at the target probability
#K Place a marker dot at the exact intersection point on the curve
#L Label the retrieved value on the y-axis (formatted to 3 decimal places)
#M Set plot title
#N Label x-axis
#O Label y-axis
#P Add grid with 0.3 opacity
#Q Display the plot