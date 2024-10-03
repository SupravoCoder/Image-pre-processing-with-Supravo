import cv2
import numpy as np

# Load the image
image_path = 'istockphoto-1164386039-1024x1024.jpg'  # Replace with your image path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded properly
if image is None:
    print("Error: Could not load image.")
    exit()

# Apply a binary threshold to the image
threshold_value = 127
max_value = 255
_, thresholded_image = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_BINARY)

# Save the thresholded image
output_path = 'thresholded_howrah_bridge.jpg'
cv2.imwrite(output_path, thresholded_image)

# Display the original and thresholded images
cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()