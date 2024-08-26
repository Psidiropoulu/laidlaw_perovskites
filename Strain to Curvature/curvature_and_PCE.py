import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Data from the table
bending_angle = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80])
pce = np.array([20.56, 20.38, 19.36, 18.29, 15.37, 12.47, 10.11, 7.31, 0.59])

#estimating the radius of the arc
R = 0.1
bending_angles_radians = bending_angle * np.pi / 180
curvature=bending_angles_radians*R

# Define model functions for fitting
def linear_fit(x, a, b):
    return a * x + b

def quadratic_fit(x, a, b, c):
    return a * x**2 + b * x + c

def exponential_fit(x, a, b):
    return a * np.exp(b * x)

# Function to calculate R-squared value
def calculate_r2(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - (ss_res / ss_tot)

# Function to determine the best fit model
def find_best_fit(x, y):
    models = {
        'linear': (linear_fit, 2),
        'quadratic': (quadratic_fit, 3),
        'exponential': (exponential_fit, 2)
    }
    best_fit_model = None
    best_fit_params = None
    best_r2 = -np.inf
    best_model_name = None
    
    for name, (model, param_count) in models.items():
        try:
            params, _ = curve_fit(model, x, y, maxfev=10000)
            y_pred = model(x, *params)
            r2 = calculate_r2(y, y_pred)
            
            if r2 > best_r2:
                best_r2 = r2
                best_fit_model = model
                best_fit_params = params
                best_model_name = name
        except:
            continue
    
    return best_fit_model, best_fit_params, best_r2, best_model_name

# Finding the best fit for PCE
model_pce, params_pce, r2_pce, model_name_pce = find_best_fit(curvature, pce)
best_fit_pce = model_pce(curvature, *params_pce)

# Output the best fit lines and their equations
if model_name_pce == 'linear':
    equation_pce = f'y = {params_pce[0]:.4f}x + {params_pce[1]:.4f}'
elif model_name_pce == 'quadratic':
    equation_pce = f'y = {params_pce[0]:.4f}x^2 + {params_pce[1]:.4f}x + {params_pce[2]:.4f}'
elif model_name_pce == 'exponential':
    equation_pce = f'y = {params_pce[0]:.4f}e^({params_pce[1]:.4f}x)'

print(f'Best fit for PCE: {model_name_pce} with R^2 = {r2_pce:.4f}')
print(f'Equation: {equation_pce}')

# Plotting the graphs
plt.figure(figsize=(10, 6))
plt.plot(curvature, pce, marker='o', label='PCE by Seong et al, 2022')
plt.plot(curvature, best_fit_pce, linestyle='-', label=f'Best Fit PCE (R2={r2_pce:.2f})')

plt.title('PCE vs Curvature')
plt.xlabel('Curvature')
plt.ylabel('PCE')
plt.legend()
plt.grid(False)

plt.show()
