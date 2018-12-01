@echo off
swig -python -c++ func.i
python setup.py build_ext --inplace
pause
