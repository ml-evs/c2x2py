from setuptools import setup, Extension
from Cython.Build import cythonize

cython_ext = Extension(
    name='c2x2py.api',
    sources=['c2x2py/bindings.pyx'],
    libraries=['check2xsf'],
    include_dirs=['/usr/local/include'],
    library_dirs=['/home/matthew/src/c2x_2.30', '.'],
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
