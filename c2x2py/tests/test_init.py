#!/usr/bin/env python

import unittest
import sys
import contextlib
import io

class testInit(unittest.TestCase):
    def test_import(self):
        import c2x2py.api
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            c2x2py.api.wrappaaah()
        self.assertEqual(f.getvalue(), 'aaah\n')

    def test_print_unit_cell(self):
        import c2x2py.api
        print('setting up cell')
        cell = c2x2py.api.UnitCell([[10, 0, 0], [0, 10, 0], [0, 0, 10]])
        cell.volume = 10
        print('set up cell')
        c2x2py.api.print_cell(cell)

    def test_dist(self):
        import c2x2py.api

        a = 0.5
        b = 0.6
        self.assertEqual(c2x2py.api.c2x_dist(a, b), b - a)
        a = 1.1
        b = 0.1
        self.assertEqual(c2x2py.api.c2x_dist(a, b), 0)
        a = -0.1
        b = 0.1
        self.assertEqual(c2x2py.api.c2x_dist(a, b), 0.2)

    def test_wrapper_python(self):
        from c2x2py.some_python import UnitCells
        blah = UnitCells(20)
        self.assertEqual(len(blah.cells), 20)
        self.assertTrue(all(cell.volume == 0 for cell in blah.cells))
        blah.cells[5].volume = 20
        self.assertEqual(blah.cells[5].volume, 20)

if __name__ == '__main__':
    unittest.main()
