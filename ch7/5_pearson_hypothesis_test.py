from scipy.stats import pearsonr
import numpy as np

x = np.array([ 51.5,  55.1,  63.0,  71.2,  73.0 ,
               77.1,  88.1,  91.2,  93.0, 101.6])

y = np.array([100.98, 137.44, 237.8 , 254.96, 263.45,
              353.89, 450.32, 521.34, 503.13, 573.91])

r, p = pearsonr(x, y)
print(f"Pearson correlation (SciPy): {r:.4f},"  #A
      f" p-value: {p:.10f}")  #A

if p < 0.05:  #B
    print("Reject the null hypothesis")  #B
else:  #B
    print("Fail to reject the null hypothesis")  #B

#A Pearson correlation: 0.9889, p-value: 0.0000000654
#B Check the p-value is less than 0.05, reject H0