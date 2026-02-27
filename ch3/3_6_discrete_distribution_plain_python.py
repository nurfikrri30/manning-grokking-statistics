discrete_dist = {
  "BLACK": .4,
  "GREY": .3,
  "RED": .15,
  "GREEN": .07,
  "BLUE": .05,
  "YELLOW": .03
}

for x,p in discrete_dist.items():
   print(f"P(X={x}) = {p}")

#PRINTS:
# P(X=BLACK) = 0.4
# P(X=GREY) = 0.3
# P(X=RED) = 0.15
# P(X=GREEN) = 0.07
# P(X=BLUE) = 0.05
# P(X=YELLOW) = 0.03
