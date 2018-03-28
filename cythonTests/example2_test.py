# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 11:44:17 2018

@author: js22g12
"""

import timeit

setup = """
import %sython_example2
import numpy as np
"""

func = """
N = 600
f = np.arange(N*N, dtype=np.int).reshape((N,N))
g = np.arange(81, dtype=np.int).reshape((9, 9))
%sython_example2.naive_convolve(f, g)
"""

cy = timeit.timeit(func % 'c',setup=setup % 'c',number=1)
py = timeit.timeit(func % 'p',setup=setup % 'p',number=1)

print(cy, py)
print('Cython is {}x faster'.format(py/cy))