
# TheoIV
# 1. Exercise Sheet
#  -> 4. Shooting Pi

import numpy as np
import matplotlib.pyplot as plt
import time

# num_shoots is N from the exercise sheet.
def shoot_pi(num_shoots = 10, verbose = True):

    if verbose:
        print('Shooting PI with ' + str(num_shoots) + ' samples...')
    
    # shoot randomly (uniform) at 1x1 area and count hits on inner quarter circle.
    num_hits = 0
    for _ in range(num_shoots):
        point = np.random.rand(2)
        if (np.linalg.norm(point) < 1):
            num_hits += 1
    
    # compute pi as ratio of hits to all samples
    # (factor 4 necessary, since we're only shooting at a quarter circle)
    pi = (num_hits / num_shoots) * 4 

    if verbose:
        print('PI is approximately ', str(pi), '!', sep='')
    
    return pi


# num_samples is M from the exercise sheet.
def sample_pi_shoots(num_samples = 500, num_shoots_per_sample = 10, verbose = True):

    # shoot pi M times and compute mean + std of results
    pi_samples = []
    for _ in range(num_samples):
        pi_samples.append(shoot_pi(num_shoots_per_sample, False))
    pi_mean = np.mean(pi_samples, axis=0)
    pi_std = np.std(pi_samples, axis=0)
    pi_var = pi_std**2

    if verbose:
        print('Mean:', round(pi_mean, 3))
        print('Std: ', round(pi_std, 3))
        print('Var: ', round(pi_var, 3))

    return (pi_mean, pi_std, pi_var)


# show proportionality between standard deviation and 1/sqrt(N)
def show_dependency():

    M = 500
    Ns = []
    stds = []

    t = time.time()

    for N in range(500, 8_001, 500):
        (_, std, _) = sample_pi_shoots(M, N, False)
        Ns.append(N)
        stds.append(std)

    print('Runtime:', time.time()-t, 'seconds')
        
    fig, axs = plt.subplots(3)
    fig.canvas.set_window_title('Homework 1')
    fig.suptitle(r'Showing: $\Delta x \sim \frac{1}{\sqrt{N}}$, M=' + str(M))
    axs[0].set_xlabel('N', fontsize=15)
    axs[0].set_ylabel(r'$\Delta x$', rotation=0, fontsize=15)
    axs[0].plot(Ns, np.array(stds))
    axs[1].set_xlabel(r'$log(N)$', fontsize=15)
    axs[1].set_ylabel(r'$log(\Delta x)$', rotation=0, fontsize=15)
    axs[1].plot(np.log(np.array(Ns)), np.log(np.array(stds)))
    axs[2].set_xlabel(r'$\frac{1}{\sqrt{N}}$', fontsize=15)
    axs[2].set_ylabel(r'$\Delta x$', rotation=0, fontsize=15)
    axs[2].plot(1/np.sqrt(np.array(Ns)), np.array(stds))
    plt.show()

if __name__ == '__main__':
    # 4a):
    # shoot_pi(10_000)
    
    # 4b):
    show_dependency()
