import numpy as np

discrete_dist = {
  "BLACK": .4,
  "GREY": .3,
  "RED": .15,
  "GREEN": .07,
  "BLUE": .05,
  "YELLOW": .03
}

sample = np.random.choice([*discrete_dist.keys()], p=[*discrete_dist.values()])

# Outputs a color
print(sample)
