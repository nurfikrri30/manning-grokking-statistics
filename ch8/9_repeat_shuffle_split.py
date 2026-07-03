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

accuracies = []  #C

for i in range(100):  #C
    X_train, X_test, Y_train, Y_test = \
        train_test_split(x, y, test_size=1/3)  #C

    model = LogisticRegression(penalty=None)  #D
    model.fit(X_train, Y_train)  #D

    predictions = model.predict(X_test)  #E

    accuracy = np.sum(predictions == Y_test) \
               / len(Y_test)  #G
    accuracies.append(accuracy)  #G

average_accuracy = np.mean(accuracies)  #G
print(f"Average accuracy: {average_accuracy:.4f}")  #G

std_dev = np.std(accuracies)  #H
print(f"Standard deviation: {std_dev:.4f}")  #H

#A Declare and reshape X column
#B Declare Y column
#C Perform random train/test split 100 times
#D Fit on the training data for each split
#E Predict on the test data for each split
#G Calculate accuracy for each split and the average (output will vary, e.g., 0.8778)
#H Calculate and print the standard deviation of the accuracies (output will vary, e.g., 0.0882)