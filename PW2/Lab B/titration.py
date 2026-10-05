import numpy as np
import matplotlib.pyplot as plt

# Read titration.csv
data = np.loadtxt("titration.csv", delimiter=",", skiprows=1)
V = data[:, 0]
pH = data[:, 1]

# Compute slope (dpH / dV)
dpH_dV = np.gradient(pH, V)

# Find volume where slope is maximum
max_idx = np.argmax(dpH_dV)
equiv_vol = V[max_idx]

print(f"Titration equivalence point: {equiv_vol:.2f} mL")

# Plot pH curve and derivative side-by-side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Panel 1: pH curve
ax1.plot(V, pH, color="blue")
ax1.axvline(equiv_vol, color="red", linestyle="--", label=f"Equiv point = {equiv_vol:.1f} mL")
ax1.set_xlabel("Volume of Base (mL)")
ax1.set_ylabel("pH")
ax1.set_title("Titration Curve")
ax1.legend()
ax1.grid(True)

# Panel 2: Slope dpH/dV
ax2.plot(V, dpH_dV, color="green")
ax2.axvline(equiv_vol, color="red", linestyle="--", label=f"Peak at {equiv_vol:.1f} mL")
ax2.set_xlabel("Volume of Base (mL)")
ax2.set_ylabel("dpH / dV")
ax2.set_title("Derivative (Slope) Curve")
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig("titration.png")
print("Saved titration.png successfully!")