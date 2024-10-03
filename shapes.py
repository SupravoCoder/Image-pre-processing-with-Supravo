import cv2 as cv  # Import the OpenCV library as cv
import numpy as np  # Import the NumPy library as np

# Create a blank image with dimensions 720x720 and 3 color channels (RGB)
blank = np.zeros((100, 100, 3), dtype='uint8')

# Display the blank image
cv.imshow('Blank', blank)

# Set a specific region of the blank image to the color (255, 120, 150)
blank[0:100, 100:225] = 255, 120, 150

# Display the modified image
cv.imshow('Blank1', blank)

cv.rectangle(blank,(0,0),(300,300),())

# Wait for a key press to close the window
cv.waitKey(0)