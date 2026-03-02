import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import average_precision_score, precision_recall_curve


# Declare and reshape X column
x = np.array([0.1, 0.13, 0.22, 0.31, 0.38, 0.38,
              0.46, 0.5, 0.50, 0.56, 0.64, 0.7,
              0.70, 0.85, 0.96, 0.97, 1.06, 1.06,
              1.15, 1.2, 1.2, 1.22, 1.23, 1.24,
              1.31, 1.33, 1.33, 1.41, 1.5, 1.6,
              1.70, 1.78, 1.84, 1.9, 1.90, 1.91,
              1.98, 1.98, 2.03, 2.11, 2.31, 2.37,
              2.42, 2.5, 2.5, 2.50, 2.7, 2.77,
              2.82, 2.92, 3.17, 3.2, 3.28, 3.3,
              3.32, 3.35, 3.46, 3.48, 3.7, 3.77,
              3.8, 3.80, 3.81, 3.82, 3.86, 3.89,
              4.1, 4.20, 4.34, 4.48, 4.49, 4.5,
              4.5, 4.5, 4.63, 4.88, 4.90, 4.96,
              5., 5.07, 5.1, 5.11, 5.15, 5.23,
              5.26, 5.47, 5.6, 5.64, 5.7, 5.73,
              5.81, 5.92, 5.98, 5.99, 6.08, 6.11,
              6.11, 6.2, 6.21, 6.3]) \
    .reshape(-1, 1)  #A

y = np.array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
              0., 0., 0., 0., 0., 0., 0., 0.,0., 0.,
              0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
              0., 0., 1., 0., 0., 0.,0., 0., 0., 1.,
              0., 0., 0., 0., 1., 0., 0., 0., 0., 0.,
              1., 0., 1., 1.,1., 0., 0., 1., 1., 1.,
              0., 1., 0., 1., 1., 1., 1., 1., 1., 1.,
              1., 1.,1., 1., 1., 1., 1., 1., 0., 1.,
              1., 1., 1., 1., 0., 1., 1., 1., 1., 1.,
              1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])  #B


X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=1/3)  #C

model = LogisticRegression(penalty=None)  #D
model.fit(X_train, Y_train)  #D

proba = model.predict_proba(X_test)[:, 1]  #E Get predicted probabilities for the positive class

print(proba)  #F

ap = average_precision_score(Y_test, proba)  #G
print(f"AP: {ap:.4f}")  #G

#H Plot the precision-recall curve
precision, recall, thresholds = precision_recall_curve(Y_test, proba)  #H
no_skill = sum(Y_test) / len(Y_test)  #H
plt.figure()  #H
plt.plot(recall, precision, label=f'AP = {ap:.4f}')  #H
plt.plot([0, 1], [no_skill, no_skill], 'k--', label='No Skill')  #H
plt.xlim([0.0, 1.0])  #H
plt.ylim([0.0, 1.05])  #H
plt.xlabel('Recall')  #H
plt.ylabel('Precision')  #H
plt.title('Precision-Recall Curve')  #H
plt.legend(loc="lower right")  #H


import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()  #H

#A Declare and reshape X column
#B Declare Y column
#C Perform train/test split
#D Fit on the training data
#E Get probabilities on the test data
#F Show the probabilities (output will vary, e.g., [0.99 0.98 0.02 0.03 0.97 0.01 0.04 0.05 0.96])
#G Calculate and print AP (output will vary, e.g., 0.9658)
#H Compute and display the precision-recall plot (output will vary based on the split)