import matplotlib.pyplot as plt
import numpy as np

# Adding more points from the picture for better fit approximation
bandgap_more = np.array([1.1, 1.2, 1.4, 1.5, 1.6, 1.75, 2.0, 2.1, 2.3])
pce_more = np.array([33, 32, 32, 31, 30, 28, 24, 22, 17])  # Added more points to match the original graph

# Perform a polynomial fit (2nd degree) to get a best-fit line
coeffs = np.polyfit(bandgap_more, pce_more, 2)
pce_fit = np.polyval(coeffs, bandgap_more)

# Create the plot with the best fit line
plt.figure(figsize=(8, 4))
plt.plot(bandgap_more, pce_more, 'k-', label='Original PCE', linewidth=2)
plt.scatter(bandgap_more, pce_more, color='r', zorder=5)  # Original points
plt.plot(bandgap_more, pce_fit, 'b--', label='Best fit (2nd degree)', linewidth=2)  # Best fit line

# Labels and title
plt.xlabel('Bandgap (eV)', fontsize=12)
plt.ylabel('PCE (%)', fontsize=12)
plt.title('PCE vs Bandgap Energy with Best Fit', fontsize=14)
plt.grid(False)
plt.ylim(0, 35)
plt.legend()

# Display the plot
plt.show()