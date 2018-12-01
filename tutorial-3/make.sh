#!/bin/bash

swig -python -c++ func.i
python setup.py build_ext --inplace
