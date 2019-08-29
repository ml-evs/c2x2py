# cython: language_level=3

from . cimport c2x

cdef class UnitCell:

    cdef c2x.unit_cell* _unit_cell

    # def __cinit__(self, basis):
        # self._unit_cell.basis = basis
        # self._unit_cell.volume = 0

def wrappaaah():
    c2x.aaah()

def print_cell(unit_cell: UnitCell):
    print(unit_cell.basis)
