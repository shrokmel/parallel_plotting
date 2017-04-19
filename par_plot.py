#!/bin/python
 
#Copyleft Arvind Ravichandran
#Tue Apr 18 12:03:48 CEST 2017
#par_plot.py
#Description: Minimum working example of plotting multiple frames using multiprocessing

import matplotlib as mpl
mpl.use('Agg')
import multiprocessing
import matplotlib.pyplot as plt
import numpy as np
import time

def RandomWalk(N=100,d=2):
    """
    Generate random walk data
    """
    return np.cumsum(np.random.uniform(-0.5,0.5,(N,d)),axis=0)

def PlotRandomWalk2D(args):
    """
    Plot X,Y 2-D random walk
    """
    i,walk = args
    fig = plt.figure()
    X, Y = walk.T
    plt.plot(X,Y)
    plt.scatter(X[0],Y[0],c='g',s=100)
    plt.scatter(X[-1],Y[-1],c='r',s=100)    # ending position
    plt.axis('equal')
    fig.savefig('./fig_%02i.png' % i)

def main_par():
    pool = multiprocessing.Pool()   # Create Pool objects for parallelizing
    num_figs = 5                    # Number of frames

    # Generating some sort of data (load ALL frame data here)
    input = [(i,RandomWalk(N=1000,d=2)) for i in range(num_figs)]
   
    # Distribute plotting job across all available processors
    pool.map(PlotRandomWalk2D, input)

def main_serial():
    num_figs = 5                    # Number of frames

    # Generating some sort of data
    input = [(i,RandomWalk(N=1000,d=2)) for i in range(num_figs)]

    # Plot each frame within a for loop serially
    for i in input:
        PlotRandomWalk2D(i)

if __name__ == '__main__':
    t1 = time.time()
    main_serial()
    print("Serial time:\t", str(time.time()-t1))

    t1 = time.time()
    main_par()
    print("Parallel time:\t", str(time.time()-t1))
