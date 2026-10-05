import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# Part 2: Read data and compute derivatives
# Read freefall.csv (skipping header time,y)
data = np.loadtxt("freefall.csv", delimiter=",", skiprows=1)
t = data[:, 0]
y = data[:, 1]

# Compute velocity v = dy/dt and acceleration a = dv/dt using np.gradient
v = np.gradient(y, t)
a = np.gradient(v, t)

# Print mean acceleration and standard deviation (Part 3)
mean_a = np.mean(a)
std_a = np.std(a)

print(f"Mean acceleration: {mean_a:.2f} m/s^2")
print(f"Standard deviation of acceleration: {std_a:.2f} m/s^2")


# Part 4: Integrate back
# Recover velocity from acceleration, then position from velocity
v_recovered = cumulative_trapezoid(a, t, initial=0) + v[0]
y_recovered = cumulative_trapezoid(v_recovered, t, initial=0) + y[0]

# Calculate max difference between original and recovered position
max_diff = np.max(np.abs(y - y_recovered))
print(f"Max difference in recovered position: {max_diff:.4f} m")

# Part 5: Plotting
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(8, 10))

# Panel 1: Position y(t)
ax1.plot(t, y, color="blue", label="Position y(t)")
ax1.set_ylabel("Position (m)")
ax1.set_title("Free Fall Motion Analysis")
ax1.grid(True)

# Panel 2: Velocity v(t)
ax2.plot(t, v, color="orange", label="Velocity v(t)")
ax2.set_ylabel("Velocity (m/s)")
ax2.grid(True)

# Panel 3: Acceleration a(t)
ax3.plot(t, a, color="red", alpha=0.6, label="Acceleration a(t)")
ax3.axhline(-9.81, color="black", linestyle="--", label="g = -9.81 m/s²")
ax3.set_xlabel("Time (s)")
ax3.set_ylabel("Acceleration (m/s²)")
ax3.legend()
ax3.grid(True)

plt.tight_layout()
plt.savefig("motion.png")
print("Saved motion.png successfully!")