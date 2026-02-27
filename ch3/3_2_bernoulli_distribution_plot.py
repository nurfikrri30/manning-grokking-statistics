import matplotlib.pyplot as plt

p = 0.7  #A
x = [0, 1]  #B
probabilities = [1-p, p]  #C

# Create the plot
plt.figure(figsize=(10, 6))
bars = plt.bar(x, probabilities,
              color=['#002d8b'],
              hatch=['///', 'xxx'],
              edgecolor='black')

plt.title('Bernoulli Distribution: MacBook Water Damage Recovery', pad=20)  #D
plt.xlabel('Outcome (0 = Not Recovered, 1 = Recovered)')  #D
plt.ylabel('Probability')  #D

for i, prob in enumerate(probabilities):  #E
   plt.text(i, prob, f'{prob:.2f}', ha='center', va='bottom')  #E

plt.xticks(x, ['Not Recovered\n(0)', 'Recovered\n(1)'])  #F

plt.grid(axis='y', linestyle='--', alpha=0.3)  #G

plt.tight_layout()  #H

import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()

#A probability of success (recovery)
#B possible outcomes
#C probabilities of failure and success
#D Add labels and title
#E Add value labels on top of bars
#F Customize x-axis ticks
#G Add grid for better readability
#H Adjust layout