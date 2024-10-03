import cv2 as cv
capture = cv.VideoCapture('forest.mp4')
def rescale(frame, scale=0.8):
    # Images, Videos and Live Videos
    width = int(frame.shape[1] * scale)  # reduce the width of the frame or image
    height = int(frame.shape[0] * scale)  # reduce the height of the frame or image
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('forest.mp4')
while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break
    rescale_frame = rescale(frame)
    cv.imshow('Video', rescale_frame)
    
    if cv.waitKey(20) & 0xFF == ord('i'):
        break
capture.release()
cv.destroyAllWindows()
   