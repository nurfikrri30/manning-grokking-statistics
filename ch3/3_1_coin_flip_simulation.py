from random import random

heads, tails = 0, 0
p = 0.5 # probability of event (heads)

for i in range(1000):
    if random() < p:
        heads += 1
    else:
        tails += 1

# Should roughly be 500 heads, 500 tails
print(f"HEADS: {heads}, TAILS: {tails}")