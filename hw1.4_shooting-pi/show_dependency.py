
from sample_pi import sample_pi_shoots
import math
import matplotlib.pyplot as plt
import numpy as np

def initialize_plots(M, fullscreen=False):
    fig, axs = plt.subplots(2)
    fig.canvas.set_window_title('Homework 1')
    if fullscreen:
        fig.canvas.manager.full_screen_toggle()
    fig.suptitle(r'Showing: $\Delta x \sim \frac{1}{\sqrt{N}}$, M=' + str(M))
    axs[0].set_xlabel('N')
    axs[0].set_ylabel(r'$\Delta x$', rotation=0)
    axs[1].set_xlabel(r'$log(N)$')
    axs[1].set_ylabel(r'$log(\Delta x)$', rotation=0)
    return axs


def show_dependency():

    ratios = []
    Ns = []
    results = []
    M = 500

    axs = initialize_plots(M)

    for N in range (500, 10_001, 500):
        result = sample_pi_shoots(M, N, False)
        ratio = result[1] * math.sqrt(N)
        ratios.append(ratio)
        Ns.append(N)
        results.append(result)
        print(round(ratio, 3))
        
    axs[0].plot(Ns, np.array(results)[:, 1])
    axs[1].plot(np.log(np.array(Ns)), np.log(np.array(results)[:, 1]))
    plt.show()

if __name__ == '__main__':
    show_dependency()
