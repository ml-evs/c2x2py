from setuptools import setup, Extension
from Cython.Build import cythonize

import os
build_dir = os.environ.get("C2X_DIR")
if build_dir is None:
    raise RuntimeError(
        """ Please set C2X_DIR environment variable to the location of your libcheck2xsf.so and c2xsf.h files.
        his dir should also be on your LD_LIBRARY_PATH."""
    )

cython_ext = Extension(
    name='c2x2py.api',
    sources=['c2x2py/bindings.pyx'],
    libraries=['check2xsf'],
    include_dirs=[build_dir],
    library_dirs=[build_dir],
    depends=['c2xsf.h'],
    language='c'
)

setup(
    name='c2x2py',
    packages=['c2x2py'],
    license="GPLv3",
    version=0.1,
    setup_requires=['cython'],
    ext_modules=cythonize([cython_ext]),
    zip_safe=False,
)
