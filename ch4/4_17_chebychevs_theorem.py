mu, sigma = 7, 1.5

k = 3.0
p_min = 1.0 - (1.0/k**2)
lower,upper = mu-3*sigma, mu+3*sigma

print(f"At least {p_min*100:.1f}% of chips last between {lower:.1f} and {upper:.1f} years.")
# At least 88.9% of chips last between 2.5 and 11.5 years.