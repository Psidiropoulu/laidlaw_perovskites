import numpy as np
import matplotlib.pyplot as plt

# Extracting data points based on visual estimation from the graph QUADRATIC FIT

# Strain values (X-axis)
strain_values = np.array([-0.02, -0.015, -0.01, -0.005, 0.0, 0.005, 0.01, 0.015, 0.02])

# Corresponding mobility values (Y-axis) for each transition
mobility_R_to_Gamma = np.array([750, 680, 620, 580, 540, 500, 460, 420, 400])  # Dark blue line (R -> Γ)
mobility_R_to_X = np.array([500, 460, 420, 380, 350, 320, 300, 280, 260])  # Medium blue line (R -> X)
mobility_R_to_M = np.array([300, 270, 250, 230, 210, 190, 180, 170, 160])  # Light blue line (R -> M)

# Fit polynomial models for each line based on best fit
coefficients_R_to_Gamma = np.polyfit(strain_values, mobility_R_to_Gamma, 2)  # Quadratic for R -> Γ
coefficients_R_to_X = np.polyfit(strain_values, mobility_R_to_X, 2)  # Quadratic for R -> X
coefficients_R_to_M = np.polyfit(strain_values, mobility_R_to_M, 2)  # Quadratic for R -> M

# Create polynomial functions from the coefficients
polynomial_R_to_Gamma = np.poly1d(coefficients_R_to_Gamma)
polynomial_R_to_X = np.poly1d(coefficients_R_to_X)
polynomial_R_to_M = np.poly1d(coefficients_R_to_M)

# Generate a range of strain values for plotting the fits
strain_fit_values = np.linspace(min(strain_values), max(strain_values), 100)
mobility_fit_values_R_to_Gamma = polynomial_R_to_Gamma(strain_fit_values)
mobility_fit_values_R_to_X = polynomial_R_to_X(strain_fit_values)
mobility_fit_values_R_to_M = polynomial_R_to_M(strain_fit_values)

# Plot the data points and the fits for each transition
plt.figure(figsize=(10, 8))

plt.plot(strain_values, mobility_R_to_Gamma, 'ko', label='R -> Γ Data Points')
plt.plot(strain_fit_values, mobility_fit_values_R_to_Gamma, 'k-', label='R -> Γ Best Fit (Quadratic)')

plt.plot(strain_values, mobility_R_to_X, 'bo', label='R -> X Data Points')
plt.plot(strain_fit_values, mobility_fit_values_R_to_X, 'b-', label='R -> X Best Fit (Quadratic)')

plt.plot(strain_values, mobility_R_to_M, 'co', label='R -> M Data Points')
plt.plot(strain_fit_values, mobility_fit_values_R_to_M, 'c-', label='R -> M Best Fit (Quadratic)')

plt.xlabel('Strain')
plt.ylabel('Mobility (cm^2/V.s)')
plt.title('Best Fit: Mobility vs Strain for Different Transitions')
plt.legend()
plt.grid(True)
plt.show()

# Print the best fit equations
equation_R_to_Gamma = f"μ (R -> Γ) = {coefficients_R_to_Gamma[0]:.4f} * Strain^2 + {coefficients_R_to_Gamma[1]:.4f} * Strain + {coefficients_R_to_Gamma[2]:.4f}"
equation_R_to_X = f"μ (R -> X) = {coefficients_R_to_X[0]:.4f} * Strain^2 + {coefficients_R_to_X[1]:.4f} * Strain + {coefficients_R_to_X[2]:.4f}"
equation_R_to_M = f"μ (R -> M) = {coefficients_R_to_M[0]:.4f} * Strain^2 + {coefficients_R_to_M[1]:.4f} * Strain + {coefficients_R_to_M[2]:.4f}"

equation_R_to_Gamma, equation_R_to_X, equation_R_to_M



#LINEAR FIT
# Fit linear models for each transition
coefficients_R_to_Gamma_linear = np.polyfit(strain_values, mobility_R_to_Gamma, 1)  # Linear for R -> Γ
coefficients_R_to_X_linear = np.polyfit(strain_values, mobility_R_to_X, 1)  # Linear for R -> X
coefficients_R_to_M_linear = np.polyfit(strain_values, mobility_R_to_M, 1)  # Linear for R -> M

# Create linear functions from the coefficients
polynomial_R_to_Gamma_linear = np.poly1d(coefficients_R_to_Gamma_linear)
polynomial_R_to_X_linear = np.poly1d(coefficients_R_to_X_linear)
polynomial_R_to_M_linear = np.poly1d(coefficients_R_to_M_linear)

# Generate the linear fit values for plotting
mobility_fit_values_R_to_Gamma_linear = polynomial_R_to_Gamma_linear(strain_fit_values)
mobility_fit_values_R_to_X_linear = polynomial_R_to_X_linear(strain_fit_values)
mobility_fit_values_R_to_M_linear = polynomial_R_to_M_linear(strain_fit_values)

# Plot the data points and the linear fits for each transition
plt.figure(figsize=(10, 8))

plt.plot(strain_values, mobility_R_to_Gamma, 'ko', label='R -> Γ Data Points')
plt.plot(strain_fit_values, mobility_fit_values_R_to_Gamma_linear, 'k-', label='R -> Γ Linear Fit')

plt.plot(strain_values, mobility_R_to_X, 'bo', label='R -> X Data Points')
plt.plot(strain_fit_values, mobility_fit_values_R_to_X_linear, 'b-', label='R -> X Linear Fit')

plt.plot(strain_values, mobility_R_to_M, 'co', label='R -> M Data Points')
plt.plot(strain_fit_values, mobility_fit_values_R_to_M_linear, 'c-', label='R -> M Linear Fit')

plt.xlabel('Strain')
plt.ylabel('Mobility (cm^2/V.s)')
plt.title('Linear Fit: Mobility vs Strain for Different Transitions')
plt.legend()
plt.grid(True)
plt.show()

# Print the linear fit equations
equation_R_to_Gamma_linear = f"μ (R -> Γ) = {coefficients_R_to_Gamma_linear[0]:.4f} * Strain + {coefficients_R_to_Gamma_linear[1]:.4f}"
equation_R_to_X_linear = f"μ (R -> X) = {coefficients_R_to_X_linear[0]:.4f} * Strain + {coefficients_R_to_X_linear[1]:.4f}"
equation_R_to_M_linear = f"μ (R -> M) = {coefficients_R_to_M_linear[0]:.4f} * Strain + {coefficients_R_to_M_linear[1]:.4f}"

equation_R_to_Gamma_linear, equation_R_to_X_linear, equation_R_to_M_linear
