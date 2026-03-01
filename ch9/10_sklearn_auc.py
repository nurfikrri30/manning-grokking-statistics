import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score  # Added for AUC calculation

x = np.array([0.1, 0.5, 0.7, 1.2, 1.2, 1.5, 1.6, 1.9, 2.5, 2.5,
              2.7, 3.2, 3.3, 3.7, 3.8, 4.1, 4.5, 4.5, 4.5, 5.0,
              5.1, 5.6, 5.7, 6.2, 6.3]) \
    .reshape(-1, 1)  #A

y = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0,
              0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0,
              1.0, 1.0, 1.0, 1.0, 1.0])  #B

X_train, X_test, Y_train, Y_test = \
    train_test_split(x, y, test_size=1/3)  #C

model = LogisticRegression(penalty=None)  #D
model.fit(X_train, Y_train)  #D

proba = model.predict_proba(X_test)[:, 1]  #E Get predicted probabilities for the positive class

print([f"{p:.4f}" for p in proba])  #F

auc = roc_auc_score(Y_test, proba)  #G
print(f"AUC: {auc:.4f}")  #G

#A Declare and reshape X column
#B Declare Y column
#C Perform train/test split
#D Fit on the training data
#E Get probabilities on the test data
#F Show the probabilities (output will vary, e.g., [0.99 0.98 0.02 0.03 0.97 0.01 0.04 0.05 0.96])
#G Calculate and print AUC (output will vary, e.g., 0.9658)