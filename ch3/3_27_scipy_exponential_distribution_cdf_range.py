from numpy.random import exponential as expon

mu = 10  #A
times_between_views = expon(scale=1/mu, size=10)  #B

print(times_between_views)  #C

#A Set mean views per minute to 10
#B Generate 10 samples from exponential distribution with scale parameter 1/mu
#C Print the generated times between views, yours will vary
