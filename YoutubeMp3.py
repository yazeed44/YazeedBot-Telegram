import youtube_dl
from os import listdir
from os import getcwd
from os import remove
from os.path import isfile, join


class MyLogger():
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    pass


def youtube_mp3(updater, context):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': MyLogger(),
    }
    # TODO specify readable file name

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(context.args)
        for filePath in listdir(getcwd()):
            if isfile(filePath) and filePath.endswith(".mp3"):
                context.bot.send_audio(chat_id=updater.message.chat_id, audio=open(filePath, 'rb'), timeout=1000)
                remove(filePath)
