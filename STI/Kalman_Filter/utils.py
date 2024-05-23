import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from sklearn.model_selection import train_test_split as tts
import pandas as pd

class params:
    unscented_kalman_filter_hyperparameters = {
        'Q': np.array([[0.1, 0, 0], [0, 0.1, 0], [0, 0, 0.1]]),
        'R': np.array([[100, 100, 100]]),
        'P': 100
    }


# Best ARIMA model for treadmill dataset: (7, 1, 2)
class kalman_state:
    def __init__(self, fit_function, state_type, **kwargs):
        self.fit_function = fit_function
        self.state_type = state_type
        if fit_function == "ARIMA":
            self.ar = kwargs["AR"]
            self.diff = kwargs["I"]
            self.ma = kwargs["MA"]


    def load_fit_data(self):
        return 0


    def split_data(self):
        observation = pd.read_csv()
        label = pd.read_csv()
        tts()


    def fit_torch(self, learning_rate):
        # arima_model =
        # optimizer = optim.Adam(, lr=learning_rate)
        return 0


    def measurement_arima(self, x):
        output = x + 1
        return output


    def observation_arima(self, x):
        output = x + 1
        return output

