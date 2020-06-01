import tkinter as tk
from tkinter import ttk, filedialog
import webbrowser

from main_functions import youtube_download, yt_search


root = tk.Tk()
root.title('YOUTUBE DOWNLOADER')
root.geometry("710x515")

user_search = tk.StringVar()
user_format_option = tk.StringVar()
link_or_name = tk.StringVar()
previous_widgets = []
previous_bottom_widgets = []


def download(_id, name, len):
    clear_messages()
    path = set_directory()
    file_format = set_file_format()
    was_successful = youtube_download(_id, path, file_format)
    if was_successful:
        downloading_widget = ttk.Label(root, text=f"{name} was downloaded successfully", padding=3)
        downloading_widget.grid(row=len + 1, column=1, ipady=7, ipadx=11, padx=3, pady=2, columnspan=3)

    else:
        downloading_widget = ttk.Label(root, text=f"error downloading {name}", padding=3)
        downloading_widget.grid(row=len + 1, column=1, ipady=7, ipadx=11, padx=3, pady=2, columnspan=3)

    previous_bottom_widgets.append(downloading_widget)


def clear_search():
    for widget in previous_widgets:
        widget.grid_remove()


def clear_messages():
    for previous in previous_bottom_widgets:
        previous.grid_remove()


def check_conditions():
    _, searched_link = yt_search(user_search.get())
    search_by_name = set_search_option()

    if search_by_name == 'select a searching option!':
        error_widget = ttk.Label(root, text='select a searching option!', padding=3)
        error_widget.grid(row=1, column=1, ipady=7, ipadx=11, padx=3, pady=2, columnspan=3)
        previous_bottom_widgets.append(error_widget)
        return False
    if searched_link and search_by_name:
        error_widget = ttk.Label(root, text='you used a link while searching by name', padding=3)
        error_widget.grid(row=1, column=1, ipady=7, ipadx=11, padx=3, pady=2, columnspan=3)
        previous_bottom_widgets.append(error_widget)
        return False
    elif not searched_link and not search_by_name:
        error_widget = ttk.Label(root, text='you used a name while searching by link', padding=3)
        error_widget.grid(row=1, column=1, ipady=7, ipadx=11, padx=3, pady=2, columnspan=3)
        previous_bottom_widgets.append(error_widget)
        return False
    else:
        return True


def show_results(event):
    clear_search()
    clear_messages()
    searching_conditions_are_ok = check_conditions()
    if searching_conditions_are_ok:
        results, _ = yt_search(user_search.get())
        if results:
            for num, result in enumerate(results):
                num = num + 1

                widget = ttk.Label(root, text=result['title'], width=63, borderwidth=7, padding=3, relief='groove')
                watch_button = ttk.Button(root, text="Watch the video", width=17,
                                          command=lambda x=result: webbrowser.open(f'https://www.youtube.com/watch?v={x["id"]}'))
                download_button = ttk.Button(root, text='Download', width=15,
                                             command=lambda x=result: download(x['id'], x['title'], len(results)))

                widget.grid(row=num, column=0, ipady=7, ipadx=11, padx=3, pady=2, columnspan=3)
                watch_button.grid(row=num, column=3, ipady=7, ipadx=11, padx=3, pady=2)
                download_button.grid(row=num, column=4, ipady=7, ipadx=11, padx=3, pady=2)

                previous_widgets.append(widget)
                previous_widgets.append(watch_button)
                previous_widgets.append(download_button)
        else:
            ttk.Label(root, text='no results found').grid(row=1, column=0, columnspan=3)


def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        with open('previous_path.txt', 'w') as f:
            f.write(directory)


def set_directory():
    with open('previous_path.txt', 'r') as f:
        previous_path = f.read()
        if previous_path:  # if there is a previous path selected, use it
            path = tk.StringVar()
            path.set(previous_path)
            return path.get()
        else:  # if not, set to root
            path = tk.StringVar()
            path.set('./songs')
            return path.get()


def set_file_format():
    if user_format_option.get() == 'Select format...':
        file_format = tk.StringVar()
        file_format.set('webm')
        return file_format.get()
    return user_format_option.get()


def set_search_option():
    if link_or_name.get() == 'Search by...':
        return 'select a searching option!'
    elif link_or_name.get() == 'Video Name':
        return True
    return False


search_options = ttk.OptionMenu(root, link_or_name, 'Search by...', 'Video Name', 'Video Link')
search_options.grid(row=0, column=0, ipady=5, padx=9, pady=3)
search_options.config(width=11)

search = ttk.Entry(root, width=30, textvariable=user_search)
search.grid(row=0, column=1, ipady=5, padx=1, pady=3)
search.focus()
root.bind('<Return>', show_results)

ttk.Button(root, text='Search', width=16, command=lambda: show_results('')).grid(row=0, column=2, ipady=5, padx=9, pady=3)

format_options = ttk.OptionMenu(root, user_format_option, 'Select format...', 'webm', 'mp4', 'mkv', '---------', 'mp3', 'wav')
format_options.grid(row=0, column=3, ipady=5, padx=7, pady=3)
format_options.config(width=13)

ttk.Button(root, text='Downloads directory', width=19, command=browse_directory).grid(row=0, column=4, ipady=5, padx=9, pady=3)


root.mainloop()   
   
