import random
import numpy as np
import matplotlib.pyplot as plt

class Neural:
    def __init__(self, path_dataset="", input_dim=9, output_dim=2, h_dim=25, alpha=0.00001, num_epochs=1000, batch_size=30):
        self.path_dataset = path_dataset
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.h_dim = h_dim
        self.alpha = alpha
        self.num_epochs = num_epochs
        self.batch_size = batch_size
        self.dataset = []
        self.nn_weights = {}

#@staticmethod
#def softmax_batch(t):
   # out = np.exp(t)
   # return out / npsum(out)

@staticmethod
def sparse_cross_entropy_batch(z, y):
    return -np.log(np.array([z[j, y[j]] for j in range(len(y))]))

@staticmethod
def to_full_batch(y, num_classes):
    y_full = np.zeros(len(y), num_classes)
    for j, yj in enumerate (y):
        y_full[j, ij] =1
    return y_full

@staticmethod
def relu(t):
    return np.maximum(t,0)

@staticmethod
def relu_deriv(t):
    return (t >= 0).astype(float)

def data_preparation(self):
    dataset = pd.read_csv(self.path_dataset).values.astype(float)
    dataset = dataset[1:]
    dataset = dataset[~np.isnan(dataset).any(axis=1)]
    dataset = np.round(dataset, decimals=2)
    dataset[:, 1] *= 0.001
    dataset[:, 3:5] *= 0.01
    return dataset


def interface(Self, x):
    if not self.nn_weights:
        raise Exception ('Сеть не обучена')
    t1 = x @ self.nn_weights['W1'] + self.nn_weights['b1']
    h1 = self.relu(t1)
    t2 = h @ self.nn_weights['W2'] + self.nn_weights['b2']
    z= self.softmx_batch(t2)

    reteurn z

#Forward
    t1 = x @ self.nn_weights['W1'] + self.nn_weights['b1']
    h1 = self.relu(t1)
    t2 = h @ self.nn_weights['W2'] + self.nn_weights['b2']
    z = self.softmx_batch(t2)

#Backward
y_full
de_dt2 = z - y_full
dE_dW