import cv2 as cv
# Load an image
img = cv.imread(r'C:\Users\Supravo\OneDrive\Desktop\BS\summerschool2024\sahaaysummerschool2024\Screenshot 2022-10-21 170657.png')
# Display the image in a window
cv.imshow('beach', img)

def rescale(frame, scale =0.8):
    # Images, Videos and Live Videos 
    width = int(frame.shape[1] * scale)#this is used for reducing the width of the frame or the image
    height = int(frame.shape[0] * scale)# this is  used for reducing the  of the frame or the image
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)
rescaled_img = rescale(img)
cv.imshow("Rescaled",rescaled_img)
cv.waitKey(0)
# Wait for a key press to close the window
