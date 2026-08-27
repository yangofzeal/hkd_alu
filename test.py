#!/usr/bin/env python3
from __future__ import print_function

import numpy as np

import hkd_alu

ROWS = 1000000
DIM = 8

p = np.zeros(DIM, dtype=np.float32)
m = np.zeros(DIM, dtype=np.float32)
v = np.zeros(DIM, dtype=np.float32)
g = np.array(
    [0.1, -0.2, 0.3, -0.4, 0.5, -0.6, 0.7, -0.8],
    dtype=np.float32
)

res = hkd_alu.active_state(
    ROWS,
    1,
    hkd_alu.sparse_adam_row,
    p,
    m,
    v,
    g
)

print("=" * 76)
print("HKD ALU FREE / STANDARD TEST")
print("=" * 76)
print(hkd_alu.about())
print("logical rows        = {:,}".format(res.logical_rows))
print("active rows         = {:,}".format(res.active_rows))
print("logical reduction   = {:,.0f}x".format(res.logical_reduction_x))
print("elapsed             = {:.9f} sec".format(res.elapsed_s))
print("certificate         = {}".format(res.certificate))
print("result              = {}".format(res.result[0]))

assert res.logical_rows == 1000000
assert res.active_rows == 1
assert res.logical_reduction_x == 1000000.0
assert np.isfinite(res.result[0]).all()

print("PASS")
