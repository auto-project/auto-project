from distutils.core import setup, Extension

dtc_lib_module = Extension('_dtc_lib',
                           sources=['diaglib_wrap.cxx', 'diaglib.cpp'],
                           language="c++"
                           )

setup(name='dtc_lib',
      version='0.1',
      author="tsdim",
      description="""DTC library""",
      ext_modules=[dtc_lib_module],
      py_modules=["dtc_lib"]
      )
