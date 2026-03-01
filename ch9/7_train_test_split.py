import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

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

predictions = model.predict(X_test)  #E

print(predictions)  #F

accuracy = np.sum(predictions == Y_test) / len(Y_test)  #G
print(f"Accuracy: {accuracy:.4f}")  #G

#A Declare and reshape X column
#B Declare Y column
#C Perform train/test split
#D Fit on the training data
#E Predict on the test data
#F Show the predictions (output will vary, e.g., [1. 1. 0. 0. 1. 0. 0. 0. 1.])
#G Calculate and print accuracy (output will vary, e.g., 0.7778)