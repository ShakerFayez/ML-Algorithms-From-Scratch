import numpy as np

# computes the euclidean distance
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum(x2-x1)**2)

# computes the mean squared error
def mse(y_true, y_predicted):
    return np.mean((y_true - y_predicted)**2)

# computes the accuracy score
def accuracy_score(y_true, y_predicted):
    return np.sum(y_true == y_predicted) / len(y_true)