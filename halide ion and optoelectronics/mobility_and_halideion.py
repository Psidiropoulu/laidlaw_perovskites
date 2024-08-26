import numpy as np
import matplotlib.pyplot as plt

# Extracting data points based on visual estimation from the graph

# Bromide fraction (X-axis)
bromide_fraction = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

# Charge-carrier mobility (Y-axis) for each material
mobility_FAPb = np.array([25, 5, 8, 2, 4, 6, 10, 12, 15, 18, 23])  # Blue points (FAPb(BrₓI₁₋ₓ)₃)
mobility_CsFA = np.array([40, 35, 32, 30, 28, 25, 22, 20, 18, 16, 15])  # Red points (Cs₀.₁₇FA₀.₈₃Pb(BrₓI₁₋ₓ)₃)

# Fit polynomial models for each dataset
coefficients_FAPb = np.polyfit(bromide_fraction, mobility_FAPb, 3)  # Cubic fit for FAPb(BrₓI₁₋ₓ)₃
coefficients_CsFA = np.polyfit(bromide_fraction, mobility_CsFA, 3)  # Cubic fit for Cs₀.₁₇FA₀.₈₃Pb(BrₓI₁₋ₓ)₃

# Create polynomial functions from the coefficients
polynomial_FAPb = np.poly1d(coefficients_FAPb)
polynomial_CsFA = np.poly1d(coefficients_CsFA)

# Generate a range of bromide fraction values for plotting the fits
bromide_fit_values = np.linspace(min(bromide_fraction), max(bromide_fraction), 100)
mobility_fit_values_FAPb = polynomial_FAPb(bromide_fit_values)
mobility_fit_values_CsFA = polynomial_CsFA(bromide_fit_values)

# Plot the data points and the fits for each material
plt.figure(figsize=(10, 8))

plt.plot(bromide_fraction, mobility_FAPb, 'bo', label='FAPb(BrₓI₁₋ₓ)₃ Data Points')
plt.plot(bromide_fit_values, mobility_fit_values_FAPb, 'b-', label='FAPb(BrₓI₁₋ₓ)₃ Best Fit (Cubic)')

plt.plot(bromide_fraction, mobility_CsFA, 'ro', label='Cs₀.₁₇FA₀.₈₃Pb(BrₓI₁₋ₓ)₃ Data Points')
plt.plot(bromide_fit_values, mobility_fit_values_CsFA, 'r-', label='Cs₀.₁₇FA₀.₈₃Pb(BrₓI₁₋ₓ)₃ Best Fit (Cubic)')

plt.xlabel('Bromide Fraction (x)')
plt.ylabel('Charge-Carrier Mobility (cm^2/V.s)')
plt.title('Best Fit: Charge-Carrier Mobility vs Bromide Fraction')
plt.legend()
plt.grid(True)
plt.show()

# Print the best fit equations
equation_FAPb = f"μ (FAPb(BrₓI₁₋ₓ)₃) = {coefficients_FAPb[0]:.4f} * x^3 + {coefficients_FAPb[1]:.4f} * x^2 + {coefficients_FAPb[2]:.4f} * x + {coefficients_FAPb[3]:.4f}"
equation_CsFA = f"μ (Cs₀.₁₇FA₀.₈₃Pb(BrₓI₁₋ₓ)₃) = {coefficients_CsFA[0]:.4f} * x^3 + {coefficients_CsFA[1]:.4f} * x^2 + {coefficients_CsFA[2]:.4f} * x + {coefficients_CsFA[3]:.4f}"

print(equation_FAPb, equation_CsFA)