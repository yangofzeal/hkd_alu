# HKD ALU — Up to 1,000,000× Logical Python Work Reduction

**Drop-in active-state execution for Python workloads whose outputs depend on a tiny changed subset of a much larger logical state.**

HKD ALU is a lightweight execution layer for replacing large repeated state transitions with exact active-state transitions. On the included free benchmark, a workload with **1,000,000 logical rows and 1 active row** performs **1 row transition instead of 1,000,000**, producing an exact **1,000,000× structural work reduction**.

> Important: this is a logical-work reduction, not a promise that every Python program or every CPU instruction runs 1,000,000× faster. Measured wall-clock speedup depends on the workload, runtime, memory system, and how much work can be eliminated.

## Why it matters

Conventional execution often scales with the total state size even when only a tiny portion changed. HKD ALU instead treats the changed state as the fundamental execution unit.

If a logical state contains `N` rows and only `k` rows changed:

```text
ordinary work  ~ N transitions
HKD ALU work   ~ k transitions

logical reduction = N / k
```

At the free-edition boundary:

```text
N = 1,000,000
k = 1

logical reduction = 1,000,000×
```

That same principle applies naturally to sparse optimizer state, incremental repricing, ranking/index maintenance, persistent caches, delta checkpoints, and other workloads with exact local dependencies.

## Editions

### Free

The free edition supports up to:

```text
1,000,000 logical rows
```

That is deliberately large enough to demonstrate a full **1,000,000× structural reduction** when exactly one row is active.

A workload with:

```text
1,000,001 logical rows
```

requires the paid edition.

The upgrade text is intentionally a normal Python string:

```python
UPGRADE_MESSAGE = (
    "HKD_ALU_FREE_LIMIT: ... "
    "BUY: https://example.com/buy-hkd-alu"
)
```

Edit that string in `free/hkd_alu.py` to point to your own checkout, documentation, or sales page.

### Paid

The paid edition uses the same public API and removes the logical-row cap.

No source-code rewrite is required when switching editions: replace which `hkd_alu.py` is installed/imported.

## Quick start

Run the free benchmark:

```bash
python3 test.py
```

Expected shape:

```text
HKD ALU FREE TEST
logical rows        = 1,000,000
active rows         = 1
logical reduction   = 1,000,000x
...
PASS
```

Then verify the licensing boundary:

```bash
python3 test_large.py
```

Expected shape:

```text
FREE BLOCKED         = YES
FREE MESSAGE         = HKD_ALU_FREE_LIMIT: ...
PAID EXECUTED        = YES
logical rows         = 1,000,001
logical reduction    = 1,000,001x
PASS
```

## API

The central call is:

```python
result = hkd_alu.active_state(
    logical_rows,
    active_rows,
    transition_function,
    *args,
    **kwargs,
)
```

Example:

```python
res = hkd_alu.active_state(
    1_000_000,
    1,
    hkd_alu.sparse_adam_row,
    parameter_row,
    exp_avg_row,
    exp_avg_sq_row,
    gradient_row,
)

print(res.logical_reduction_x)
# 1000000.0
```

The library returns:

- the exact transition result,
- logical rows,
- active rows,
- structural reduction,
- elapsed transition time,
- a short deterministic certificate for result comparison.

## Included semantic kernels

The reference build includes compact examples for:

- sparse Adam-style optimizer updates,
- exact fixed-point portfolio repricing,
- integer opportunity-score updates.

These are examples of the execution model rather than the full set of possible kernels.

## Mechanics

HKD ALU separates two ideas that are often conflated:

1. **How fast is an arithmetic instruction?**
2. **How many logical state transitions are actually necessary?**

Traditional acceleration usually attacks the first question through faster native code, vectorization, JIT compilation, SIMD, or GPUs.

HKD ALU attacks the second.

When the runtime can prove that only a small active subset influences the next state, it executes only that subset and preserves the rest.

This is why the gain can be much larger than an instruction-level optimization on the right workload: eliminated operations do not need to be made faster.

## Theory

Let the complete logical state be:

```text
S = {s0, s1, ..., sN-1}
```

and let a transition from time `t` to `t+1` depend only on an active set `A`:

```text
A ⊂ S
|A| = k
```

If unchanged state remains invariant under the transition, then the exact next state can be represented by updating only `A`.

The structural reduction is:

```text
N / k
```

The included 1,000,000-row benchmark uses:

```text
N = 1,000,000
k = 1
```

which gives:

```text
1,000,000×
```

The implementation intentionally keeps the internal machinery compact. The public contract is the important part: declare the logical state size, identify the active subset, and execute an exact transition over that subset.

## What HKD ALU is not

HKD ALU does **not** claim that arbitrary Python scalar `+`, `-`, `*`, or `/` instructions become physically one million times faster.

A workload must have exploitable structure: sparsity, unchanged state, repeated state, reusable transitions, or another exact dependency reduction.

For workloads where every output genuinely depends on every input every time, the runtime must still perform the necessary work.

## Product positioning

A concise technical description is:

> **HKD ALU is an exact incremental execution layer for Python. It reduces work in proportion to changed state rather than total logical state.**

A concise benchmark description is:

> **1,000,000 logical rows → 1 active transition → 1,000,000× structural work reduction, with exact output verification.**

That framing is both striking and reproducible.

## Files

```text
hkd_alu_product/
├── free/
│   └── hkd_alu.py
├── paid/
│   └── hkd_alu.py
├── test.py
├── test_large.py
└── README.md
```

## License / distribution

Add your own license terms, checkout URL, packaging metadata, and distribution mechanism before publication.

For a commercial release, keep the free and paid public APIs identical so users can upgrade without changing application code.
