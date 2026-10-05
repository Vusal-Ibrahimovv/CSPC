import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 50.0  # Equilibrium constant

# Polynomial form: (2x)^2 - K * (1-x)^2 = 0 (avoids division by zero)
def k_imbalance_poly(x):
    return (2 * x)**2 - K * (1 - x)**2

def k_imbalance_poly_prime(x):
    return 8 * x + 2 * K * (1 - x)

# Standard rational form for SLSQP objective function
def k_imbalance(x):
    return ((2 * x)**2) / ((1 - x)**2) - K

# 1. Newton's root finding on polynomial form
x_newton = newton(k_imbalance_poly, x0=0.5, fprime=k_imbalance_poly_prime)

# 2. SLSQP minimization of squared imbalance
res_slsqp = minimize(lambda x: k_imbalance(x[0])**2, x0=[0.5], method="SLSQP", bounds=[(0.01, 0.99)])
x_slsqp = res_slsqp.x[0]

print(f"Equilibrium extent x (Newton): {x_newton:.4f}")
print(f"Equilibrium extent x (SLSQP):  {x_slsqp:.4f}")

nH2_eq = 1 - x_newton
nI2_eq = 1 - x_newton
nHI_eq = 2 * x_newton

print(f"Equilibrium composition: H2 = {nH2_eq:.2f} mol, I2 = {nI2_eq:.2f} mol, HI = {nHI_eq:.2f} mol")

# Plot reaction progress
x_vals = np.linspace(0, 0.99, 100)
plt.figure(figsize=(7, 5))
plt.plot(x_vals, 1 - x_vals, label="H2 / I2 (Reactants)")
plt.plot(x_vals, 2 * x_vals, label="HI (Product)")
plt.axvline(x_newton, color="black", linestyle="--", label=f"Equilibrium x ≈ {x_newton:.2f}")
plt.xlabel("Extent of reaction (x)")
plt.ylabel("Amount (moles)")
plt.title("Chemical Equilibrium Progress")
plt.legend()
plt.grid(True)
plt.savefig("equilibrium.png")
print("Saved equilibrium.png successfully!")