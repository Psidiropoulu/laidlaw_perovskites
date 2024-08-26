import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Step 1: Estimate the data points from the graph
percent = np.array([0, 20, 40, 60, 80, 100])  # Estimated percentages from the graph
E_gap = np.array([1.6, 1.7, 1.8, 1.9, 2.0, 2.2])  # Estimated E_gap values in eV

# Step 2: Define the linear model
def linear_model(x, a, b):
    return a * x + b

# Step 3: Fit the data to the linear model
params_linear, _ = curve_fit(linear_model, percent, E_gap)

# Step 4: Calculate the predicted values using the linear fit
E_gap_pred = linear_model(percent, *params_linear)

# Step 5: Plot the original data and the linear fit
plt.scatter(percent, E_gap, color='black', label='Data')
plt.plot(percent, E_gap_pred, 'r--', label=f'Linear fit: y = {params_linear[0]:.4f}x + {params_linear[1]:.4f}')
plt.xlabel('Percentage (%)')
plt.ylabel('E_gap (eV)')
plt.legend()
plt.title('Linear Fit of E_gap vs Percentage')
plt.show()

# Step 6: Output the equation of the line
print(f"The linear fit equation is: E_gap = {params_linear[0]:.4f} * Percentage + {params_linear[1]:.4f}")