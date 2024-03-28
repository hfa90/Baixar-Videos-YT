import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
import instaloader

def download_video():
    youtube_url = youtube_url_entry.get()
    instagram_url = instagram_url_entry.get()
    download_path = filedialog.askdirectory()

    try:
        if youtube_url:
            yt = YouTube(youtube_url)
            video = yt.streams.get_highest_resolution()
            video.download(download_path)
            status_label.config(text="Download do vídeo do YouTube completo!")
        if instagram_url:
            loader = instaloader.Instaloader()
            loader.download_post(instagram_url, target=download_path)
            status_label.config(text="Download do post do Instagram completo!")
    except Exception as e:
        status_label.config(text=f"Ocorreu um erro durante o download: {str(e)}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Download de Vídeos do YouTube e do Instagram")

youtube_url_label = tk.Label(root, text="Insira o URL do vídeo do YouTube:")
youtube_url_label.pack()

youtube_url_entry = tk.Entry(root, width=50)
youtube_url_entry.pack()

instagram_url_label = tk.Label(root, text="Insira o URL do post do Instagram:")
instagram_url_label.pack()

instagram_url_entry = tk.Entry(root, width=50)
instagram_url_entry.pack()

download_button = tk.Button(root, text="Baixar Vídeos", command=download_video)
download_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
