
import numpy as np
import matplotlib.pyplot as plt

def random_binary():
    return np.random.rand() > .5

def random_uniform(b = 1):
    return np.random.rand() * (2 * b) - b

def random_poisson():
    return np.random.poisson(2)

def Y(N, sample):
    y = 0
    for _ in range(N):
        y += sample()
    return y

def sample_Y(M, N, distribution):
    y_samples = []
    for _ in range(M):
        y_samples.append(Y(N, distribution))
    return np.array(y_samples)

def viz_Y(ys):
    fig, axs = plt.subplots(3)
    for i in range(3):
        axs[i].hist(ys[i], bins=200)
    plt.show()

if __name__ == '__main__':

    M = 10_000

    dist = random_uniform

    #for N in range(1, 2, 1):

    N = 50

    ys = []
    ys.append(sample_Y(M, N, random_binary))
    ys.append(sample_Y(M, N, random_uniform))
    ys.append(sample_Y(M, N, random_poisson))

    viz_Y(ys)
        

        

