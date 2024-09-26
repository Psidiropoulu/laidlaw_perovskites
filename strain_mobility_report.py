import matplotlib.pyplot as plt
import numpy as np

# Strain values (x-axis)
strain = np.linspace(-0.02, 0.02, 5)

# Assuming approximate values based on the plot for each curve
mu_R_to_Gamma = [800, 620, 550, 500, 420]
mu_R_to_X = [680, 575, 500, 420, 400]
mu_R_to_M = [420, 400, 300, 280, 250]

mu_R_to_Gamma_dash = [680, 420, 380, 300, 280]
mu_R_to_X_dash = [500, 380, 300, 210, 200]
mu_R_to_M_dash = [380, 250, 200, 180, 100]

# Create a finer strain array for smooth quadratic fit curves
strain_fine = np.linspace(-0.02, 0.02, 100)

# Perform quadratic fits (degree=2)
fit_R_to_Gamma = np.polyfit(strain, mu_R_to_Gamma, 2)
fit_R_to_X = np.polyfit(strain, mu_R_to_X, 2)
fit_R_to_M = np.polyfit(strain, mu_R_to_M, 2)

fit_R_to_Gamma_dash = np.polyfit(strain, mu_R_to_Gamma_dash, 2)
fit_R_to_X_dash = np.polyfit(strain, mu_R_to_X_dash, 2)
fit_R_to_M_dash = np.polyfit(strain, mu_R_to_M_dash, 2)

# Get quadratic fit curves
mu_R_to_Gamma_fit = np.polyval(fit_R_to_Gamma, strain_fine)
mu_R_to_X_fit = np.polyval(fit_R_to_X, strain_fine)
mu_R_to_M_fit = np.polyval(fit_R_to_M, strain_fine)

mu_R_to_Gamma_dash_fit = np.polyval(fit_R_to_Gamma_dash, strain_fine)
mu_R_to_X_dash_fit = np.polyval(fit_R_to_X_dash, strain_fine)
mu_R_to_M_dash_fit = np.polyval(fit_R_to_M_dash, strain_fine)

# Create the plot
plt.figure(figsize=(8, 6))

# Plot the original data points
plt.plot(strain, mu_R_to_Gamma, 's', label='Electron mobility [111] direction', color='navy')
plt.plot(strain, mu_R_to_X, 'o', label='Electron mobility [000] direction', color='blue')
plt.plot(strain, mu_R_to_M, '^', label='Electron mobility [110] direction', color='deepskyblue')

plt.plot(strain, mu_R_to_Gamma_dash, 's', label='Hole mobility [111] direction', color='navy')
plt.plot(strain, mu_R_to_X_dash, 'o', label='Hole mobility [000] direction', color='blue')
plt.plot(strain, mu_R_to_M_dash, '^', label='Hole mobility [110] direction', color='deepskyblue')

# Plot the quadratic fit curves
plt.plot(strain_fine, mu_R_to_Gamma_fit, 'navy', linestyle='-')
plt.plot(strain_fine, mu_R_to_X_fit, 'blue', linestyle='-')
plt.plot(strain_fine, mu_R_to_M_fit, 'deepskyblue', linestyle='-')

plt.plot(strain_fine, mu_R_to_Gamma_dash_fit, 'navy', linestyle='--')
plt.plot(strain_fine, mu_R_to_X_dash_fit, 'blue', linestyle='--')
plt.plot(strain_fine, mu_R_to_M_dash_fit, 'deepskyblue', linestyle='--')

# Labeling the axes
plt.xlabel('Strain')
plt.ylabel('μ (cm²/V·s)')
plt.title('Charge Carrier Mobility vs Strain')

# Adding legend
plt.legend()

# Show grid
plt.grid(False)

# Display the plot
plt.show()
