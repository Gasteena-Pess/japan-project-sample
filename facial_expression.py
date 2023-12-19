import cv2
from keras.models import load_model
import numpy as np

# Load the pre-trained facial expression recognition model
model = load_model('path/to/your/emotion_model.h5')

# Define the emotions labels
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Create a function to detect and analyze facial expressions
def detect_and_analyze_emotion(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml').detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Analyze each detected face
    for (x, y, w, h) in faces:
        face_roi = gray[y:y + h, x:x + w]
        face_roi = cv2.resize(face_roi, (48, 48), interpolation=cv2.INTER_AREA)
        face_roi = np.expand_dims(face_roi, axis=0)
        face_roi = np.expand_dims(face_roi, axis=-1)
        face_roi = face_roi / 255.0  # Normalize pixel values to be between 0 and 1

        # Predict the emotion using the pre-trained model
        emotion_prediction = model.predict(face_roi)[0]
        emotion_label = emotion_labels[np.argmax(emotion_prediction)]

        # Draw a rectangle and label on the image
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(image, emotion_label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Display the image with annotations
    cv2.imshow('Facial Expression Analysis', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = 'path/to/your/image.jpg'
detect_and_analyze_emotion(image_path)
