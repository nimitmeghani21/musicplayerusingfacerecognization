import pygame
import os
import time

# Initialize pygame mixer
pygame.mixer.init()

# Function to test music playback
def test_music_playback(music_file):
    if os.path.exists(music_file):
        print(f"Playing: {music_file}")
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()
        time.sleep(5)  # Play for 5 seconds
        pygame.mixer.music.stop()
    else:
        print("Music file not found!")

# Test with happy music
test_music_playback("happy_music.mp3")  # Ensure this file exists
