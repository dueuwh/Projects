import numpy as np
import matplotlib.pyplot as plt
import math
import typing as t
import random


class generator_params():
    def __init__(self):
        self.gaussian_mean = 10
        self.gaussian_stdd = 1
        self.poisson_lmda = 10
        self.gaussian = {"mean":self.gaussian_mean, "stdd":self.gaussian_stdd}
        self.poisson = {"lmda":self.poisson_lmda}

    def get_parameters(self):
        return (self.gaussian, self.poisson)


class random_distribution_generator(generator_params):
    def __init__(self, num_mix):
        super().__init__()
        self.num_mix = num_mix

    def generate(self):

        return

class gaussian():
    def __init__(self, mean: t.Union[int, float], standard_deviation: t.Union[int, float]):
        self.m = mean
        self.stdd = standard_deviation
        self.v = self.stdd**2  # variance

    def update_parameter(self, mean: t.Union[int, float], standard_deviation: t.Union[int, float]):
        self.m = mean
        self.stdd = standard_deviation

    def get_parameters(self):
        return (self.m, self.stdd)

    def output(self, x: t.Union[int, float]) -> float:
        return 1/((2*math.pi*self.v)**(1/2))*math.exp(-((x-self.m)**2)/(2*self.v))

class poisson():
    def __init__(self, lmda):
        self.lmda = lmda

    def update_parameter(self, lmda):
        self.lmda = lmda

    def get_parameters(self):
        return (self.lmda)

    def output(self, k):
        return (self.lmda**k)*math.exp(-self.lmda)/math.factorial(k)

def run_example():
    x_g = np.linspace(0, 30, 301)
    x_p = [i for i in range(30)]
    y_g_1 = []
    y_p_1 = []
    mean = 15
    standard_dev = 1
    lmda = 3
    g_1 = gaussian(mean=mean, standard_deviation=standard_dev)
    p_1 = poisson(lmda=lmda)
    for i in x_g:
        y_g_1.append(g_1.output(i))

    for i in x_p:
        y_p_1.append(p_1.output(i))

    plt.title("statistical distribution graphs")
    plt.plot(x_g, y_g_1, label="gaussian distribution g_1")
    plt.scatter(x_p, y_p_1, s=2, c='r', label="poisson distribution p_1")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    run_example()