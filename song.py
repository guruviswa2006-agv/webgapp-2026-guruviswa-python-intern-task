import pygame
import time

def play_song(C:\Users\MY-PC\OneDrive\Desktop\Python intern):
    # Pygame mixer-a initialize panrom
    pygame.mixer.init()
    
    # Audio file-a load panrom (mp3 or wav file)
    pygame.mixer.music.load(file_path)
    
    # Paatu paada start pannudhu!
    print("Machan, paatu paaditu iruku... Kélu!")
    pygame.mixer.music.play()
    
    # Paatu mudiyura varaikum program close aagama iruka indha loop
    while pygame.mixer.music.get_busy():
        time.sleep(1) # 1 second wait பண்ணி check பண்ணும்

# Unoda paatu file path-a inga kudu
# Example: 'en_paatu.mp3' or 'C:/Music/song.mp3'
song_file = "[iSongs.info] 01 - Maate Vinadhuga.mp3" 
play_song([iSongs.info] 01 - Maate Vinadhuga)