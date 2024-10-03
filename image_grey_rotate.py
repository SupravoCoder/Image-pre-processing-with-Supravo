import cv2 as cv
import numpy as np

# Load the image
image_path = r'C:\Users\Supravo\OneDrive\Desktop\BS\summerschool2024\sahaaysummerschool2024\deer_iitm.jpg'  # Update this with the path to your image
image = cv.imread(image_path)

# Convert the image to grayscale
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Function to rotate an image
def rotate_image(image, angle):
    height, width = image.shape[:2]
    center = (width // 2, height // 2)
    rotation_matrix = cv.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image

# Rotate the image by 60 degrees anticlockwise
rotated_60 = rotate_image(gray_image, 60)

# Rotate the 60 degrees rotated image by another 70 degrees anticlockwise
rotated_130 = rotate_image(rotated_60, 70)

# Rotate the original grayscale image by 110 degrees anticlockwise
rotated_110 = rotate_image(gray_image, 110)

# Concatenate the images horizontally for comparison
combined_image = np.hstack((rotated_60, rotated_130, rotated_110))

# Save the combined image for display
output_path = 'path_to_save_combined_image.jpg'  # Update this with your desired path
cv.imwrite(output_path, combined_image)

# Display the image using OpenCV
cv.imshow('Rotated Images', combined_image)
cv.waitKey(0)
cv.destroyAllWindows()
