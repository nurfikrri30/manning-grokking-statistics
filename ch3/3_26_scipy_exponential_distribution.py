from scipy.stats import expon

mu = 10 # mean views per minute
area = expon.cdf(.4, scale=1/mu)

# AREA: 0.9816843611112658
print(f"AREA: {area}")
