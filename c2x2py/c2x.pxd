# cython: language_level=3

cdef extern from "c2xsf.h":

    cdef struct unit_cell:
        double vol
        # double basis[3]
        # double recip[3][3]

    ctypedef struct atom
    ctypedef struct grid
    ctypedef struct mp_grid
    ctypedef struct vector
    ctypedef struct sym_op
    ctypedef struct contents
    ctypedef struct kpts
    ctypedef struct symmetry
    ctypedef struct es

    double dist(double a, double b)
    # double fft3d(double *c, int *ngptar, int dir)


cdef inline void aaah():
    print("aaah")
