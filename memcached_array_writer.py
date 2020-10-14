# coding: utf-8
# /*##########################################################################
# Copyright (C) 2020 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ############################################################################*/
"""Script filling memcached with a 3D stack chunk by chunk

memcached --listen=127.0.0.1 --memory-limit=65000 --max-item-size=17m --slab-min-size=16m
"""

import json
import io
import itertools
import math

import h5py
import numpy
import bloscpack
from pymemcache.client.base import Client
import silx.io


class NumpySerde(object):
    """Numpy array serializer"""

    def serialize(key, value):
        if isinstance(value, numpy.ndarray):
            with io.BytesIO() as buffer:
                numpy.save(buffer, value)
                return buffer.getvalue(), 2
        else:
            return value, 1

    def deserialize(key, value, flags):
        if flags == 1:
            return value
        elif flags == 2:
            with io.BytesIO(value) as buffer:
                return numpy.load(buffer)
        else:
            raise RuntimeException("Unsupported serialization flags")


class NumpyBloscpackSerde(object):
    """Numpy array serializer"""

    def serialize(key, value):
        if isinstance(value, numpy.ndarray):
            with io.BytesIO() as buffer:
                numpy.save(buffer, value)
                return buffer.getvalue(), 2
        else:
            return value, 1

    def deserialize(key, value, flags):
        if flags == 1:
            return value
        elif flags == 2:
            with io.BytesIO(value) as buffer:
                return numpy.load(buffer)
        else:
            raise RuntimeException("Unsupported serialization flags")


def slice_sender(client, dset):
    """Send slice from dataset to client

    :param Client client:
    :param dset: Array-like of data
    """
    ndigits = math.floor(math.log10(len(dset))) + 1
    template = "slice%%0%dd" % ndigits
    for index, slice_ in enumerate(dset):
        key = template % index
        client.set(key, slice_)
        yield key


def _flatten_slices(slices):
    """Returns a flattened tuple of slices start and stop

    :param List[slice] slices:
    """
    result = []
    for s in slices:
        result.append(s.start)
        result.append(s.stop)
    return tuple(result)


def chunk_sender(client, dset, uid="data", chunks=None):
    """Send chunks from dataset to client

    :param Client client:
    :param dset: Array-like of data (with slicing and a shape attribute)
    :param str uid: Unique ID of the dataset
    :param Union[List[int],None] chunks:
        List of size of the chunk in each dimension.
        As many dimension as the dataset.
        If None, a single chunk is used.
    """
    template = uid + "[" + ",".join(["%d:%d"] * len(dset.shape)) + "]"

    if chunks is None:
        chunks = dset.shape

    # Write header
    client.set(
        uid,
        json.dumps(
            {
                "version": 1,
                "shape": dset.shape,
                "dtype": dset.dtype.str,
                "chunks": chunks,
            }
        ),
    )

    nchunks = numpy.ceil(numpy.array(dset.shape) / numpy.array(chunks)).astype(
        numpy.int
    )
    for index in range(numpy.prod(nchunks)):
        slices = []
        for nchunk_dim, chunk_size, dset_size in zip(
            reversed(nchunks), reversed(chunks), reversed(dset.shape)
        ):
            start = (index % nchunk_dim) * chunk_size
            stop = min(start + chunk_size, dset_size)
            slices.insert(0, slice(start, stop))
            index = index // nchunk_dim

        key = template % tuple(
            itertools.chain.from_iterable((s.start, s.stop) for s in slices)
        )
        client.set(key, dset[tuple(slices)])
        yield key


if __name__ == "__main__":
    import sys

    SERVER = "localhost", 11211

    client = Client(SERVER, serde=NumpySerde)

    url = silx.io.url.DataUrl(sys.argv[1])
    with silx.io.open(url.path()) as dset:
        # for key in slice_sender(client, dset):
        for key in chunk_sender(client, dset, chunks=[1, 512, 512]):
            print("loaded", key)
