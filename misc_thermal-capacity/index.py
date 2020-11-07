
import numpy as np
import scipy.constants as const
import matplotlib.pyplot as plt

def Capacity(T):
    beta = 1/const.Boltzmann/T
    w_E = 1e13
    x = beta * const.hbar * w_E
    return 3 * const.Boltzmann * x**2 * np.exp(x) / (np.exp(x) - 1)**2

if __name__ == '__main__':
    T = np.arange(3, 400, 1)
    C = Capacity(T)
    T_ = 1/T
    plt.plot(T_, C)
    plt.show()
    