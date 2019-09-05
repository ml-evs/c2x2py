""" Dummy module to demonstrate how pure Python code gets
incorporated into the package.

"""

from c2x2py.api import UnitCell


class UnitCells:

    cells = []

    def __init__(self, num_cells):
        for i in range(num_cells):
            self.cells.append(UnitCell())
        print('Made combined object with {} cells'.format(num_cells))
