# hkd_alu
HKD ALU is a lightweight execution layer for replacing large repeated state transitions with exact active-state transitions. On the included free benchmark, a workload with **1,000,000 logical rows and 1 active row** performs **1 row transition instead of 1,000,000**, producing an exact **1,000,000× structural work reduction**.
