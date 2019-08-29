# cython: language_level=3

cdef extern from "../../c2xsf.h":

    struct unit_cell:
        cdef double basis[3]
        cdef double recip[3]
        cdef double volume

cdef inline void aaah():
    print("aaah")
