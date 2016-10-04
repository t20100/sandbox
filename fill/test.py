# coding: utf-8

import time
import numpy as np
import matplotlib.pyplot as plt

from skimage.draw import polygon as skimg_polygon

from polygon import polygon_mask, polygon

# Test data

nb_vertices = 100
shape = 2048, 2048
#shape = 4096, 4096
print('Nb vertices: %d, image shape: %d, %d' %
      (nb_vertices, shape[0], shape[1]))

row = np.random.randint(-int(shape[0]/10), int(1.1 * shape[0]), nb_vertices).astype(np.float32)
col = np.random.randint(-int(shape[0]/10), int(1.1 * shape[1]), nb_vertices).astype(np.float32)


st = time.time()
skimg_row, skimg_col = skimg_polygon(row, col, shape)
dt = time.time() - st
print('skimage: %f s' % dt)

st = time.time()
result = polygon(row, col, shape)
dt = time.time() - st
assert np.all(np.equal(skimg_row, result[0]))
assert np.all(np.equal(skimg_col, result[1]))
print('using line buffer: %f s' % dt)

st = time.time()
result = polygon_mask(row, col, shape, asmask=False)
dt = time.time() - st
assert np.all(np.equal(skimg_row, result[0]))
assert np.all(np.equal(skimg_col, result[1]))
print('using mask buffer: %f s' % dt)

st = time.time()
mask = polygon_mask(row, col, shape, asmask=True)
dt = time.time() - st
result = mask.nonzero()
assert np.all(np.equal(skimg_row, result[0]))
assert np.all(np.equal(skimg_col, result[1]))
print('returning mask: %f s' % dt)


# Plot mask

mask = np.zeros(shape, dtype=np.bool_)
if len(skimg_row):
    mask[skimg_row, skimg_col] = True

plt.imshow(mask)
plt.show()
