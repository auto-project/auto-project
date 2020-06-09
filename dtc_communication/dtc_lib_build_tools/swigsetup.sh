#!/bin/sh
echo "Running SWIG..."
swig -c++ -python diaglib.i
echo "Building with distutils..."
python3 setup.py build_ext --inplace
echo "Copying files to 'dtc_manager' dir..."
mv _dtc_lib.*so _dtc_lib.so
cp _dtc_lib.so ../dtc_manager
cp dtc_lib.py ../dtc_manager
echo "Library built and copied to 'dtc_manager' dir!"
