# cython: language_level=3

cimport c2x
from libc.stdlib cimport malloc
from cpython.mem cimport PyMem_Malloc, PyMem_Realloc, PyMem_Free
from cpython cimport array
import array

cdef class UnitCell:

    cdef c2x.unit_cell _unit_cell

    def __init__(self, basis=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]):
        # cdef double[:][:] tmp_basis
        # self._unit_cell.basis =
        tmp_basis = basis

        new = <double*> malloc(9*sizeof(double))

        self._unit_cell.basis = new
        # vol = c2x.volume(basis)
        # self._unit_cell.vol = vol
        print('Created unit cell with {} volume'.format(basis))# self._unit_cell.basis))

    # def __repr__(self):
        # print('UnitCell: vol = {} A^3'.format(self.volume))

    @property
    def volume(self):
        return self._unit_cell.vol

    @volume.setter
    def volume(self, vol: float):
        self._unit_cell.vol = vol

    # def __dealloc__(self):
        # PyMem_Free(self.basis)

def wrappaaah():
    c2x.aaah()

def print_cell(unit_cell: UnitCell):
    print(unit_cell.volume)

def c2x_dist(a, b):
    return c2x.dist(a, b)
