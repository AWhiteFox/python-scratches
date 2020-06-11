import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    while True:
        try:
            ydl.download([input("Pass a link to the video: ")])
            print("Complete!", end="\n\n")
        except youtube_dl.utils.DownloadError:
            pass
