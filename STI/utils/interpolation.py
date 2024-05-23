import numpy as np
from distributions import *
import matplotlib.pyplot as plt

class spline():
    def __init__(self, order):
        self.order = order

    def cubic(self):
        return 0

    def interpolation(self, x, y):
        output = (x, y)
        return output

def Laglange_interpolation():
    return 0

class Bayesian_interpolation():
    def __init__(self):
        self.order = '?'

# The methods(using LLM) is considered to utilize within time series data
# Core technique is embedding number series as tokens of LLM input
# RGB - rPPG ...etc
class Large_Language_Model():
    def __init__(self, model):
        self.model = model

def run_example():
    x_p = [i for i in range(30)]
    x_p_interpolation = np.linspace(0, 30, 301)
    lmda = 10
    p_1 = poisson(lmda=lmda)
    y_p = []
    for ax in x_p:
        y_p.append(p_1.output(ax))

    plt.scatter(x_p, y_p, s=10, c='r')
    plt.title("poisson distribution")
    plt.show()


if __name__ == "__main__":
    run_example()