import pandas as pd
import matplotlib.pyplot as plt

# Data from the table
data = {
    "x (Bromine concentration)": [0, 0.12, 0.26, 0.42, 0.59, 0.72, 0.95],
    "Jsc (mA cm−2)": [17.45, 13.89, 10.39, 8.20, 6.35, 3.18, 2.38],
    "Voc (V)": [0.977, 0.890, 0.936, 0.898, 0.834, 0.940, 0.832],
    "FF (%)": [61.13, 65.31, 61.95, 65.84, 52.40, 48.54, 49.81],
    "PCE (%)": [10.64, 8.13, 6.13, 4.63, 2.80, 1.39, 1.03],
    "Band-gap (eV)": [1.56, 1.62, 1.69, 1.79, 1.96, 2.01, 2.23]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plotting
fig, axes = plt.subplots(3, 2, figsize=(14, 16))

# Jsc vs Bromine concentration
axes[0, 0].plot(df["x (Bromine concentration)"], df["Jsc (mA cm−2)"], marker='o')
axes[0, 0].set_title("Jsc vs Bromine concentration")
axes[0, 0].set_xlabel("Bromine concentration (x)")
axes[0, 0].set_ylabel("Jsc (mA cm−2)")

# Voc vs Bromine concentration
axes[0, 1].plot(df["x (Bromine concentration)"], df["Voc (V)"], marker='o')
axes[0, 1].set_title("Voc vs Bromine concentration")
axes[0, 1].set_xlabel("Bromine concentration (x)")
axes[0, 1].set_ylabel("Voc (V)")

# FF vs Bromine concentration
axes[1, 0].plot(df["x (Bromine concentration)"], df["FF (%)"], marker='o')
axes[1, 0].set_title("FF vs Bromine concentration")
axes[1, 0].set_xlabel("Bromine concentration (x)")
axes[1, 0].set_ylabel("FF (%)")

# PCE vs Bromine concentration
axes[1, 1].plot(df["x (Bromine concentration)"], df["PCE (%)"], marker='o')
axes[1, 1].set_title("PCE vs Bromine concentration")
axes[1, 1].set_xlabel("Bromine concentration (x)")
axes[1, 1].set_ylabel("PCE (%)")

# Band-gap vs Bromine concentration
axes[2, 0].plot(df["x (Bromine concentration)"], df["Band-gap (eV)"], marker='o')
axes[2, 0].set_title("Band-gap vs Bromine concentration")
axes[2, 0].set_xlabel("Bromine concentration (x)")
axes[2, 0].set_ylabel("Band-gap (eV)")

# Adjust layout
plt.tight_layout()

plt.show()