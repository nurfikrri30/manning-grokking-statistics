from scipy.stats import norm
from math import sqrt

mu = 98.2  #A
sigma = .73  #B
n = 31  #C

mu_sample_means = mu  #D
sigma_sample_means = sigma / sqrt(n)  #E

A = norm.cdf(98.0, mu_sample_means, sigma_sample_means)  #F

print(f"P(sample mean < 98.0): {A:.4f}")  #G
# P(sample mean < 98.0): 0.0636

#A Population mean is 98.2
#B Population standard deviation is 0.73
#C Sample size is 31
#D Mean of sample means equal to population mean
#E Calculate standard deviation of sample means
#F Compute probability of sample mean less than 98.0 using normal CDF
#G Print probability to four decimal places: P(sample mean < 98.0): 0.0636
