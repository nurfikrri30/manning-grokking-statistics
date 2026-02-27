mu, sigma = 27.6, 3.2

min68, max68 = mu-sigma*1, mu+sigma*1
print(f"68% of baristas report coffee measurement between {min68:.1f} and {max68:.1f} grams")

min95, max95 = mu-sigma*2, mu+sigma*2
print(f"95% of baristas report coffee measurement between {min95:.1f} and {max95:.1f} grams")

min99_7, max99_7  = mu-sigma*3, mu+sigma*3
print(f"99.7% of baristas report coffee measurement between {min99_7:.1f} and {max99_7:.1f} grams")

# 68% of baristas report coffee measurement between 24.4 and 30.8 grams
# 95% of baristas report coffee measurement between 21.2 and 34.0 grams
# 99.7% of baristas report coffee measurement between 18.0 and 37.2 grams
