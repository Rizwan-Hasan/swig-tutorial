#!/bin/bash

swig -python -c++ square.i
python setup.py build_ext --inplace
