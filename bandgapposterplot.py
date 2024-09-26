import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
from scipy.optimize import curve_fit

energy_a = np.array([1.36, 1.475, 1.525, 1.565, 1.63, 1.63, 1.625, 1.62, 1.662, 1.615, 1.615, 1.61])
energy_b = np.array([1.31, 1.38, 1.47, 1.565, 1.64, 1.61, 1.59, 1.58, 1.57, 1.56, 1.55, 1.54])
energy_c = np.array([1.36, 1.475, 1.525, 1.565, 1.63, 1.66, 1.70, 1.73, 1.74, 1.73, 1.72, 1.71])

strain = np.array([-5, -4, -3, -2, -1, 0, 1.0, 2.0, 3.0, 3.5, 4.0, 4.5, 5.0])



# Adjusting the figure size to make it longer and less tall
plt.figure(figsize=(10, 4))

# Plotting the data again with the new figure size
plt.plot(strain[:len(energy_a)], energy_a, 'o-', label='Bandgap energy in a-direction', color='blue')
plt.plot(strain[:len(energy_b)], energy_b, 'o-', label='Bandgap energy in b-direction', color='red')
plt.plot(strain[:len(energy_c)], energy_c, 'o-', label='Bandgap energy in c-direction', color='green')

# Adding labels and title
plt.xlabel('Strain (%)')
plt.ylabel('Bandgap energy (eV)')
plt.title('Bandgap energy Vs strain in a, b, c directions within the perovsktie')
plt.legend()
plt.grid(False)

# Show the updated plot
plt.show()