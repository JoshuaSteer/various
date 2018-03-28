# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 11:29:16 2018

@author: js22g12
"""

import timeit

cy = timeit.timeit('''cython_example1.test(5000000)''',setup='import cython_example1',number=100)
py = timeit.timeit('''python_example1.test(5000000)''',setup='import python_example1', number=100)

print(cy, py)
print('Cython is {}x faster'.format(py/cy))