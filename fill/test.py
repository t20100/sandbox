# coding: utf-8

import time
import numpy as np
import matplotlib.pyplot as plt

from skimage.draw import polygon as sk_polygon

from polygon import polygon_mask, polygon, polygon2

# Test data

#nb_vertices = 10
#shape = 1024, 2048
nb_vertices = 100
shape = 4000, 4000

row = np.random.randint(0, shape[0], nb_vertices).astype(np.float32)
col = np.random.randint(0, shape[1], nb_vertices).astype(np.float32)

#row = np.array([ 199.,  192.,  130.,  518.,  566.,  169.,  335.,   75.,  310.,  573., 0., 1024., 0., 1024.], dtype=np.float32)
#col = np.array([ 1686.,  1685.,  1071.,  1208.,  1558.,   734.,  1922.,   977., 1890.,  1003., 0., 2048., 2048., 0.], dtype=np.float32)

# Polygon fill

st = time.time()
buffer_row, buffer_col = polygon(row, col, shape)  # With full mask
buffer_dt = time.time() - st

st = time.time()
line_row, line_col = polygon2(row, col, shape)  # Alternative
line_dt = time.time() - st

st = time.time()
sk_row, sk_col = sk_polygon(row, col, shape)  # skimage
sk_dt = time.time() - st

# Check

if (len(sk_col) == len(buffer_col) and
        np.all(np.equal(sk_row, buffer_row)) and
        np.all(np.equal(sk_col, buffer_col)) and
        len(sk_col) == len(line_col) and
        np.all(np.equal(sk_row, line_row)) and
        np.all(np.equal(sk_col, line_col))):
    print('Same')
else:
    print('Error')
print('Time (s): buffer: %f; line: %f; skimage: %f' %
      (buffer_dt, line_dt, sk_dt))

# Plot mask

mask = np.zeros(shape, dtype=np.bool_)
if len(buffer_row):
    mask[buffer_row, buffer_col] = True

plt.imshow(mask)
plt.show()
