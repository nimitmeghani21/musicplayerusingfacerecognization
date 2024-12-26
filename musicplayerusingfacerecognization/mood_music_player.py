import cv2
import pygame
import os
import threading


pygame.mixer.init(frequency=44100, size=-16, channels=2)


pygame.mixer.music.set_volume(0.5)  # Set volume between 0.0 and 1.0


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


def play_music(mood):
    music_file = None

    if mood == "happy":
        music_file = "happy_music.mp3"  
    elif mood == "sad":
        music_file = "sad_music.mp3"  

    if music_file and os.path.exists(music_file):
        print(f"Detected mood: {mood}. Playing music: {music_file}")
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1)  
    else:
        print(f"Music file not found: {music_file}")  


cap = cv2.VideoCapture(0)
current_mood = None

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    
    new_mood = "happy" if len(faces) > 0 else "sad"

    if new_mood != current_mood:
        current_mood = new_mood
        
        pygame.mixer.music.stop() 
        
        music_thread = threading.Thread(target=play_music, args=(current_mood,))
        music_thread.start()

    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    
    cv2.imshow('Mood Detection Music Player', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit if 'q' is pressed
        break


cap.release()
cv2.destroyAllWindows()
pygame.mixer.music.stop()
