# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 12:53:19 2018

@author: js22g12
"""

import timeit

setup = """
from example3_class import pycyTest
import numpy as np
"""

func = """
N = 600
f = np.arange(N*N, dtype=np.int32).reshape((N,N))
g = np.arange(81, dtype=np.int32).reshape((9, 9))
pycy = pycyTest(f, g)
pycy.naive_convolve_%sy()
"""

cy = timeit.timeit(func % 'c',setup=setup,number=1)
py = timeit.timeit(func % 'p',setup=setup,number=1)

print(cy, py)
print('Cython is {}x faster'.format(py/cy))