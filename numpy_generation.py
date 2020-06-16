"""
Created on Mon May 25 2020

@author: Laura Iacovissi
"""

import time
import datetime
import argparse
import numpy as np
from scipy.spatial.distance import pdist, squareform


def main():
    # define arguments
    parser = argparse.ArgumentParser()
    # graph size
    parser.add_argument('--n', type=int)
    # dimension of the hypercube
    parser.add_argument('--d', type=int, default=2)
    # parameter of the minkowski distance
    parser.add_argument('--p', type=int, default=2)
    # index of the radius to use
    parser.add_argument('--r', type=int)
    # append or not
    parser.add_argument('--app', dest='append', action='store_true')
    parser.add_argument('--no_app', dest='append', action='store_false')
    parser.set_defaults(append=False)
    # number of samples
    parser.add_argument('--k', type=int, default=50)
    # parse arguments to dictionary
    args = parser.parse_args()

    print(args)

    # load radius r_i
    with open('data/keys{}.txt'.format(args.n), 'r') as f:
        radius = eval(f.read())
    # pick the probability of interest
    r = radius[args.r]
    del radius

    # info
    start_time = time.time()
    # data path
    path = 'data/graphs/'

    # generate n positions (hidden variables) in the [0,1]^d space
    pos = np.random.uniform(0,1,(args.n, arg.d, args.k))
    # compute the pairwise distances
    A = np.zeros((args.n, args.n, args.k))
    for i in range(args.k):
        A[:,:,i] = squareform(pdist(pos[:,:,i], 'minkowski', args.p))
        # fill diagonal with zeros in place
        np.fill_diagonal(A[i,:,:], 0)
    # filter with radius
    A[A > r] = 0
    A[A != 0] = 1
    np.save(path+'graph_{}_{}.npy'.format(args.n, r), A)
    np.save(path+'positions_{}_{}.npy'.format(args.n, r), pos)

    # info
    end_time = time.time()
    uptime = end_time - start_time
    human_uptime = datetime.timedelta(seconds=uptime)
    print("\n\nG({},{})'s samples generation uptime: {}".format(args.n, r, human_uptime))

if __name__ == "__main__":
    main()
