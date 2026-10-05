import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Read data from kinetics.csv
data = np.loadtxt("kinetics.csv", delimiter=",", skiprows=1)
t = data[:, 0]
C_measured = data[:, 1]
C0 = C_measured[0]

# Define sum of squared errors function
def total_error(k):
    C_model = C0 * np.exp(-k * t)
    return np.sum((C_measured - C_model)**2)

# Minimize error to find rate constant k
res = minimize(total_error, x0=0.5, method="SLSQP", bounds=[(0, 5)])
fitted_k = res.x[0]

print(f"Fitted rate constant k: {fitted_k:.4f}")

# Plot fitted curve vs data
plt.figure(figsize=(7, 5))
plt.scatter(t, C_measured, color="red", label="Measured Data")
plt.plot(t, C0 * np.exp(-fitted_k * t), color="blue", label=f"Fit: k = {fitted_k:.2f}")
plt.xlabel("Time (s)")
plt.ylabel("Concentration (C)")
plt.title("Reaction Kinetics Fitting")
plt.legend()
plt.grid(True)
plt.savefig("kinetics.png")
print("Saved kinetics.png successfully!")