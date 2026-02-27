import os

import matplotlib.pyplot as plt

data = {
   "BLACK": .4,
   "GREY": .3,
   "RED": .15,
   "GREEN": .07,
   "BLUE": .05,
   "YELLOW": .03
}

plt.figure(figsize=(10, 6))  #A
plt.bar(data.keys(), data.values(), color='#002d8b', edgecolor='black')  #A

plt.title('Distribution of Colors', fontsize=12)  #B
plt.xlabel('Colors', fontsize=10)  #B
plt.ylabel('Probability', fontsize=10)  #B

for i, v in enumerate(data.values()):  #C
   plt.text(i, v, f'{v:.2f}', ha='center', va='bottom')  #C

plt.xticks(rotation=45)  #D

plt.grid(axis='y', linestyle='--', alpha=0.7)  #E

plt.tight_layout()  #F

plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()

#A Create the bar chart
#B Customize the chart
#C Add value labels on top of each bar
#D Rotate x-axis labels for better readability
#E Add grid for better readability
#F Adjust layout to prevent label cutoff