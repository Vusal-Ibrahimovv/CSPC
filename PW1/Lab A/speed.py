import time
from decay import simulate, simulate_loop

N0 = 200000
LAM = 0.4

t0 = time.perf_counter()
simulate_loop(N0, LAM)
t_loop = time.perf_counter() - t0

t0 = time.perf_counter()
simulate(N0, LAM)
t_numpy = time.perf_counter() - t0

print(f"loop  : {t_loop:.4f} s")
print(f"numpy : {t_numpy:.6f} s")
print(f"speed-up: {t_loop / t_numpy:.0f} x faster")