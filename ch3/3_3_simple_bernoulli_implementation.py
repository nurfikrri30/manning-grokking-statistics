bernoulli = {
    0 : .30,
    1: .70
}

for x,p in bernoulli.items():
    print(f"P(X={x}) = {p}")

# PRINTS:
# P(X=0) = 0.30
# P(X=1) = 0.70