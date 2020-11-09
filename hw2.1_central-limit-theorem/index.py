
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

if __name__ == '__main__':

    M = 10_000

    dists = (random_binary, random_uniform, random_poisson)

    _, axs = plt.subplots(5, 3)

    for i in range(5):
        N = int(np.power(np.power(100, 1/4), i))
        for j in range(3):
            sample = sample_Y(M, N, dists[j])
            axs[i][j].hist(sample, bins=200)
    plt.show()
