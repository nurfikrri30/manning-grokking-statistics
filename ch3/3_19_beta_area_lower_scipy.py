from scipy.stats import beta
a, b = 7, 3 # successes, failures
area = beta.cdf(.4, a, b)
print(f"AREA: {area}") # 0.025034752000000007
