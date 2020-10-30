
from sample_pi import sample_pi_shoots
import math
import matplotlib.pyplot as plt
import numpy as np

def show_dependency():
    ratios = []
    Ns = []
    results = []
    M = 500
    for N in range (500, 10_001, 500):
        result = sample_pi_shoots(M, N, False)
        ratio = result[1] * math.sqrt(N)
        ratios.append(ratio)
        Ns.append(N)
        results.append(result)
        print(round(ratio, 3))
    fig, axs = plt.subplots(2)
    fig.canvas.set_window_title('Homework 1')
    fig.suptitle(r'Showing: $\Delta x \sim \frac{1}{\sqrt{N}}$, M=' + str(M))
    #fig.tight_layout(pad=3)
    axs[0].plot(Ns, np.array(results)[:, 1])
    axs[0].set_xlabel('N')
    axs[0].set_ylabel(r'$\Delta x$', rotation=0)
    #plt.show()
    axs[1].plot(1/np.sqrt(np.array(Ns)), np.array(results)[:, 1])
    axs[1].set_xlabel(r'$\frac{1}{\sqrt{N}}$')
    axs[1].set_ylabel(r'$\Delta x$', rotation=0)
    plt.show()
    #plt.title('1/sqrt(N) ~ delta_x')
    #plt.show()


if __name__ == '__main__':
    show_dependency()
