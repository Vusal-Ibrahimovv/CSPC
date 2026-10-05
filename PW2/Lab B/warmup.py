import numpy as np
from scipy.optimize import newton, minimize

# Part 2A: Easy convex function
def f(x):
    return (x - 3)**2 + 1

def f_prime(x):
    return 2 * (x - 3)

def f_double_prime(x):
    return 2

print("--- Part 2A: Easy Convex Function ---")

# 1. Gradient Descent
x_gd = 0.0
learning_rate = 0.1
for _ in range(100):
    x_gd = x_gd - learning_rate * f_prime(x_gd)
print(f"Gradient Descent result: x = {x_gd:.4f}")

# 2. Newton's Method
x_newton = newton(f_prime, x0=0.0, fprime=f_double_prime)
print(f"Newton's method result: x = {x_newton:.4f}")

# 3. SLSQP
res_slsqp = minimize(f, x0=0.0, method="SLSQP")
print(f"SLSQP result: x = {res_slsqp.x[0]:.4f}")

# Part 2B: Harder landscape
def g(x):
    return x**4 - 3*x**2 + x + 5

def g_prime(x):
    return 4*x**3 - 6*x + 1

def g_double_prime(x):
    return 12*x**2 - 6

print("\n--- Part 2B: Harder Landscape ---")

for x0 in [0.0, 2.0]:
    print(f"\nStarting from x0 = {x0}:")
    x_gd = x0
    for _ in range(200):
        x_gd = x_gd - 0.05 * g_prime(x_gd)
    print(f"  Gradient Descent: x = {x_gd:.4f}")

    x_newt = newton(g_prime, x0=x0, fprime=g_double_prime)
    second_deriv = g_double_prime(x_newt)
    point_type = "Minimum (g'' > 0)" if second_deriv > 0 else "Maximum (g'' < 0)"
    print(f"  Newton's Method:  x = {x_newt:.4f} -> {point_type}")

    res = minimize(g, x0=x0, method="SLSQP")
    print(f"  SLSQP:            x = {res.x[0]:.4f}")