from pytube import YouTube

def baixarAudio50(url):

    audio_url = url.format('')

    yt = YouTube(audio_url)

    return yt.streams.filter(only_audio=True, abr='50kbps').first().download()


baixarAudio50('https://www.youtube.com/watch?v=ZqMh3Icy-L8')