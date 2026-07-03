import pygame
import os
import time

def play_my_song():
    pygame.mixer.init()
    song_path = r"C:\Users\MY-PC\OneDrive\Desktop\Python intern\[iSongs.info] 01 - Maate Vinadhuga.mp3"
    
    if not os.path.exists(song_path):
        print("file path exists or not")
        return

    try:
        pygame.mixer.music.load(song_path)
        print("Songs enjoy!")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)
            
    except Exception as e:
        print(f"Error machan: {e}")

if __name__ == "__main__":
    play_my_song()