import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
from scipy.optimize import curve_fit

# Data
x = np.array([0, 0.12, 0.26, 0.42, 0.59, 0.72, 0.95])
PCE = np.array([10.64, 8.13, 6.13, 4.63, 2.80, 1.39, 1.03])
bandgap = np.array([1.56, 1.62, 1.69, 1.79, 1.96, 2.01, 2.23])

# Manually scale the data
x_mean, x_std = x.mean(), x.std()
bandgap_mean, bandgap_std = bandgap.mean(), bandgap.std()

scaled_x = (x - x_mean) / x_std
scaled_bandgap = (bandgap - bandgap_mean) / bandgap_std

# Fit Functions
def quadratic_model(X, a, b, c, d, e, f):
    x, y = X
    return a*x**2 + b*y**2 + c*x*y + d*x + e*y + f

# Fit model
params, _ = curve_fit(quadratic_model, (scaled_x, scaled_bandgap), PCE)

# Generate mesh grid for plotting
X_grid, Y_grid = np.meshgrid(np.linspace(min(scaled_x), max(scaled_x), 100), np.linspace(min(scaled_bandgap), max(scaled_bandgap), 100))
Z_grid = quadratic_model((X_grid.ravel(), Y_grid.ravel()), *params).reshape(X_grid.shape)

# Set values exceeding 15 to NaN
Z_grid[Z_grid > 15] = np.nan

# Inverse transform the grid for plotting
plot_x = X_grid * x_std + x_mean
plot_y = Y_grid * bandgap_std + bandgap_mean

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Surface plot with truncated Z-values
surf = ax.plot_surface(plot_x, plot_y, Z_grid, cmap=cm.viridis, alpha=0.8)

# Scatter plot for original data points
sc = ax.scatter(x, bandgap, PCE, color='red', label='Data Points by Helal Miah, 2024', s=50)

# Setting axis ranges
ax.set_xlim([0, 1])
ax.set_ylim([1.5, 2.5])
ax.set_zlim([0, 20])

# Labels
ax.set_xlabel('Halide Ion Concentration x')
ax.set_ylabel('Bandgap (eV)')
ax.set_zlabel('PCE (%)')

# Color bar and legend
# delete the colourbar to shrink the photo cbar = fig.colorbar(surf, shrink=0.5, aspect=5)
#cbar.set_label('PCE (%)')
ax.legend()

plt.title('3D Surface Plot with Quadratic Fit for MAPbIxBr3-x')
plt.show()

# Debug: print fitted parameters
print("Fitted parameters:", params)