# coding: utf-8
#cython: cdivision=True
#cython: boundscheck=False
#cython: nonecheck=False
#cython: wraparound=False

cimport numpy as cnp
import numpy as np
from libc.math cimport ceil


def polygon_mask(y, x, shape, asmask=False):  # TODO shape=None
    """Returns the mask or included points depending on asmask"""
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

    if asmask:
        return np.asarray(mask)
    else:
        return np.asarray(mask).nonzero()


def polygon(y, x, shape):
    """Returns included points, using a buffer the size of a line"""
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

                is_inside = current ^ is_inside

    return rr, cc


def polygon_sort(y, x, shape):
    """Returns included points, using sort of intersection points"""
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
    cdef int start_col, end_col

    # output coordinate arrays
    cdef list rr = list()
    cdef list cc = list()
    cdef list intersections
    #cdef long[:] sorted_intersections

    for row in range(minr, maxr+1):
        # Adapted from http://alienryderflex.com/polygon_fill/

        intersections = list()

        pt1row = contiguous_rdata[nr_verts-1]
        pt1col = contiguous_cdata[nr_verts-1]
        col_min = width - 1
        col_max = 0
        is_inside = 0

        for index in range(nr_verts):
            pt2row = contiguous_rdata[index]
            pt2col = contiguous_cdata[index]

            if ((pt1row <= row < pt2row) or (pt2row <= row < pt1row)):
                # Intersection casted to int so that ]x, x+1] => x
                xinters = (<int>ceil(pt1col + (row - pt1row) *
                           (pt2col - pt1col) / (pt2row - pt1row)))

                intersections.append(xinters)

            pt1row = pt2row
            pt1col = pt2col


        # Sort
        intersections.sort()

        # Fill pixels between pairs
        for index in range(0, len(intersections), 2):
            start_point = intersections[index]
            end_point = intersections[index + 1]

            if end_point <= 0:
                continue
            if start_point > maxc:
                break

            if start_point < 0:
                start_point = 0
            if end_point > maxc:
                end_point = maxc + 1

            if start_point == end_point:
                continue
            #    #end_point += 1

            rr.extend([row] * (end_point - start_point))
            cc.extend(range(start_point, end_point))

    return rr, cc


def _pairs(iterable):
    "s -> (s0,s1), (s2,s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)

def polygon_scanline(image, yp, xp):
    """Draw polygon onto image using a scanline algorithm.

    Attributes
    ----------
    yp, xp : double array
    Coordinates of polygon.

    References
    ----------
    .. [1] "Intersection point of two lines in 2 dimensions",
    http://paulbourke.net/geometry/pointlineplane/
    .. [2] UC Davis ECS175 (Introduction to Computer Graphics) notes,
    http://www.cs.ucdavis.edu/~ma/ECS175_S00/Notes/0411_b.pdf
    """
    yp = list(yp)
    xp = list(xp)

    y_start, y_end = np.min(yp), np.max(yp)
    if not ((yp[0] == yp[-1]) and (xp[0] == xp[-1])):
        yp.append(yp[0])
        xp.append(xp[0])

    ys = zip(yp[:-1], yp[1:])
    xs = zip(xp[:-1], xp[1:])

    h, w = image.shape[:2]

    segments = zip(xs, ys)

    for y in range(max(0, y_start), min(h, y_end)):
        intersections = []

        for ((x0, x1), (y0, y1)) in segments:
            if y0 == y1:
                continue

            xmin = min(x0, x1)
            xmax = max(x0, x1)
            ymin = min(y0, y1)
            ymax = max(y0, y1)

            if not (ymin <= y <= ymax):
                continue

            xi = ((x1 - x0) * (y - y0) - (y1 - y0) * (-x0)) / (y1 - y0)

            if (xmin <= xi <= xmax):
                if (y == y0 or y == y1) and (y != ymin):
                    continue
                intersections.append(xi)

        intersections = np.sort(intersections)

        for x0, x1 in _pairs(intersections):
            image[y, max(0, np.ceil(x0)):min(np.ceil(x1), w)] = 1

    return image
