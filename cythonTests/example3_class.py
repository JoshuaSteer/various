# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 12:27:40 2018

@author: js22g12
"""
import numpy as np 
from cython_example3 import cythonMixin
from python_example3 import pythonMixin

class pycyTest(cythonMixin, pythonMixin):
    
    def __init__(self, f, g):
        self.f = f
        self.g = g