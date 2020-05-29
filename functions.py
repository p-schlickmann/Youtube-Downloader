from __future__ import unicode_literals
import os
from time import sleep
import youtube_dl
from youtube_search import YoutubeSearch


def download_video(_id):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'/songs/{_id}%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f'https://www.youtube.com/watch?v={_id}'])
    sleep(1)

    songs = os.listdir('./songs/')
    song = [song for song in songs if song.startswith(_id)]
    old_song_name = song[0]
    new_song_name = old_song_name.replace(_id, '')

    try:
        os.rename(f'./songs/{old_song_name}', f'./songs/{new_song_name}')
    except FileExistsError:
        os.remove(f'./songs/{old_song_name}')

    return f'{new_song_name} downloaded successfully'


def yt_search(video_name):
    search = YoutubeSearch(video_name, max_results=10).to_dict()
    if search:
        return search
    return False

