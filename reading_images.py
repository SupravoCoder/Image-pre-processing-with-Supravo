import cv2 as cv

#img = cv.imread(r'C:\Users\Supravo\OneDrive\Desktop\BS\summerschool2024\sahaaysummerschool2024\deer.jpg')
#cv.imshow('IITMdeer', img)

#cv.waitKey(0)
# Initialize a video capture object for the default camera (0).
capture = cv.VideoCapture('forest.mp4')

# Start an infinite loop to continuously capture frames from the camera.
while True:
    # Capture the current frame.
    # isTrue will be True if the frame was successfully captured.
    # frame contains the captured frame.
    isTrue, frame = capture.read()
    
    # Display the captured frame in a window named 'Video'.
    cv.imshow('Video', frame)
    
    # Wait for 20 milliseconds for a key press.
    # If the 'd' key is pressed, exit the loop.
    if cv.waitKey(20) & 0xFF==ord('d'): 
        break

# Release the capture object, freeing up the camera.
capture.release()

# Close all OpenCV windows.
cv.destroyAllWindows() 