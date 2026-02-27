import numpy as np
from sklearn.linear_model import LogisticRegression

# Declare and reshape X column
x = np.array([0.1, 0.5, 0.7, 1.2, 1.2, 1.5, 1.6, 1.9, 2.5, 2.5,
              2.7, 3.2, 3.3, 3.7, 3.8, 4.1, 4.5, 4.5, 4.5, 5.0,
              5.1, 5.6, 5.7, 6.2, 6.3]).reshape(-1, 1)

# Declare Y column
y = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0,
              0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0,
              1.0, 1.0, 1.0, 1.0, 1.0])

# Fit a logistic regression
model = LogisticRegression(penalty=None)
model.fit(x, y)

# Extract and print coefficients
b1 = model.coef_.flatten()[0]
b0 = model.intercept_[0]
print(f"β₀={b0:.4f}, β₁={b1:.4f}")
# β₀=-7.0587, β₁=2.2047