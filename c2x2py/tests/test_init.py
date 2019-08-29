import unittest
import sys
import contextlib
import io

class testInit(unittest.TestCase):
    def test_import(self):
        try:
            import c2x2py.api
        except ImportError:
            sys.path.append(__file__.split('/')[:-1] + '/..')
            import c2x2py.api

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            c2x2py.api.wrappaaah()
        self.assertEqual(f.getvalue(), 'aaah\n')

    def test_print_unit_cell(self):
        try:
            import c2x2py.api
        except ImportError:
            sys.path.append(__file__.split('/')[:-1] + '/..')
            import c2x2py.api

        cell = c2x2py.api.UnitCell()
        c2x2py.api.print_cell(cell)
