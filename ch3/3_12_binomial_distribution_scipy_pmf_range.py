from scipy.stats import binom

result = sum(binom.pmf(k, n=10, p=.9) for k in range(0,9))
print(result) # 0.2639010709
