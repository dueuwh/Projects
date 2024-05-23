import numpy as np
import math as m
import matplotlib.pyplot as plt
from utils import params

class UKF():
    def __init__(self, num_window, ukfh=params.unscented_kalman_filter_hyperparameters):
        self.q = ukfh['Q']
        self.r = ukfh['R']
        self.p = ukfh['P']
        self.n_window = num_window

    def sigma_point(self, x_series, n_window):
        new_mean = sum(x_series) / n_window
        new_stdd = (sum([(new_mean - value) ** 2 for value in x_series]) / n_window) ** (1 / 2)
        output = [x for x in x_series if abs(x) <= new_stdd]
        return output

    def run(self, x):
        sigma_points = self.sigma_point(x, self.n_window)

        return sum(x) / len(x)


if __name__ == "__main__":

    ax = np.linspace(1, 21, 201)
    y = []
    y_noise = []
    for x in ax:
        y.append(m.log10(x))
        y_noise.append(m.log10(x) + np.random.normal(0, 0.15))

    ukf_ans = []
    time_window = 10
    window = []
    ukf_1 = UKF(time_window)
    m_avg = []
    print(f"y_noise length: {len(y_noise)}")
    for y_value in y_noise:
        window.append(y_value)
        if len(window) > time_window:
            del window[0]
            m_avg.append(sum(window) / len(window))

    plt.plot(ax, y, label="original signal", c='r')
    plt.plot(ax, y_noise, label="noise signal")
    plt.plot(ax[time_window:], m_avg, label="moving average signal")
    plt.title("UKF performance test")
    plt.legend()
    plt.show()
