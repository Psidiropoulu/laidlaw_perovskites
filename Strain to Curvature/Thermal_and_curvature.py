import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Example data (replace with actual data)
curvature = np.linspace(0.01, 0.1, 100)  # Curvature values
thermal_conductivity = 0.5 + 0.3 * curvature + 0.05 * np.random.randn(100)  # Thermal conductivity with some noise
distance_from_neutral_axis = np.linspace(0, 10, 100)  # Distance from neutral axis

# Fit a line (linear fit as an example)
coefficients = np.polyfit(curvature, thermal_conductivity, 1)
fit_line = np.poly1d(coefficients)(curvature)

# Create a colormap based on distance from the neutral axis
norm = plt.Normalize(distance_from_neutral_axis.min(), distance_from_neutral_axis.max())
points = np.array([curvature, fit_line]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
lc = LineCollection(segments, cmap='coolwarm', norm=norm)
lc.set_array(distance_from_neutral_axis)
lc.set_linewidth(2)

# Plotting the data
plt.figure(figsize=(8, 6))
plt.gca().add_collection(lc)
plt.scatter(curvature, thermal_conductivity, c=distance_from_neutral_axis, cmap='coolwarm', s=50)
plt.colorbar(lc, label='Distance from Neutral Axis')
plt.xlabel('Curvature (1/m)')
plt.ylabel('Thermal Conductivity (W/m·K)')
plt.title('Thermal Conductivity vs Curvature with Distance Colormap')
plt.grid(True)
plt.show()

# Print the equation of the line of best fit
equation = f"Thermal Conductivity = {coefficients[0]:.4f} * Curvature + {coefficients[1]:.4f}"
equation