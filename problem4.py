import cv2
import numpy as np

# Load the image
image_path = r'C:\Users\Supravo\OneDrive\Desktop\BS\summerschool2024\sahaaysummerschool2024\deer_iitm.jpg'  # Replace with the actual path to your image
image = cv2.imread(image_path)

# Identify the middle deer (you might need to adjust this based on your image)
middle_deer_x = image.shape[1] // 2
middle_deer_y = image.shape[0] // 2

# Define the rectangle parameters
rect_x = middle_deer_x - 50  # Adjust the rectangle size as needed
rect_y = middle_deer_y - 50
rect_width = 100
rect_height = 100

# Draw the rectangle
cv2.rectangle(image, (rect_x, rect_y), (rect_x + rect_width, rect_y + rect_height), (0, 255, 0), 2)

# Add the text "OP Deer"
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, "OP Deer", (rect_x, rect_y - 10), font, 0.5, (0, 255, 0), 2)

# Save the modified image
output_path = r'C:\Users\Supravo\OneDrive\Desktop\BS\summerschool2024'  # Replace with the desired output path
cv2.imwrite(output_path, image)

print(f"Rectangle and text added. Saved as {output_path}")

