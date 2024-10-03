import cv2 as cv

# Load the image
image_path = r'C:\Users\Supravo\OneDrive\Desktop\BS\summerschool2024\sahaaysummerschool2024\deer_iitm.jpg'
image = cv.imread(image_path)

# Define larger coordinates for the green square to make it more visible
top_left = (100, 100)
bottom_right = (300, 300)

# Draw the green square
color = (0, 255, 0)  # Green color in BGR
thickness = 2
cv.rectangle(image, top_left, bottom_right, color, thickness)

# Save the image to a file for display
output_path = 'path_to_save_modified_image.jpg'
cv.imwrite(output_path, image)

# Display the image using OpenCV
cv.imshow('Modified Image', image)
cv.waitKey(0)
cv.destroyAllWindows()
