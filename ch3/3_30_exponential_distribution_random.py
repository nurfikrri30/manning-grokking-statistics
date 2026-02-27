from numpy.random import exponential as expon

mu = 10 # mean views per minute
times_between_views = expon(scale=1/mu, size=10)

print(times_between_views)
# Your times will vary
# array([0.04256854, 0.08893854, 0.04248317, 0.07514961, 0.05067546,
#       0.05795616, 0.01069159, 0.14543745, 0.17855999, 0.14383976])
