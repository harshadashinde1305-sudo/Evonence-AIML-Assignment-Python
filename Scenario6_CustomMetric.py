Scenario 6: Custom Evaluation Metric
Python
import numpy as np

def weighted_accuracy(y_true, y_pred):
    weights = np.where(np.array(y_true) == 0, 1, 2)
    correct = (np.array(y_true) == np.array(y_pred)).astype(int)
    
    return np.sum(weights * correct) / np.sum(weights)
