import cv2 as cv
import numpy as np

# Load the image
image_path = r'C:\Users\Supravo\OneDrive\Desktop\BS\summerschool2024\sahaaysummerschool2024\deer_iitm.jpg'  # Replace with the path to your image
image = cv.imread(image_path)

# Convert the image to grayscale
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv.Canny(gray_image, 100, 200)  # Adjust thresholds if necessary

# Create a kernel for dilation
kernel = np.ones((3, 3), np.uint8)  # You can try different sizes

# Dilate the edges
dilated_edges = cv.dilate(edges, kernel, iterations=1)

# Save the processed images
cv.imwrite('path_to_save_canny.jpg', edges)  # Replace with your save path
cv.imwrite('path_to_save_dilated.jpg', dilated_edges)  # Replace with your save path

# Display the images using OpenCV
cv.imshow('Canny Edges', edges)
cv.imshow('Dilated Edges', dilated_edges)
cv.waitKey(0)
cv.destroyAllWindows()
