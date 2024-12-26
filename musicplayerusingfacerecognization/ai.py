import cv2
import numpy as np
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Load pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to play music based on mood
def play_music(mood):
    # Stop any currently playing music
    pygame.mixer.music.stop()

    # Load music files based on detected mood
    if mood == "happy":
        music_file = "happy_music.mp3"  # Replace with your happy music file path
    elif mood == "sad":
        music_file = "sad_music.mp3"  # Replace with your sad music file path
    else:
        return  # If mood is not recognized, do nothing

    # Play the corresponding music
    if os.path.exists(music_file):
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1)  # Play indefinitely until stopped

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Determine mood based on face detection
    mood = "happy" if len(faces) > 0 else "sad"

    # Play music based on detected mood
    play_music(mood)

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the frame
    cv2.imshow('Mood Detection Music Player', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
pygame.mixer.music.stop()
