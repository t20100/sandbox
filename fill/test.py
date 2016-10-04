# coding: utf-8

import time
import numpy as np
import matplotlib.pyplot as plt

from skimage.draw import polygon as sk_polygon

from shapes import polygon, polygon2

# Test data

nb_vertices = 10
shape = 1024, 2048

#y = np.random.randint(0, shape[0], nb_vertices).astype(np.float32)
#x = np.random.randint(0, shape[1], nb_vertices).astype(np.float32)

y = np.array([ 199.,  192.,  130.,  518.,  566.,  169.,  335.,   75.,  310.,  573., 0., 1024., 0., 1024.], dtype=np.float32)
x = np.array([ 1686.,  1685.,  1071.,  1208.,  1558.,   734.,  1922.,   977., 1890.,  1003., 0., 2048., 2048., 0.], dtype=np.float32)

# Polygon fill

st = time.time()
new_y, new_x = polygon(y, x, shape)  # New with full mask
new_dt = time.time() - st

st = time.time()
alt_y, alt_x = polygon2(y, x, shape)  # Alternative
alt_dt = time.time() - st

st = time.time()
sk_y, sk_x = sk_polygon(y, x, shape)  # skimage
sk_dt = time.time() - st

# Check

if (len(sk_x) == len(new_x) and len(sk_x) == len(alt_x) and
        np.all(np.equal(sk_x, new_x)) and np.all(np.equal(sk_y, new_y)) and
        np.all(np.equal(sk_x, alt_x)) and np.all(np.equal(sk_y, alt_y))):
    print('Same')
else:
    print('Error')
print('Time (s): new: %f; alt: %f; skimage: %f' % (new_dt, alt_dt, sk_dt))

# Plot mask

mask = np.zeros(shape, dtype=np.bool_)
if len(new_y):
    mask[new_y, new_x] = True

plt.imshow(mask)
plt.show()
