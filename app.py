import tkinter as tk
from tkinter import ttk, W, E, N, S
from functions import yt_search, download_video


root = tk.Tk()
style = ttk.Style()
root.title('YOUTUBE MP3 DOWNLOADER')
root.geometry("600x500")

user_search = tk.StringVar()

previous_widgets = []


def clear():
    for widget in previous_widgets:
        widget.grid_forget()


def show_results():
    clear()
    results = yt_search(user_search.get())
    if results:
        for num, result in enumerate(results):
            widget = ttk.Label(root, text=result['title'], width=60, borderwidth=7, padding=5, relief='groove')
            download_button = ttk.Button(root, text='Download', width=10, command=lambda: download_video(result['id']))
            widget.grid(row=num, column=0)
            download_button.grid(row=num, column=1)
            previous_widgets.append(widget)
            previous_widgets.append(download_button)
    else:
        ttk.Label(root, text='no results found').pack(side='top')


frame = tk.Frame(root, bg="green", height=100, width=200).pack(side='top')

ttk.Label(frame, text='Video Name: ').pack()

ttk.Entry(frame, width=30, textvariable=user_search).pack()

ttk.Button(frame, text='Search', width=10, command=show_results).pack()

root.mainloop()
