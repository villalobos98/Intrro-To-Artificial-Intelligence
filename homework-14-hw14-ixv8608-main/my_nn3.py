import pandas as pd

from np_nn3 import *

nn_architecture = [
    {"input_dim": 2, "output_dim": 6, "activation": "sigmoid"},
    {"input_dim": 6, "output_dim": 6, "activation": "relu"},
    {"input_dim": 6, "output_dim": 1, "activation": "sigmoid"}

]

data = pd.read_csv("dataset3.csv")
Xs = np.array(data[["X0", "X1"]]).T
Ys = np.array([data["Y"]])
learning_rate = 1.0
params_values, cost_history, accuracy_history = train(Xs, Ys, nn_architecture, 4000, learning_rate)
onestep = OneStep(Xs, Ys, params_values, cost_history, accuracy_history, nn_architecture)
onestep()
