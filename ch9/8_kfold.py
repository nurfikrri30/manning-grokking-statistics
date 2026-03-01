import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold

x = np.array([0.1, 0.5, 0.7, 1.2, 1.2, 1.5, 1.6, 1.9, 2.5, 2.5,
              2.7, 3.2, 3.3, 3.7, 3.8, 4.1, 4.5, 4.5, 4.5, 5.0,
              5.1, 5.6, 5.7, 6.2, 6.3]) \
    .reshape(-1, 1)  #A

y = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0,
              0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0,
              1.0, 1.0, 1.0, 1.0, 1.0])  #B

kf = KFold(n_splits=3, shuffle=True)  #C

accuracies = []  #C

for fold, (train_index, test_index) \
        in enumerate(kf.split(x), 1):  #C
    X_train, X_test = x[train_index], x[test_index]  #C
    Y_train, Y_test = y[train_index], y[test_index]  #C

    model = LogisticRegression(penalty=None)  #D
    model.fit(X_train, Y_train)  #D

    predictions = model.predict(X_test)  #E

    print(f"Fold {fold} predictions: "
          f"{predictions}")  #F

    accuracy = np.sum(predictions == Y_test) \
               / len(Y_test)  #G

    print(f"Fold {fold} accuracy: {accuracy:.4f}")  #G
    accuracies.append(accuracy)  #G

average_accuracy = np.mean(accuracies)  #G
print(f"Average accuracy: {average_accuracy:.4f}")  #G

std_dev = np.std(accuracies)  #H
print(f"Standard deviation: {std_dev:.4f}")  #H

#A Declare and reshape X column
#B Declare Y column
#C Perform 3-fold cross validation split
#D Fit on the training data for each fold
#E Predict on the test data for each fold
#F Show the predictions for each fold (output will vary, e.g., [1. 1. 0. 0. 1. 0. 0. 0. 1.])
#G Calculate and print accuracy for each fold and the average (output will vary, e.g., 0.8056)
#H Calculate and print the standard deviation of the accuracies (output will vary, e.g., 0.0982)