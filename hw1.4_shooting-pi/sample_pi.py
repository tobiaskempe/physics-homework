
import numpy as np
from shoot_pi import shoot_pi
import argparse

# num_samples is M from the exercise sheet.
def sample_pi_shoots(num_samples = 500, num_shoots_per_sample = 10, verbose = True):
    pi_samples = []
    for _ in range(num_samples):
        pi_samples.append(shoot_pi(num_shoots_per_sample, False))
    pi_mean = np.mean(pi_samples, axis=0)
    pi_std = np.std(pi_samples, axis=0)

    if verbose:
        print('Mean:', round(pi_mean, 3))
        print('Std: ', round(pi_std, 3))

    return (pi_mean, pi_std)

if __name__ == '__main__':
    #parser = argparse.ArgumentParser()
    #parser.add_argument()
    sample_pi_shoots()
    