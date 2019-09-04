# cython: language_level=3

cimport c2x

cdef class UnitCell:

    cdef c2x.unit_cell _unit_cell

    def __init__(self, volume=0):
        self._unit_cell.vol = volume
        print('Created unit cell with {} volume'.format(self._unit_cell.vol))

    @property
    def volume(self):
        return self._unit_cell.vol

    @volume.setter
    def volume(self, vol: float):
        self._unit_cell.vol = vol

def wrappaaah():
    c2x.aaah()

def print_cell(unit_cell: UnitCell):
    print(unit_cell.volume)

def c2x_dist(a, b):
    return c2x.dist(a, b)
