#!/usr/bin/env python

import unittest
import sys
import contextlib
import io

def trace(func, *args, **kwargs):
    print('Entering {}'.format(func.__name__))
    results = func(*args, **kwargs)
    print('Exiting {}'.format(func.__name__))
    return results

class testInit(unittest.TestCase):
    def test_import(self):
        try:
            import c2x2py.api
        except (ImportError, ModuleNotFoundError):
            print('/'.join(__file__.split('/')[:-1]) + '/../')
            sys.path.append('/'.join(__file__.split('/')[:-1]) + '/..')
            import c2x2py.api

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            c2x2py.api.wrappaaah()
        self.assertEqual(f.getvalue(), 'aaah\n')

    def test_print_unit_cell(self):
        try:
            import c2x2py.api
        except (ImportError, ModuleNotFoundError):
            print('/'.join(__file__.split('/')[:-1]) + '/../')
            sys.path.append('/'.join(__file__.split('/')[:-1]) + '/..')
            import c2x2py.api

        print('setting up cell')
        cell = c2x2py.api.UnitCell(volume=10)
        cell.volume = 10
        print('set up cell')
        c2x2py.api.print_cell(cell)

    def test_dist(self):
        try:
            import c2x2py.api
        except (ImportError, ModuleNotFoundError):
            print('/'.join(__file__.split('/')[:-1]) + '/../')
            sys.path.append('/'.join(__file__.split('/')[:-1]) + '/../')
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

if __name__ == '__main__':
    unittest.main()
