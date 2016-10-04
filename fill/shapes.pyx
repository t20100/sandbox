# coding: utf-8
#cython: cdivision=True
#cython: boundscheck=False
#cython: nonecheck=False
#cython: wraparound=False

from libcpp.vector cimport vector
cimport numpy as cnp
import numpy as np
from libc.math cimport ceil


def polygon(y, x, shape):  # TODO shape=None
    cdef float[:] c_x = np.ascontiguousarray(x)
    cdef float[:] c_y = np.ascontiguousarray(y)
    cdef Py_ssize_t nr_verts = c_x.shape[0]

    cdef int height, width

    height, width = shape

    cdef unsigned char[:, :] mask = np.zeros((height, width),
                                                dtype=np.uint8)
    cdef int row_min, row_max, col_min, col_max  # mask subpart to update
    cdef int row, col, index  # Loop indixes
    cdef float pt1x, pt1y, pt2x, pt2y  # segment end points
    cdef int xinters, is_inside, current

    row_min = max(int(min(c_y)), 0)
    row_max = min(int(max(c_y)) + 1, height)

    # Can be replaced by prange(row_min, row_max, nogil=True)
    with nogil:
        for row in range(row_min, row_max):
            # For each line of the image, mark intersection of all segments
            # in the line and then run a xor scan to fill inner parts
            # Adapted from http://alienryderflex.com/polygon_fill/
            pt1x = c_x[nr_verts-1]
            pt1y = c_y[nr_verts-1]
            col_min = width - 1
            col_max = 0
            is_inside = 0  # Init with whether first col is inside or not

            for index in range(nr_verts):
                pt2x = c_x[index]
                pt2y = c_y[index]

                if ((pt1y <= row and row < pt2y) or
                        (pt2y <= row and row < pt1y)):
                    # Intersection casted to int so that ]x, x+1] => x
                    xinters = (<int>ceil(pt1x + (row - pt1y) *
                               (pt2x - pt1x) / (pt2y - pt1y))) - 1

                    # Update column range to patch
                    if xinters < col_min:
                        col_min = xinters
                    if xinters > col_max:
                        col_max = xinters

                    if xinters < 0:
                        # Add an intersection to init value of xor scan
                        is_inside ^= 1
                    elif xinters < width:
                        # Mark intersection in mask
                        mask[row, xinters] ^= 1
                    # else: do not consider intersection on the right

                pt1x, pt1y = pt2x, pt2y

            if col_min < col_max:
                # Clip column range to mask
                if col_min < 0:
                    col_min = 0
                if col_max > width - 1:
                    col_max = width - 1

                # xor exclusive scan
                for col in range(col_min, col_max + 1):
                    current = mask[row, col]
                    mask[row, col] = is_inside
                    is_inside = current ^ is_inside

    return np.asarray(mask).nonzero()


cdef class VectorInt:
    cdef:
        cnp.intp_t[:] data
        cnp.intp_t size, allocated
    
    def __cinit__(self, data=None, int min_size=10):

        if data:
            self.data = np.ascontiguousarray(data)
            self.allocated = self.size = self.data.size
        else:
            self.allocated = min_size
            self.data = np.empty(self.allocated, dtype=np.intp)
            self.size = 0
    
    def __dealloc__(self):
        self.data = None
    
    def __len__(self):
        return self.size
        
    def get_data(self):
        return np.asarray(self.data[:self.size])
    
    def append(self, cnp.intp_t value):
        if self.size >= self.allocated - 1:
            new_allocated = self.allocated * 2
            newdata = np.empty(new_allocated, dtype=np.intp)
            newdata[:self.size] = self.data[:self.size]
            self.data = newdata
            self.allocated = new_allocated
        self.data[self.size] = value
        self.size += 1


def polygon2(y, x, shape):
    x = np.asanyarray(x)
    y = np.asanyarray(y)

    cdef Py_ssize_t nr_verts = x.shape[0]
    cdef Py_ssize_t minr = int(max(0, y.min()))
    cdef Py_ssize_t maxr = int(ceil(y.max()))
    cdef Py_ssize_t minc = int(max(0, x.min()))
    cdef Py_ssize_t maxc = int(ceil(x.max()))

    # make sure output coordinates do not exceed image size
    if shape is not None:
        maxr = min(shape[0] - 1, maxr)
        maxc = min(shape[1] - 1, maxc)

    cdef Py_ssize_t width
    width = maxc + 1 # TODO remove minc, maxc

    cdef Py_ssize_t r, c

    # make contigous arrays for r, c coordinates
    cdef double[:] contiguous_rdata, contiguous_cdata
    contiguous_rdata = np.ascontiguousarray(y, dtype=np.double)
    contiguous_cdata = np.ascontiguousarray(x, dtype=np.double)

    cdef int col_min, col_max
    cdef int index
    cdef cnp.intp_t row, col
    cdef double pt1row, pt1col, pt2row, pt2col  # segment end points
    cdef int xinters, is_inside, current

    # TODO remove the mask and directly fill rr, cc
    cdef unsigned char[:] line = np.zeros((maxc,), dtype=np.uint8)
    # output coordinate arrays
    cdef list rr = list()
    cdef list cc = list()
    #cdef VectorInt rr = VectorInt()
    #cdef VectorInt cc = VectorInt()
    #cdef vector[cnp.intp_t] rr
    #cdef vector[cnp.intp_t] cc

    for row in range(minr, maxr+1):
        # For each line of the image, mark intersection of all segments
        # in the line and then run a xor scan to fill inner parts
        # Adapted from http://alienryderflex.com/polygon_fill/

        pt1row = contiguous_rdata[nr_verts-1]
        pt1col = contiguous_cdata[nr_verts-1]
        col_min = width - 1
        col_max = 0
        is_inside = 0

        line[:] = 0

        for index in range(nr_verts):
            pt2row = contiguous_rdata[index]
            pt2col = contiguous_cdata[index]

            if ((pt1row <= row and row < pt2row) or
                    (pt2row <= row and row < pt1row)):
                # Intersection casted to int so that ]x, x+1] => x
                xinters = (<int>ceil(pt1col + (row - pt1row) *
                           (pt2col - pt1col) / (pt2row - pt1row))) - 1

                # Update column range to patch
                if xinters < col_min:
                    col_min = xinters
                if xinters > col_max:
                    col_max = xinters

                if xinters < 0:
                    # Add an intersection to init value of xor scan
                    is_inside ^= 1
                elif xinters < width:
                    # Mark intersection in mask
                    line[xinters] ^= 1
                # else: do not consider intersection on the right

            pt1row = pt2row
            pt1col = pt2col

        if col_min < col_max:
            # Clip column range to mask
            if col_min < 0:
                col_min = 0
            if col_max > width - 1:
                col_max = width - 1

            # xor exclusive scan
            for col in range(col_min, col_max + 1):
                current = line[col]
                line[col] = is_inside
                if is_inside:
                    rr.append(row)
                    cc.append(col)
                    #rr.push_back(row)
                    #cc.push_back(col)

                is_inside = current ^ is_inside

    return rr, cc
    #return np.array(rr, dtype=np.intp), np.array(cc, dtype=np.intp)
    #return rr.get_data(), cc.get_data()
