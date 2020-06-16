import numpy as np
from math import pi

N = [ 10**3, 5*10**3, 10**4 ]
lc = 2.0736

def main():
    # termodinamycal threshold
    rt = lambda n: np.sqrt(lc/n)
    # connectivity threshold
    rc = lambda n: np.sqrt(np.log(n)/(n*pi))

    for n in N:
        if n == 10**3: x = 6e-2
        else: x = 4e-2
        # define radius of interest
        radius = [ 8e-1, 7e-1, 6e-1, 3e-1, 1e-1, x,                     # connected regime (high - low)
                rt(n) + (rc(n) - rt(n))/3, rt(n) + 2*(rc(n) - rt(n))/3, # supercritical regime
                rt(n) * 1/np.sqrt(10), rt(n) * 1/np.sqrt(2) ]           # subscritical regime
        print('radius', n, radius)
        print()
        # save probabilities
        with open('data/keys{}.txt'.format(str(n)), 'w') as f:
            #saving keys to file
            f.write(str(radius))

    # save the explored values of n
    np.save('data/sizes.npy', N)
    # save resistances thresholds
    np.save('data/res_phase1.npy', [ 0.25, 0.5, 0.75, 1 ])  # phase 1 values

if __name__ == "__main__":
    main()
