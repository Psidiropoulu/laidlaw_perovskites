import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Step 1: Estimate the data points from the graph (you can adjust these based on more precise data extraction if needed)
strain = np.array([-3, -2, -1, 0, 1, 2, 3])
k_L = np.array([0.55, 0.45, 0.4, 0.35, 0.30, 0.25, 0.20])  # Estimated points from the graph

# Step 2: Define models for fitting
def linear_model(x, a, b):
    return a * x + b

def inverse_model(x, a, b, c):
    return a / (x + c) + b

def quadratic_model(x, a, b, c):
    return a * x**2 + b * x + c

# Step 3: Fit the data to each model
params_linear, _ = curve_fit(linear_model, strain, k_L)
params_inverse, _ = curve_fit(inverse_model, strain, k_L, p0=[1, 1, 0.1])  # initial guess to avoid zero
params_quadratic, _ = curve_fit(quadratic_model, strain, k_L)

# Step 4: Calculate R-squared values manually
def calculate_r2(actual, predicted):
    residual_sum_of_squares = np.sum((actual - predicted) ** 2)
    total_sum_of_squares = np.sum((actual - np.mean(actual)) ** 2)
    r2 = 1 - (residual_sum_of_squares / total_sum_of_squares)
    return r2

k_L_pred_linear = linear_model(strain, *params_linear)
k_L_pred_inverse = inverse_model(strain, *params_inverse)
k_L_pred_quadratic = quadratic_model(strain, *params_quadratic)

r2_linear = calculate_r2(k_L, k_L_pred_linear)
r2_inverse = calculate_r2(k_L, k_L_pred_inverse)
r2_quadratic = calculate_r2(k_L, k_L_pred_quadratic)

# Step 5: Determine the best fit
best_fit = max(r2_linear, r2_inverse, r2_quadratic)
if best_fit == r2_linear:
    best_model = "Linear"
    best_params = params_linear
elif best_fit == r2_inverse:
    best_model = "Inverse"
    best_params = params_inverse
else:
    best_model = "Quadratic"
    best_params = params_quadratic

# Step 6: Plot the data and the best fit line
plt.scatter(strain, k_L, color='green', label='Data')
if best_model == "Linear":
    plt.plot(strain, k_L_pred_linear, color='red', label=f'Linear fit: y = {best_params[0]:.4f}x + {best_params[1]:.4f}')
elif best_model == "Inverse":
    plt.plot(strain, k_L_pred_inverse, color='red', label=f'Inverse fit: y = {best_params[0]:.4f}/(x + {best_params[2]:.4f}) + {best_params[1]:.4f}')
else:
    plt.plot(strain, k_L_pred_quadratic, color='red', label=f'Quadratic fit: y = {best_params[0]:.4f}x^2 + {best_params[1]:.4f}x + {best_params[2]:.4f}')

plt.xlabel('Strain (%)')
plt.ylabel('k_L (W/mK)')
plt.legend()
plt.title(f'Best Fit: {best_model} Model')
plt.show()

# Step 7: Output the best fit equation
if best_model == "Linear":
    print(f"The best fit is a linear model: y = {best_params[0]:.4f}x + {best_params[1]:.4f}")
elif best_model == "Inverse":
    print(f"The best fit is an inverse model: y = {best_params[0]:.4f}/(x + {best_params[2]:.4f}) + {best_params[1]:.4f}")
else:
    print(f"The best fit is a quadratic model: y = {best_params[0]:.4f}x^2 + {best_params[1]:.4f}x + {best_params[2]:.4f}")
