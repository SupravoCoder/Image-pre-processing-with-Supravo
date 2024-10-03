import cv2 as cv

# Load the Haar Cascade Classifier for face detection
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open a connection to the webcam (0 is the default camera)
video_capture = cv.VideoCapture(0)

# Check if the webcam is opened successfully
if not video_capture.isOpened():
    print("Error: Could not open video device.")
    exit()

# Set the webcam resolution (optional)
video_capture.set(cv.CAP_PROP_FRAME_WIDTH, 640)
video_capture.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

# Loop to continuously get frames from the webcam
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert the frame to grayscale (Haar Cascade works with grayscale images)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw a rectangle around each detected face
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the resulting frame
    cv.imshow('Real-Time Face Detection', frame)

    # Break the loop if the user presses the 'q' key
    if cv.waitKey(1) & 0xFF == ord('s'):
        break

# Release the capture and close any OpenCV windows
video_capture.release()
cv.destroyAllWindows()
