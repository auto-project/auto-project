#!/bin/sh
echo "Removing files from the build."
rm -r build
rm diaglib_wrap.cxx
rm _dtc_lib*.so
rm dtc_lib.py
echo "Directory cleaned from build files!"
