from random import random

p = 0.9  #A

outcomes = {key: 0 for key in range(11)}  #B

for i in range(10000):  #C

  successes = 0
  for j in range(10):  #D
      if random() < p:  #E
          successes += 1  #E

  outcomes[successes] +=1

for k,v in outcomes.items():  #F
  print(f"Experiments with {k} successes: {v}")  #F

#A probability of event
#B start each outcome at 0
#C We run 10,0000 experiments
#D Each experiment does 10 trials
#E simulate a weighted coin flip
#F Show outcomes of experiments

# ===========================================
# APPEND THE PLOT BELOW
# ===========================================

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 6))  #A

x = list(outcomes.keys())  #B
y = [count/10000 for count in outcomes.values()]  #C

bars = ax.bar(x, y, color='#002d8b', edgecolor='black', alpha=0.7)  #D

ax.set_title('Distribution of Successes in 10 Trials\n(p=0.9, 10000 experiments)', pad=20, fontsize=12)  #E
ax.set_xlabel('Number of Successes')  #F
ax.set_ylabel('Proportion of Experiments')  #G

ax.grid(True, linestyle='--', alpha=0.3)  #H

ax.set_xticks(x)  #I

for bar in bars:  #J
    height = bar.get_height()  #K
    ax.text(bar.get_x() + bar.get_width()/2., height, f'{height:.3f}', ha='center', va='bottom')  #L

plt.tight_layout()  #M

import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()

#A Create the visualization with a figure size of 12x6
#B Extract keys from outcomes dictionary for x-axis
#C Convert outcome counts to proportions for y-axis
#D Create bar plot with specified color, edge color, and transparency
#E Set plot title with padding and font size
#F Label x-axis
#G Label y-axis
#H Add grid with dashed lines and low opacity
#I Set x-axis ticks to match outcome keys
#J Iterate through bars to add value labels
#K Get height of each bar
#L Add text label above each bar showing its height to three decimal places
#M Adjust layout to prevent overlapping elements
