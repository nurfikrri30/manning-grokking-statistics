from scipy.stats import norm

mu, sigma = 64, 3
area = norm.cdf(63, mu, sigma) - norm.cdf(61, mu, sigma)

print(f"Area between 61 and 63: {area:.4f}")
# Area between 61 and 63: 0.2108
