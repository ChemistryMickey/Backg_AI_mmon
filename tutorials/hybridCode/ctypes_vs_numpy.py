#!/bin/python3

# Ctypes/C vs. Numpy 
import pathlib
import numpy as np
import ctypes
from time import process_time

benchmarkSize = 50000;

def main():
    ## Numpy test
    npArr = np.ones((benchmarkSize, benchmarkSize));

    # Loop though each index and sum row
    simpleStart = process_time();
    simpleSum = 0;
    for iInd in range(benchmarkSize):
        simpleSum += np.sum( npArr[iInd, :] );
    simpleSum = int( simpleSum );
    simpleEnd = process_time();
    # print(f'It took {simpleEnd - simpleStart} seconds to complete a simple loop over {benchmarkSize} indexes: {simpleSum}' );

    # Do more clever python
    arrStart = process_time();
    arrSum = int( np.sum([np.sum(x) for x in npArr[:, :]]) );
    arrEnd = process_time();
    # print(f'It took {arrEnd - arrStart} seconds to complete a vectorized loop over {benchmarkSize} indexes: {arrSum}' );

    ## C test
    attachStart = process_time();
    libname = pathlib.Path().absolute() / "libArrSum.so"; #getting the library path
    c_lib = ctypes.CDLL(libname); #attaching the variable c_lib to the shared library
    c_lib.arr_sum.restype = ctypes.c_long; #telling python that the function returns a float
    attachEnd = process_time();
    # print( f'It took {attachEnd - attachStart} seconds to attach the shared library to python' );

    cStart = process_time();
    cSum = c_lib.arr_sum(benchmarkSize);
    cEnd = process_time();
    # print( f'It took {cEnd - cStart} seconds to complete a C loop over {benchmarkSize} indexes: {cSum}: {cSum}');

    print( f'C is {int( (arrEnd - arrStart) / (cEnd - cStart) )} times faster than Numpy');



if __name__ == '__main__':
    main();