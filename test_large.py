#!/usr/bin/env python3
from __future__ import print_function

import hashlib
import time

import numpy as np

import hkd_alu

# One logical row beyond the free ceiling.
# This check happens BEFORE any large allocation or benchmark work.
ROWS = 1000001
DIM = 8


def _paid_gate_probe():
    def no_op():
        return "HKD_ALU_PAID_GATE_PASS"

    # FREE must raise UPGRADE_MESSAGE here immediately.
    # PAID continues.
    return hkd_alu.active_state(
        ROWS,
        1,
        no_op
    )


_paid_gate_probe()


def show(name, dense_s, result):
    print("")
    print(name)
    print("-" * 76)
    print(
        "logical baseline     = {:,} row transitions".format(
            result.logical_rows
        )
    )
    print(
        "HKD active state     = {:,} row transition".format(
            result.active_rows
        )
    )
    print(
        "logical reduction    = {:,.0f}x".format(
            result.logical_reduction_x
        )
    )
    print("dense/reference      = {:.9f} sec".format(dense_s))
    print("HKD transition       = {:.9f} sec".format(result.elapsed_s))

    if result.elapsed_s > 0.0:
        print(
            "measured speedup     = {:,.2f}x".format(
                dense_s / result.elapsed_s
            )
        )

    print("exact equality       = True")
    print("hidden result cert   = {}".format(result.certificate))


print("=" * 76)
print("HKD ALU PAID LARGE BENCHMARK")
print("=" * 76)
print("paid gate            = PASS")
print("logical rows         = {:,}".format(ROWS))


# ---------------------------------------------------------------------------
# 1) LLM SPARSE OPTIMIZER
# One active embedding/optimizer row among 1,000,001 logical rows.
# ---------------------------------------------------------------------------

p = np.zeros((ROWS, DIM), dtype=np.float32)
m = np.zeros_like(p)
v = np.zeros_like(p)
g = np.zeros_like(p)

idx = 543210

g[idx] = np.array(
    [0.1, -0.2, 0.3, -0.4, 0.5, -0.6, 0.7, -0.8],
    dtype=np.float32
)

t0 = time.time()

dm = 0.9 * m + 0.1 * g
dv = 0.999 * v + 0.001 * (g * g)
mh = dm / 0.1
vh = dv / 0.001

dense_p = p - 0.001 * mh / (np.sqrt(vh) + 1e-8)

dense_s = time.time() - t0

res = hkd_alu.active_state(
    ROWS,
    1,
    hkd_alu.sparse_adam_row,
    p[idx],
    m[idx],
    v[idx],
    g[idx]
)

assert np.array_equal(dense_p[idx], res.result[0])

show(
    "1) LLM SPARSE OPTIMIZER",
    dense_s,
    res
)

del p
del m
del v
del g
del dm
del dv
del mh
del vh
del dense_p


# ---------------------------------------------------------------------------
# 2) EXACT PORTFOLIO REPRICING
# One changed quote among 1,000,001 positions.
# ---------------------------------------------------------------------------

rng = np.random.RandomState(20260826)

qty = rng.randint(
    -500,
    501,
    size=ROWS
).astype(np.int64)

entry = rng.randint(
    1000,
    50000,
    size=ROWS
).astype(np.int64)

marks = rng.randint(
    1000,
    50000,
    size=ROWS
).astype(np.int64)

fees = rng.randint(
    0,
    50,
    size=ROWS
).astype(np.int64)

old_pnl = qty * (marks - entry) - fees
old_total = int(old_pnl.sum())

idx = 333333
new_mark = int(marks[idx] + 137)

t0 = time.time()

new_marks = marks.copy()
new_marks[idx] = new_mark
dense_pnl = qty * (new_marks - entry) - fees
dense_total = int(dense_pnl.sum())

dense_s = time.time() - t0

res = hkd_alu.active_state(
    ROWS,
    1,
    hkd_alu.portfolio_reprice_one,
    int(qty[idx]),
    int(entry[idx]),
    int(marks[idx]),
    new_mark,
    old_total,
    int(old_pnl[idx]),
    int(fees[idx])
)

assert res.result[1] == dense_total

show(
    "2) EXACT PORTFOLIO REPRICING",
    dense_s,
    res
)

del qty
del entry
del marks
del fees
del old_pnl
del new_marks
del dense_pnl


# ---------------------------------------------------------------------------
# 3) OPPORTUNITY SCORING ENGINE
# One changed candidate among 1,000,001 opportunities.
# ---------------------------------------------------------------------------

rng = np.random.RandomState(20260827)

revenue = rng.randint(
    0,
    10000000,
    size=ROWS
).astype(np.int64)

cost = rng.randint(
    0,
    3000000,
    size=ROWS
).astype(np.int64)

risk = rng.randint(
    0,
    2000000,
    size=ROWS
).astype(np.int64)

scores = revenue - cost - risk

idx = 142857
new_revenue = int(revenue[idx] + 5000003)

t0 = time.time()

dense_scores = revenue.copy()
dense_scores[idx] = new_revenue
dense_scores = dense_scores - cost - risk
changed_score = int(dense_scores[idx])

dense_s = time.time() - t0

res = hkd_alu.active_state(
    ROWS,
    1,
    hkd_alu.opportunity_update_one,
    int(scores[idx]),
    new_revenue,
    int(cost[idx]),
    int(risk[idx])
)

assert res.result == changed_score

show(
    "3) OPPORTUNITY SCORING ENGINE",
    dense_s,
    res
)

print("")
print("=" * 76)
print("ALL THREE EXACT: PASS")
print(
    "NOTE: {:,.0f}x is structural row-transition reduction.".format(
        float(ROWS)
    )
)
print(
    "Wall-clock speedup is measured separately and is machine dependent."
)
print("=" * 76)
