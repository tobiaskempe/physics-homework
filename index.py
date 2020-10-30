
import sys
import random
import math
import numpy as np

def shoot_pi(num_samples = 10, verbose = True):

    if verbose:
        print('Shooting PI with ' + str(num_samples) + ' samples...')
    
    # shoot randomly (uniform) at 1x1 area at count hits of inner quarter circle.
    num_hits = 0
    for _ in range(num_samples):
        x = random.random()
        y = random.random()
        point = np.array([x, y])
        if (np.linalg.norm(point) < 1):
            num_hits += 1
    
    # compute pi as ratio of hits to all samples
    # (factor 4 necessary, since we're only shooting at a quarter circle)
    pi = (num_hits / num_samples) * 4 

    if verbose:
        print('PI is approximately ', str(pi), '!', sep='')
    
    return pi


if __name__ == '__main__':
    if len(sys.argv) == 2:
        shoot_pi(int(sys.argv[1]))
    else:
        shoot_pi()

