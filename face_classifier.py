import cv2

# Load the face cascade classifier
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initialize the camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Read frame from the camera
    ret, frame = cap.read()
    
    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

    # Display the frame with detected faces
    cv2.imshow('Faces', frame)

    # Check for the 'Enter' key press
    if cv2.waitKey(1) == 13:
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
