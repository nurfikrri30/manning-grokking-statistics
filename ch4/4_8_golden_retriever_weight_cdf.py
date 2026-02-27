from scipy.stats import norm

mu, sigma = 64, 3
area = norm.cdf(63, mu, sigma)
print(f"Area under curve: {area:.4f}")
# Area under curve: 0.3694
