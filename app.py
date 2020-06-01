import tkinter as tk
from tkinter import ttk
import webbrowser
from random import randint
from functions import download_video
from time import sleep


root = tk.Tk()
style = ttk.Style()
root.title('YOUTUBE MP3 DOWNLOADER')
root.geometry("690x550")

user_search = tk.StringVar()

previous_widgets = []
waiting_download = []

test = [[{'title': 'miadama', 'link': 'watch?v=82ry389rhfnnnfvi', 'id': '82ry389rhfnnnfvi'},
         {'title': 'miadama', 'link': 'watch?v=82ry389rhfnnnfvi', 'id': '82ry389rhfnnnfvi'},
         {'title': 'miadama', 'link': 'watch?v=82ry389rhfnnnfvi', 'id': '82ry389rhfnnnfvi'},
         {'title': 'miadama', 'link': 'watch?v=82ry389rhfnnnfvi', 'id': '82ry389rhfnnnfvi'},
         {'title': 'miadama', 'link': 'watch?v=82ry389rhfnnnfvi', 'id': '82ry389rhfnnnfvi'},
         {'title': 'miadama', 'link': 'watch?v=82ry389rhfnnnfvi', 'id': '82ry389rhfnnnfvi'},
         {'title': 'miadama', 'link': 'watch?v=82ry389rhfnnnfvi', 'id': '82ry389rhfnnnfvi'},
         {'title': 'miadama', 'link': 'watch?v=82ry389rhfnnnfvi', 'id': '82ry389rhfnnnfvi'},
         {'title': 'miadama', 'link': 'watch?v=82ry389rhfnnnfvi', 'id': '82ry389rhfnnnfvi'},
         {'title': 'miadama', 'link': 'watch?v=82ry389rhfnnnfvi', 'id': '82ry389rhfnnnfvi'}]
    , [{'title': 'cu', 'link': 'watch?v=82ry389rhfnnnfvi', 'id': '82ry389rhfnnnfvi'},
       {'title': 'cu', 'link': 'watch?v=82ry389rhfnnnfvi', 'id': '82ry389rhfnnnfvi'},
       {'title': 'cu', 'link': 'watch?v=82ry389rhfnnnfvi', 'id': '82ry389rhfnnnfvi'},
       {'title': 'cu', 'link': 'watch?v=82ry389rhfnnnfvi', 'id': '82ry389rhfnnnfvi'},
       {'title': 'cu', 'link': 'watch?v=82ry389rhfnnnfvi', 'id': '82ry389rhfnnnfvi'},
       {'title': 'cu', 'link': 'watch?v=82ry389rhfnnnfvi', 'id': '82ry389rhfnnnfvi'},
       {'title': 'cu', 'link': 'watch?v=82ry389rhfnnnfvi', 'id': '82ry389rhfnnnfvi'},
       {'title': 'cu', 'link': 'watch?v=82ry389rhfnnnfvi', 'id': '82ry389rhfnnnfvi'},
       {'title': 'cu', 'link': 'watch?v=82ry389rhfnnnfvi', 'id': '82ry389rhfnnnfvi'},
       {'title': 'cu', 'link': 'watch?v=82ry389rhfnnnfvi', 'id': '82ry389rhfnnnfvi'}, ]]


def add_download(_id, name, len):
    print(waiting_download)
    downloading_widget = ttk.Label(root, text=f"downloading {name} ...", padding=3)
    downloading_widget.grid(row=len + 1, column=1, ipady=7, ipadx=11, padx=3, pady=2, columnspan=3)
    waiting_download.append({'name': name, 'id': _id, 'len': len})
    root.command(download())


def download():
    sleep(5)
    if waiting_download:
        download = waiting_download[0]
        was_sucessful = True  # download_video(download['id'])
        if was_sucessful:
            failed = ttk.Label(root, text=f"{download['name']} was downloaded sucessfully", padding=3)
            failed.grid(row=download['len'] + 1, column=1, ipady=7, ipadx=11, padx=3, pady=2, columnspan=3)
        else:
            failed = ttk.Label(root, text=f"{download['name']} could not be downloaded", padding=3)
            failed.grid(row=download['len'] + 1, column=1, ipady=7, ipadx=11, padx=3, pady=2, columnspan=3)

        waiting_download.remove(download)


def clear():
    for widget in previous_widgets:
        widget.grid_forget()


def show_results():
    clear()
    results = test[0]
    if results:
        for num, result in enumerate(results):
            num = num + 1

            widget = ttk.Label(root, text=result['title'], width=60, borderwidth=7, padding=3, relief='groove')
            watch_button = ttk.Button(root, text="Watch the video", width=17, command=lambda: print('hello watch'))
            download_button = ttk.Button(root, text='Download', width=15,
                                         command=lambda: add_download(result['id'], result['title'], len(results)))
            widget.grid(row=num, column=0, ipady=7, ipadx=11, padx=3, pady=2, columnspan=3)
            watch_button.grid(row=num, column=3, ipady=7, ipadx=11, padx=3, pady=2)
            download_button.grid(row=num, column=4, ipady=7, ipadx=11, padx=3, pady=2)

            previous_widgets.append(widget)
            previous_widgets.append(watch_button)
            previous_widgets.append(download_button)
    else:
        ttk.Label(root, text='no results found').grid(row=1, column=0, columnspan=3)


ttk.Label(root, width=13, text='Video Name: ', padding=7).grid(row=0, column=0, ipady=5, padx=1, pady=3)

ttk.Entry(root, width=30, textvariable=user_search).grid(row=0, column=1, ipady=5, padx=1, pady=3)

ttk.Button(root, text='Search', width=16, command=show_results).grid(row=0, column=2, ipady=5, padx=9, pady=3)


root.mainloop()
print('oi')
