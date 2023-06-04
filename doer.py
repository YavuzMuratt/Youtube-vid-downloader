import tkinter as tk
from tkinter import ttk, messagebox
from yt_dlp import YoutubeDL as ydl


def download(url):
    try:
        # Initialize the YouTube downloader with output template
        yt = ydl({"outtmpl": "videos/%(title)s.%(ext)s"})
        yt.download([url])

        # Show a success message box
        messagebox.showinfo("Download Complete", "Your video has been downloaded\n")

    except Exception as e:
        # Show an error message box
        messagebox.showerror("Error", e)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configure the main window
        self.title("My YouTube Video Downloader")
        self.resizable(False, False)
        self.iconbitmap("icon.ico")
        self.geometry("400x200")
        self.configure(bg="#3f586f")

        # Create and configure the message label
        msg = tk.Label(self, text="Paste your YouTube link below:")
        msg.configure(font=("Arial", 15))
        msg.configure(bg="#3f586f", fg="#e44647")
        msg.pack(expand=True)

        # Create and configure the URL input field
        url_input = ttk.Entry(self)
        url_input.configure(width=50)
        url_input.pack(expand=True)

        # Create and configure the download button
        d_button = ttk.Button(self, text="Download", command=lambda: download(url_input.get()))
        d_button.configure(width=10)
        d_button.pack(expand=True)

        self.mainloop()


def main():
    # Create an instance of the App class and start the application
    app = App()
    return app


if __name__ == "__main__":
    main()
