@echo off
swig -python -c++ square.i
python setup.py build_ext --inplace
pause
