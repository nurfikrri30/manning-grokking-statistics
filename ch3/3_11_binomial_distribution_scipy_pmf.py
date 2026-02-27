from scipy.stats import binom

result = binom.pmf(k=7, n=10, p=.9)
print(result) # 0.05739562799999998
