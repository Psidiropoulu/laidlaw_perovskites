import numpy as np
import matplotlib.pyplot as plt

# Hypothetical data for demonstration (you can replace these with actual data)
curvature = np.linspace(0.01, 0.1, 10) 
bandgap_energy = np.array([1.0, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5])
distance_from_neutral_axis = np.linspace(0, 10, 10)  # Example distance values

# Create a scatter plot with curvature on x-axis and bandgap energy on y-axis
plt.figure(figsize=(8, 6))
scatter = plt.scatter(curvature, bandgap_energy, c=distance_from_neutral_axis, cmap='viridis', s=100)

# Add colorbar 
cbar = plt.colorbar(scatter)
cbar.set_label('Distance from Neutral Axis')

# Label axes
plt.xlabel('Curvature (1/m)')
plt.ylabel('Bandgap Energy (eV)')
plt.title('Bandgap Energy vs Curvature with Distance Colormap')
plt.grid(True)
plt.show()
