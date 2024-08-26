import numpy as np
import matplotlib.pyplot as plt

# Estimated data points based on visual inspection
halide_concentration = np.array([0.07, 0.09, 0.1, 0.12, 0.17])
thermal_conductivity = np.array([0.3, 0.4, 0.45, 0.5, 0.8])

# Labels corresponding to the data points
labels = ['MAPbI3', 'FAPbBr3', 'CsPbBr3', 'MAPbBr3', 'MAPbCl3']

# Fit a polynomial model (Linear or higher order if necessary)
coefficients = np.polyfit(halide_concentration, thermal_conductivity, 1)  # Linear fit
polynomial_fit = np.poly1d(coefficients)

# Generate fitted values
concentration_fit_values = np.linspace(min(halide_concentration), max(halide_concentration), 100)
conductivity_fit_values = polynomial_fit(concentration_fit_values)

# Plot the data points and the fit
plt.figure(figsize=(8, 6))
plt.plot(halide_concentration, thermal_conductivity, 'bo', label='Data Points')

for i, label in enumerate(labels):
    plt.annotate(label, (halide_concentration[i], thermal_conductivity[i]))

plt.plot(concentration_fit_values, conductivity_fit_values, 'r-', label='Linear Fit')
plt.xlabel(r'$C_{a-cubic} \cdot \frac{\bar{v}_s}{3}$ (GW/m$^2\cdot$K)')
plt.ylabel(r'$k$ (W/m$\cdot$K)')
plt.title('Thermal Conductivity vs Halide Ion Concentration')
plt.legend()
plt.grid(True)
plt.show()

# Display the linear equation
equation = f"k = {coefficients[0]:.4f} * x + {coefficients[1]:.4f}"
equation



#BAD VERSION BUT LOOKS GOOD
import numpy as np
import matplotlib.pyplot as plt

# Estimated halide ion concentration (x-axis) and thermal conductivity (y-axis) values
halide_concentration = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
thermal_conductivity = np.array([0.3, 0.4, 0.45, 0.5, 0.8])

# Labels corresponding to the data points
labels = ['MAPbI3', 'FAPbBr3', 'CsPbBr3', 'MAPbBr3', 'MAPbCl3']

# Plot the data points
plt.figure(figsize=(8, 6))
plt.scatter(halide_concentration, thermal_conductivity, color='b')

for i, label in enumerate(labels):
    plt.annotate(label, (halide_concentration[i], thermal_conductivity[i]), textcoords="offset points", xytext=(5,-5), ha='center')

plt.xlabel('Halide Ion Concentration')
plt.ylabel(r'$k$ (W/m$\cdot$K)')
plt.title('Thermal Conductivity vs Halide Ion Concentration')
plt.grid(True)
plt.show()
