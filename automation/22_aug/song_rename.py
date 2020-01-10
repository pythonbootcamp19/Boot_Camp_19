import os

target_ext = ".txt"

def get_all_song_names():

    list_of_files = os.listdir()
    song_names = []
    for filename in list_of_files:
        if filename[-4:] == target_ext:    
            song_names.append(filename)
    return song_names

song_names = get_all_song_names()
print(song_names[1])