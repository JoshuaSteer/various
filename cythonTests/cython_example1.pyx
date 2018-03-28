# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 10:21:48 2018

@author: js22g12
"""

cpdef int test(int x):
    cdef int y = 0
    cdef int i
    for i in range(x):
        y += i
    return y