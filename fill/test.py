# coding: utf-8

import time
import numpy as np
import matplotlib.pyplot as plt

from skimage.draw import polygon as skimg_polygon

from polygon import polygon_mask, polygon, polygon_sort

# Test data

nb_vertices = 1000
# shape = 2048, 2048
shape = 4096, 4096
print("Nb vertices: %d, image shape: %d, %d" % (nb_vertices, shape[0], shape[1]))

row = np.random.randint(-int(shape[0] / 10), int(1.1 * shape[0]), nb_vertices).astype(
    np.float32
)
col = np.random.randint(-int(shape[0] / 10), int(1.1 * shape[1]), nb_vertices).astype(
    np.float32
)
# row = np.array([10, 10, 12, 12], dtype='float32')
# col = np.array([2047, 2050, 2050, 2047], dtype='float32')

st = time.time()
skimg_row, skimg_col = skimg_polygon(row, col, shape)
dt = time.time() - st
print("skimage: %f s" % dt)
# print(skimg_row, skimg_col)

st = time.time()
result = polygon(row, col, shape)
dt = time.time() - st
assert np.all(np.equal(skimg_row, result[0]))
assert np.all(np.equal(skimg_col, result[1]))
print("using line buffer: %f s" % dt)

st = time.time()
result = polygon_mask(row, col, shape, asmask=False)
dt = time.time() - st
assert np.all(np.equal(skimg_row, result[0]))
assert np.all(np.equal(skimg_col, result[1]))
print("using mask buffer: %f s" % dt)

st = time.time()
result = polygon_sort(row, col, shape)
dt = time.time() - st
print("using sort: %f s" % dt)
# print(result)
assert np.all(np.equal(skimg_row, result[0]))
assert np.all(np.equal(skimg_col, result[1]))

st = time.time()
mask = polygon_mask(row, col, shape, asmask=True)
dt = time.time() - st
result = mask.nonzero()
assert np.all(np.equal(skimg_row, result[0]))
assert np.all(np.equal(skimg_col, result[1]))
print("returning mask: %f s" % dt)


# skimage PR931


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

            if xmin <= xi <= xmax:
                if (y == y0 or y == y1) and (y != ymin):
                    continue
                intersections.append(xi)

        intersections = np.sort(intersections)

        for x0, x1 in _pairs(intersections):
            image[y, max(0, np.ceil(x0)) : min(np.ceil(x1), w)] = 1

    return image


mask = np.empty(shape, dtype=np.bool)
st = time.time()
mask = polygon_scanline(mask, row, col)
dt = time.time() - st
result = mask.nonzero()
if (
    len(result[0]) == len(skimg_row)
    and np.all(np.equal(skimg_row, result[0]))
    and np.all(np.equal(skimg_col, result[1]))
):
    print("Same")
else:
    print("Different")
print("skimage PR931: %f s" % dt)


# Plot mask

mask = np.zeros(shape, dtype=np.bool_)
if len(skimg_row):
    mask[skimg_row, skimg_col] = True

plt.imshow(mask)
plt.show()
