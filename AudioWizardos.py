import os
import tkinter as tk
from tkinter import filedialog
import subprocess

try:
    import moviepy
except ImportError:
    print("Installation de la bibliothèque moviepy...")
    subprocess.check_call(["pip", "install", "moviepy"])

root = tk.Tk()
root.title("Convertisseur MP4 en MP3")
root.config(bg="#121212")

label = tk.Label(root, text="Cliquez sur le bouton pour sélectionner un fichier MP4", fg="#ffffff", bg="#121212", font=("Arial", 14))
label.pack(pady=20)

def select_file():
    file_path = filedialog.askopenfilename(title="Sélectionnez un fichier MP4", filetypes=(("Fichiers MP4", "*.mp4"),))
    if file_path:
        convert_to_mp3(file_path)

def convert_to_mp3(file_path):
    mp4_file = moviepy.editor.VideoFileClip(file_path)
    mp3_file = os.path.splitext(file_path)[0] + ".mp3"
    mp4_file.audio.write_audiofile(mp3_file)
    label.config(text=f"Le fichier MP3 a été créé à l'emplacement suivant: {mp3_file}")

select_button = tk.Button(root, text="Sélectionner un fichier MP4", fg="#ffffff", bg="#262626", font=("Arial", 12), command=select_file)
select_button.pack(pady=10)

root.mainloop()
