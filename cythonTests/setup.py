# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 10:22:35 2018

@author: js22g12
"""

from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('cython_example1.pyx'))
