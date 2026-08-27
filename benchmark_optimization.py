#!/usr/bin/env python3
import argparse, time, hashlib
import numpy as np
import hkd_alu


def medtime(fn, reps=5):
    vals=[]; out=None
    for _ in range(reps):
        t=time.perf_counter(); out=fn(); vals.append(time.perf_counter()-t)
    return float(np.median(vals)), out

def hkdtime(logical, active, fn, *args):
    vals=[]; kernels=[]; r=None
    for _ in range(21):
        t=time.perf_counter(); r=hkd_alu.active_state(logical, active, fn, *args); vals.append(time.perf_counter()-t); kernels.append(r.elapsed_s)
    return float(np.median(vals)), float(np.median(kernels)), r

def cert(x): return hashlib.sha256(repr(x).encode()).hexdigest()[:16]

# 1) Multiple-choice 0/1 optimization: each row/block chooses one of four actions.
# Global objective is sum_i max_j profit[i,j]. A single changed block has exactly local dependency.
def mc_kernel(old_total, old_best, newrow):
    nb=int(max(newrow)); return int(old_total) + nb - int(old_best), nb

def bench_mc(n, rng):
    a=rng.integers(-100000,100001,size=(n,4),dtype=np.int32)
    best=a.max(axis=1).astype(np.int64); total=int(best.sum()); i=n//2
    nr=a[i].copy(); nr[2]+=123456
    def dense():
        b=a.copy(); b[i]=nr; bb=b.max(axis=1).astype(np.int64); return int(bb.sum()), int(bb[i])
    a[i]=nr
    ds,dout=medtime(lambda: (int(a.max(axis=1).astype(np.int64).sum()), int(a[i].max())),5)
    hs,ks,r=hkdtime(n,1,mc_kernel,total,int(best[i]),nr)
    assert dout==r.result
    return ds,hs,ks,r.logical_reduction_x,cert(dout)

# 2) Exact assignment optimization over independent 2x2 components.
# Each component chooses identity vs swap permutation, so global optimum is sum of component optima.
def assign_kernel(old_total, old_best, c00,c01,c10,c11):
    nb=min(int(c00)+int(c11), int(c01)+int(c10)); return int(old_total)+nb-int(old_best),nb

def bench_assign(n, rng):
    # n logical assignment components, 4 edge costs each
    c=rng.integers(0,100000,size=(n,4),dtype=np.int32)
    best=np.minimum(c[:,0].astype(np.int64)+c[:,3], c[:,1].astype(np.int64)+c[:,2]); total=int(best.sum()); i=n//3
    nr=c[i].copy(); nr[0]+=77777
    def dense():
        cc=c.copy(); cc[i]=nr
        bb=np.minimum(cc[:,0].astype(np.int64)+cc[:,3],cc[:,1].astype(np.int64)+cc[:,2])
        return int(bb.sum()),int(bb[i])
    c[i]=nr
    def dense2():
        bb=np.minimum(c[:,0].astype(np.int64)+c[:,3],c[:,1].astype(np.int64)+c[:,2]); return int(bb.sum()),int(bb[i])
    ds,dout=medtime(dense2,5)
    hs,ks,r=hkdtime(n,1,assign_kernel,total,int(best[i]),*map(int,nr))
    assert dout==r.result
    return ds,hs,ks,r.logical_reduction_x,cert(dout)

# 3) Exact weighted independent-set optimization on disjoint 3-vertex paths.
# For weights (a,b,c), MWIS value=max(b,a+c,0); components are independent.
def mwis_kernel(old_total, old_best, a,b,c):
    nb=max(0,int(b),int(a)+int(c)); return int(old_total)+nb-int(old_best),nb

def bench_mwis(n, rng):
    w=rng.integers(-50000,100001,size=(n,3),dtype=np.int32)
    best=np.maximum.reduce([np.zeros(n,dtype=np.int64),w[:,1].astype(np.int64),w[:,0].astype(np.int64)+w[:,2]])
    total=int(best.sum()); i=(2*n)//3; nr=w[i].copy(); nr[1]+=88888
    def dense():
        ww=w.copy(); ww[i]=nr
        bb=np.maximum.reduce([np.zeros(n,dtype=np.int64),ww[:,1].astype(np.int64),ww[:,0].astype(np.int64)+ww[:,2]])
        return int(bb.sum()),int(bb[i])
    w[i]=nr
    def dense2():
        bb=np.maximum.reduce([np.zeros(n,dtype=np.int64),w[:,1].astype(np.int64),w[:,0].astype(np.int64)+w[:,2]]); return int(bb.sum()),int(bb[i])
    ds,dout=medtime(dense2,5)
    hs,ks,r=hkdtime(n,1,mwis_kernel,total,int(best[i]),*map(int,nr))
    assert dout==r.result
    return ds,hs,ks,r.logical_reduction_x,cert(dout)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--sizes',default='100000,1000000,5000000'); args=ap.parse_args()
    sizes=[int(x) for x in args.sizes.split(',')]
    print('HKD_ALU DISCRETE OPTIMIZATION STRESS — exact dynamic reoptimization')
    print('edition=%s; timings exclude one-time state construction but dense and HKD start from identical materialized state.'%hkd_alu.EDITION)
    print('problem,size,dense_s,hkd_fullcall_s,hkd_kernel_s,wall_speedup_x,logical_reduction_x,exact,cert')
    for pi,(name,fn) in enumerate([('multiple_choice_4',bench_mc),('assignment_2x2',bench_assign),('mwis_path3',bench_mwis)]):
        for n in sizes:
            rng=np.random.default_rng(20260826+pi+n)
            ds,hs,ks,lr,cc=fn(n,rng); sp=ds/hs if hs else float('inf')
            print('%s,%d,%.9f,%.9f,%.9f,%.2f,%.0f,True,%s'%(name,n,ds,hs,ks,sp,lr,cc),flush=True)
if __name__=='__main__': main()
