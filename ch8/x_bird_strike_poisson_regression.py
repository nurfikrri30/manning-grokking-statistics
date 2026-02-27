
import numpy as np
import pandas as pd
from sklearn.linear_model import PoissonRegressor
import matplotlib.pyplot as plt

df = pd.read_csv('birdstrike.csv')

df = df[df['HEIGHT'].isna() == False]

# bin up bird strikes by height, in buckets of 100 feet
max_height = int(df['HEIGHT'].max() // 100 + 1) * 100
bins = list(range(0, max_height + 100, 100))
df['HEIGHT_BIN'] = pd.cut(df['HEIGHT'], bins=bins, right=False)
incidents_by_bin = df['HEIGHT_BIN'].value_counts().sort_index()

# extract out x and y
X = np.arange(start=0, stop=max_height, step=100).reshape(-1,1)
y = incidents_by_bin.values

model = PoissonRegressor()
model.fit(X, y)

y_pred = model.predict(X)
plt.scatter(X, y, color='orange', label='Observed')
plt.plot(X, y_pred, color='red', label='Poisson Fit')
plt.xlabel('x')
plt.ylabel('Count (y)')
plt.title('Poisson Regression')
plt.legend()
plt.show()