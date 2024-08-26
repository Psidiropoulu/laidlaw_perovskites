import matplotlib.pyplot as plt
import numpy as np

# Blue solid line (Pb without SOC)
strain_solid = np.array([-0.02, -0.01, 0.00, 0.01, 0.02])
bandgap_solid = np.array([0.80, 0.90, 1.00, 1.05, 1.08])  # Estimated from the graph

# Approximate data points for the blue dashed line (Pb with SOC)
strain_dashed = np.array([-0.02, -0.01, 0.00, 0.01, 0.02])
bandgap_dashed = np.array([2.0, 2.10, 2.25, 2.35, 2.4])  # Estimated from the graph

# Calculating slope (m) and intercept (b) for the solid line (Pb without SOC)
slope_solid_alt = np.polyfit(strain_solid, bandgap_solid, 1)[0]
intercept_solid_alt = np.polyfit(strain_solid, bandgap_solid, 1)[1]

# Calculating slope (m) and intercept (b) for the dashed line (Pb with SOC)
slope_dashed_alt = np.polyfit(strain_dashed, bandgap_dashed, 1)[0]
intercept_dashed_alt = np.polyfit(strain_dashed, bandgap_dashed, 1)[1]

# Formulating the linear equations
equation_solid_alt = f"E_g (solid) = {slope_solid_alt:.2f} * Strain + {intercept_solid_alt:.2f}"
equation_dashed_alt = f"E_g (dashed) = {slope_dashed_alt:.2f} * Strain + {intercept_dashed_alt:.2f}"

print(equation_solid_alt, equation_dashed_alt)

# Plot data from all graphs on the same plot
plt.scatter(strain_solid, bandgap_solid, label='without SOC (Yadav and Ray, 2023)')
plt.plot(strain_solid, slope_solid_alt * strain_solid + intercept_solid_alt, 'b-')

plt.scatter(strain_dashed, bandgap_dashed, label='with SOC (Yadav and Ray, 2023)')
plt.plot(strain_dashed, slope_dashed_alt * strain_dashed + intercept_dashed_alt, 'r--')


# Approximate data points ATTIQUE ET AL
size_percentages = np.array([0.8, 0.9, 1.0, 1.1, 1.2, 1.3])  # representing 80%, 90%, ... 130% of normal size
strain_values = size_percentages - 1.0
bandgap_lead = np.array([0.5, 1.45, 1.55, 2.35, 2.65, 2.95])  # estimated values from the graph


# Fit a second-degree polynomial (quadratic) model using the strain values
coefficients_lead_strain_quad = np.polyfit(strain_values, bandgap_lead, 2)
# Create a polynomial function from the coefficients
polynomial_lead_strain_quad = np.poly1d(coefficients_lead_strain_quad)

# Print the quadratic equation
equation_lead_strain_quad = f"E_g (CH3NH3PbI3) = {coefficients_lead_strain_quad[0]:.2f} * Strain^2 + {coefficients_lead_strain_quad[1]:.2f} * Strain + {coefficients_lead_strain_quad[2]:.2f}"

# Generate a range of strain values for plotting the quadratic fit
strain_fit_values = np.linspace(min(strain_values), max(strain_values), 100)
bandgap_fit_values_quad = polynomial_lead_strain_quad(strain_fit_values)


plt.plot(strain_values, bandgap_lead, 'ko', label='Data Points')
plt.plot(strain_fit_values, bandgap_fit_values_quad, 'k-', label='Quadratic Fit, (Attique et al., 2022)')

print(equation_lead_strain_quad)

# Adding labels and title
plt.xlabel('Strain')
plt.ylabel('Band Gap Energy (eV)')
plt.title('Band Gap Energy vs Strain for Pb-based Perovskite')
plt.legend()
plt.grid(False)

# Show plot
plt.show()





# Strain values (in %) (THE GRAPHS IN THE MIDDLE)
strain_values_percent = np.array([-5, -4, -3, -2, -1, 0])  # X-axis values (Strain %)

# Corresponding Gap energy values for each direction (Y-axis values)
gap_energy_a = np.array([1.32, 1.38, 1.44, 1.50, 1.56, 1.60])  # Black line (a-direction)
gap_energy_b = np.array([1.34, 1.40, 1.46, 1.52, 1.57, 1.60])  # Red line (b-direction)
gap_energy_c = np.array([1.30, 1.39, 1.48, 1.54, 1.58, 1.60])  # Green line (c-direction)

# Fit linear models for each direction (instead of quadratic)
coefficients_a_linear = np.polyfit(strain_values_percent, gap_energy_a, 1)
coefficients_b_linear = np.polyfit(strain_values_percent, gap_energy_b, 1)
coefficients_c_linear = np.polyfit(strain_values_percent, gap_energy_c, 1)

# Create linear functions from the coefficients
polynomial_a_linear = np.poly1d(coefficients_a_linear)
polynomial_b_linear = np.poly1d(coefficients_b_linear)
polynomial_c_linear = np.poly1d(coefficients_c_linear)

# Generate the linear fit values for plotting
gap_fit_values_a_linear = polynomial_a_linear(strain_fit_values)
gap_fit_values_b_linear = polynomial_b_linear(strain_fit_values)
gap_fit_values_c_linear = polynomial_c_linear(strain_fit_values)

# Plot the data points and the linear fits for each direction
plt.figure(figsize=(10, 8))

plt.plot(strain_values_percent, gap_energy_a, 'ko', label='a-direction Data Points')
plt.plot(strain_fit_values, gap_fit_values_a_linear, 'k-', label='a-direction Linear Fit')

plt.plot(strain_values_percent, gap_energy_b, 'ro', label='b-direction Data Points')
plt.plot(strain_fit_values, gap_fit_values_b_linear, 'r-', label='b-direction Linear Fit')

plt.plot(strain_values_percent, gap_energy_c, 'go', label='c-direction Data Points')
plt.plot(strain_fit_values, gap_fit_values_c_linear, 'g-', label='c-direction Linear Fit')

plt.xlabel('Strain (%)')
plt.ylabel('Gap Energy (eV)')
plt.title('Linear Fit: Gap Energy vs Strain for Different Directions')
plt.legend()
plt.grid(True)
plt.show()

# Print the linear equations
equation_a_linear = f"E_g (a-direction) = {coefficients_a_linear[0]:.4f} * Strain + {coefficients_a_linear[1]:.4f}"
equation_b_linear = f"E_g (b-direction) = {coefficients_b_linear[0]:.4f} * Strain + {coefficients_b_linear[1]:.4f}"
equation_c_linear = f"E_g (c-direction) = {coefficients_c_linear[0]:.4f} * Strain + {coefficients_c_linear[1]:.4f}"

equation_a_linear, equation_b_linear, equation_c_linear



import numpy as np
import matplotlib.pyplot as plt

# Extracting data points based on visual estimation from the graph

# Strain values (in %)
strain_values_percent = np.array([0, 1, 2, 3, 4, 5])

# Corresponding Gap energy values for each direction (Y-axis values)
gap_energy_a = np.array([1.62, 1.62, 1.62, 1.62, 1.62, 1.62])  # Approximation for a-direction (gray)
gap_energy_b = np.array([1.62, 1.61, 1.60, 1.59, 1.58, 1.57])  # Approximation for b-direction (red)
gap_energy_c = np.array([1.64, 1.66, 1.69, 1.71, 1.72, 1.71])  # Approximation for c-direction (green)

# Fit polynomial models for each direction based on the best fit
coefficients_a = np.polyfit(strain_values_percent, gap_energy_a, 1)  # Linear for a-direction
coefficients_b = np.polyfit(strain_values_percent, gap_energy_b, 2)  # Quadratic for b-direction
coefficients_c = np.polyfit(strain_values_percent, gap_energy_c, 2)  # Quadratic for c-direction

# Create polynomial functions from the coefficients
polynomial_a = np.poly1d(coefficients_a)
polynomial_b = np.poly1d(coefficients_b)
polynomial_c = np.poly1d(coefficients_c)

# Generate a range of strain values for plotting the fits
strain_fit_values = np.linspace(min(strain_values_percent), max(strain_values_percent), 100)
gap_fit_values_a = polynomial_a(strain_fit_values)
gap_fit_values_b = polynomial_b(strain_fit_values)
gap_fit_values_c = polynomial_c(strain_fit_values)

# Plot the data points and the fits for each direction
plt.figure(figsize=(10, 8))

plt.plot(strain_values_percent, gap_energy_a, 'ko', label='a-direction Data Points')
plt.plot(strain_fit_values, gap_fit_values_a, 'k-', label='a-direction Best Fit (Linear)')

plt.plot(strain_values_percent, gap_energy_b, 'ro', label='b-direction Data Points')
plt.plot(strain_fit_values, gap_fit_values_b, 'r-', label='b-direction Best Fit (Quadratic)')

plt.plot(strain_values_percent, gap_energy_c, 'go', label='c-direction Data Points')
plt.plot(strain_fit_values, gap_fit_values_c, 'g-', label='c-direction Best Fit (Quadratic)')

plt.xlabel('Strain (%)')
plt.ylabel('Gap Energy (eV)')
plt.title('Best Fit: Gap Energy vs Strain for Different Directions (Tensile)')
plt.legend()
plt.grid(True)
plt.show()

# Print the best fit equations
equation_a = f"E_g (a-direction) = {coefficients_a[0]:.4f} * Strain + {coefficients_a[1]:.4f}"
equation_b = f"E_g (b-direction) = {coefficients_b[0]:.4f} * Strain^2 + {coefficients_b[1]:.4f} * Strain + {coefficients_b[2]:.4f}"
equation_c = f"E_g (c-direction) = {coefficients_c[0]:.4f} * Strain^2 + {coefficients_c[1]:.4f} * Strain + {coefficients_c[2]:.4f}"

equation_a, equation_b, equation_c