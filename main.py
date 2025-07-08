import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

import pygame
import os



# Initialize app
root = tk.Tk()

root.title("MP3 Player")
root.geometry("854x480")

pygame.mixer.init()

# Create a list to hide the full directory path of the mp3 file
song_paths = []




def load_file():
    song = filedialog.askopenfilename(initialdir='audio', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))

    song_paths.append(song)  # Store full path in list
    song_box.insert(tk.END, os.path.basename(song))  # Show only filename



def play():
    song = song_box.get(tk.ACTIVE)

    index = song_box.get(0, tk.END).index(song) # Create an index
    full_path = song_paths[index] # Retrieve from the song_paths list

    pygame.mixer.music.load(full_path)
    pygame.mixer.music.play(loops=0)


def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(tk.ACTIVE)







# Buttons Image

# Declare and resize
back_button_img = Image.open("Images/back.png")  # Replace with your image path
back_button_img = back_button_img.resize((50, 50))  # Resize to fit the button
photo1 = ImageTk.PhotoImage(back_button_img)

play_button_img = Image.open("Images/play.png")
play_button_img = play_button_img.resize((50, 50))
photo2 = ImageTk.PhotoImage(play_button_img)

pause_button_img = Image.open("Images/pause.png")
pause_button_img = pause_button_img.resize((50, 50))
photo3 = ImageTk.PhotoImage(pause_button_img)

stop_button_img = Image.open("Images/stop-button.png")
stop_button_img = stop_button_img.resize((50, 50))
photo4 = ImageTk.PhotoImage(stop_button_img)

forward_button_img = Image.open("Images/next.png")
forward_button_img = forward_button_img.resize((50, 50))
photo5 = ImageTk.PhotoImage(forward_button_img)




# Creating the buttons

# Create a frame to hold buttons at the bottom-left
frame = tk.Frame(root)
frame.pack(side=tk.BOTTOM, anchor="w")


back_button = tk.Button(frame, image=photo1)
back_button.pack(side=tk.LEFT)

play_button = tk.Button(frame, image=photo2, command=play)
play_button.pack(side=tk.LEFT)

pause_button = tk.Button(frame, image=photo3)
pause_button.pack(side=tk.LEFT)

stop_button = tk.Button(frame, image=photo4, command=stop)
stop_button.pack(side=tk.LEFT)

forward_button = tk.Button(frame, image=photo5)
forward_button.pack(side=tk.LEFT)



# GUI Playlist box
song_box = tk.Listbox(root, bg="black", fg="green", height=25, width=60)
song_box.pack(side=tk.LEFT, padx=10)

album_box = tk.Listbox(root, bg="black",height=15, width=45)
album_box.pack(side=tk.RIGHT, padx=10)



#--------------------------------------------------------------------------------------



# Menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)


# Add "File" dropdown, tearoff=0 removes the dashed line of the dropdown
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Load MP3", command=load_file)






root.mainloop()