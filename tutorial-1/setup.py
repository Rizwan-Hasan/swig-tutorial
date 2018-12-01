#!/usr/bin/env python

"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension

tutorial_module = Extension('_func',
                           sources=['func_wrap.cxx'],
                           )

setup (name = 'func',
       version = '0.1',
       author      = "Rizwan Hasan",
       description = """Simple swig tutorial for c++ functions""",
       ext_modules = [tutorial_module],
       py_modules = ["func"],
       )
