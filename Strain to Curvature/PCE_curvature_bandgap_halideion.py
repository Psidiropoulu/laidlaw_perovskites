import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.optimize import curve_fit

# Data
x = np.array([0, 0.12, 0.26, 0.42, 0.59, 0.72, 0.95])
PCE = np.array([10.64, 8.13, 6.13, 4.63, 2.80, 1.39, 1.03])
bandgap = np.array([1.56, 1.62, 1.69, 1.79, 1.96, 2.01, 2.23])

# Estimating the curvature
bending_angle = np.array([0, 10, 20, 30, 40, 50, 60])
R = 0.1
bending_angles_radians = bending_angle * np.pi / 180
curvature_points = bending_angles_radians * R

# PCE via curvature
PCE_curvature = -994.96762 * (curvature_points**2) + 1.9772 * curvature_points + 20.5585

# Generate synthetic data for curvature and halide ion concentration
curvature = np.linspace(0, 0.14, 100)
halide_ion_concentration = np.linspace(0, 1.0, 100)

# Manually scale the data
x_mean, x_std = x.mean(), x.std()
bandgap_mean, bandgap_std = bandgap.mean(), bandgap.std()

scaled_x = (x - x_mean) / x_std
scaled_bandgap = (bandgap - bandgap_mean) / bandgap_std

# Fit Functions
def quadratic_model(X, a, b, c, d, e, f):
    x, y = X
    return a*x**2 + b*y**2 + c*x*y + d*x + e*y + f

# Fix the shapes
xdata = np.vstack((scaled_x, scaled_bandgap))

# Ensure the correct length for ydata
params, _ = curve_fit(quadratic_model, xdata[:, :7], PCE_curvature[:7])

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create mesh grids for 3D plotting
Curvature, HalideIon = np.meshgrid(curvature, halide_ion_concentration)

# Define quadratic and linear relationships for E_bandgap
E_bandgap = -4.38 * (Curvature * R)**2 + 5.19 * (Curvature * R) + 1.55 + 0.0075 * HalideIon

# Simulate PCE based on both curvature and halide ion concentration
PCE = 32.70706662 * HalideIon**2 + 33.38136811 * E_bandgap**2 - 65.55173437 * HalideIon * E_bandgap - 6.1075773 * HalideIon + 2.69812375 * E_bandgap + 3.98785005

# Plotting
surf = ax.plot_surface(Curvature, HalideIon, E_bandgap, facecolors=cm.viridis((PCE - np.min(PCE)) / (np.max(PCE) - np.min(PCE))), edgecolor='none')

# Adding the colorbar explicitly with the 'ax' parameter
cbar = fig.colorbar(cm.ScalarMappable(cmap=cm.viridis, norm=plt.Normalize(np.min(PCE), np.max(PCE))), ax=ax, shrink=0.5, aspect=5)
cbar.set_label('PCE (%)')

# Plot the given points
ax.scatter(curvature_points, x, bandgap, color='r', s=50, label='Given Points')

# Labels
ax.set_xlabel('Curvature')
ax.set_ylabel('Halide Ion Concentration')
ax.set_zlabel('E_bandgap (eV)')
ax.legend()

plt.title('3D Visualization of E_bandgap vs. Curvature and Halide Ion Concentration')
plt.show()