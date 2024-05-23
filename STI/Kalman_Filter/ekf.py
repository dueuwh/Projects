# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 23:31:47 2024

@author: ys
"""

import numpy as np
from params import Params
import os
import matplotlib.pyplot as plt
import math


class UKF():
    def __init__(self):
        u = unscented_kalman_filter_hyperparameters['U']


if __name__ == "__main__":

    a = np.zeros((2, 3))
    a[0, :] = [1, 2, 3]
    a[1, :] = [3, 2, 1]
    arr_list = []
    arr_list.append(a)
    a[0, :] = [2, 3, 4]
    a[1, :] = [4, 3, 2]
    arr_list.append(a)
    a[0, :] = [3, 4, 5]
    a[1, :] = [5, 4, 3]
    arr_list.append(a)
    print(arr_list)

    ax = np.linspace(1, 21, 201)
    y = []
    y_noise = []
    for x in ax:
        y.append(math.log10(x))
        y_noise.append(math.log10(x) + np.random.normal(0, 0.15))
    plt.plot(ax, y, label="original signal", c='r')
    plt.plot(ax, y_noise, label="noise signal")
    plt.title("UKF performance test")
    plt.legend()
    plt.show()