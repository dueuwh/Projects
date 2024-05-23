import numpy as np
import matplotlib.pyplot as plt
import math
import typing as t
import random
from utils.interpolation import spline

class mle():
    def __init__(self, model, population):
        self.pop = population
        self.model = model
        self.parameters = model.get_parameters()
        print("model parameters found by mle: ", self.parameters)

if __name__ == "__main__":
    print("?")