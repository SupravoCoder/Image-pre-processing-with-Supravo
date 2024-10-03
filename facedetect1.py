import cv2 as cv
import numpy as np
import os

# Initialize webcam
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Load the pre-trained Haar Cascade for face detection
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

if face_cascade.empty():
    print("Error: Could not load face detector.")
    exit()

# Initialize the face recognizer
recognizer = cv.face.LBPHFaceRecognizer_create()

# Load training data
face_data_dir = 'faces'
labels = []
faces_data = []
label_to_name = {}
label_counter = 0

for subdir, dirs, files in os.walk(face_data_dir):
    for file in files:
        if file.endswith('.jpg') or file.endswith('.png'):
            path = os.path.join(subdir, file)
            label = os.path.basename(subdir)
            img = cv.imread(path, cv.IMREAD_GRAYSCALE)
            if img is None:
                continue
            faces_data.append(img)
            if label not in label_to_name:
                label_to_name[label] = label_counter
                labels.append(label_counter)
                label_counter += 1
            else:
                labels.append(label_to_name[label])

recognizer.train(faces_data, np.array(labels))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(roi_gray)
        name = [name for name, label_id in label_to_name.items() if label_id == label][0]
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv.putText(frame, f'{name} ({confidence:.2f})', (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    cv.imshow('Face Recognition', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
