from ctypes import c_float,cdll,c_double

from os import environ

if environ.has_key("GROMPYDOUBLE"):
    isdouble=True
    print "Loading grompy with double precision library"
    c_real = c_double
    libmd=cdll.LoadLibrary("libmd_d.so")
    libgmx=cdll.LoadLibrary("libgmx_d.so")
else:
    isdouble=False
    print "Loading grompy with single precision library"
    c_real = c_float
    libmd=cdll.LoadLibrary("libmd.so.6")
    libgmx=cdll.LoadLibrary("libgmx.so.6")


rvec=c_real*3
matrix=c_real*3*3

class GMXctypesError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
