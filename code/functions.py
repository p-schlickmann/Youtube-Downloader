from __future__ import unicode_literals
import youtube_dl
from youtube_search import YoutubeSearch


def youtube_download(_id, selected_dir, user_format):
    mp3 = {
        'format': 'bestaudio/best',
        'outtmpl': f'{selected_dir}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192', }]
        }
    mp4 = {
        'format': 'bestvideo[ext=mkv]+bestaudio/best',
        'outtmpl': f'{selected_dir}/%(title)s.%(ext)s',
    }
    webm = {
        'format': 'bestvideo[ext=webm]+bestaudio',
        'outtmpl': f'{selected_dir}/%(title)s.%(ext)s'
    }
    wav = {
        'format': 'bestaudio/best',
        'outtmpl':  f'{selected_dir}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192', }]
    }
    mkv = {
        'format': 'bestvideo[ext=mp4]+bestaudio',
        'outtmpl': f'{selected_dir}/%(title)s.%(ext)s',
        'merge_output_format': 'mkv'
        }

    options = {'mp3': mp3, 'mp4': mp4, 'webm': webm, 'wav': wav, 'mkv': mkv}
    ydl_opts = options.get(user_format)

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f'https://www.youtube.com/watch?v={_id}'])
    except:
        return False
    else:
        return True


def yt_search(video_name):
    search = YoutubeSearch(video_name, max_results=10).to_dict()
    if search:
        for result in search:
            if result['id'] in video_name or result['link'] in video_name:
                search = YoutubeSearch(video_name, max_results=1).to_dict()
                return search, True
        return search, False
    return False, False
