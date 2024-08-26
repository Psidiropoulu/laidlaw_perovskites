import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('graph_image.png')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a threshold to get a binary image
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

# Find contours of the points
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize lists to store the extracted data points
points_x = []
points_y = []

# Assuming the graph is linear and the axes are well-defined
# Define your axis limits based on the image or manually
x_min, x_max = 0, 1  # example values
y_min, y_max = 0, 50  # example values

# Get the image dimensions
height, width = image.shape[:2]

# Loop through the contours to extract data points
for cnt in contours:
    # Get the center of the contour
    M = cv2.moments(cnt)
    if M['m00'] != 0:
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])

        # Convert pixel coordinates to data values
        data_x = x_min + (cx / width) * (x_max - x_min)
        data_y = y_min + ((height - cy) / height) * (y_max - y_min)

        # Store the data points
        points_x.append(data_x)
        points_y.append(data_y)

# Plot the extracted data
plt.scatter(points_x, points_y, color='red')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Extracted Data Points')
plt.show()
