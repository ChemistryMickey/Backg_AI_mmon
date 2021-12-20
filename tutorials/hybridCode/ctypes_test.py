# ctypes_test.py
import ctypes
import pathlib

if __name__ == "__main__" :
    #load shared library
    libname = pathlib.Path().absolute() / "libcmult.so"; #getting the library path
    c_lib = ctypes.CDLL(libname); #attaching the variable c_lib to the 
    c_lib.cmult.restype = ctypes.c_float; #telling python that the function returns a float

    x, y = 6, 2.3;
    answer = c_lib.cmult(x, ctypes.c_float(y));

    print( f'In Python: int: {x} float {y:.1f} return val {answer:.1f}' );