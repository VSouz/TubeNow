import os
from pytube import YouTube
from app import app
from moviepy.editor import *
import shutil

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def details(url):

    linkDetails = url.format('')

    yt = YouTube(linkDetails)

    streamFast = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    streamBest = yt.streams.filter(only_video=True, file_extension='mp4').first()

    fileFast = str(streamFast.filesize_mb)[:-2] + " Mb"
    fileBest = str(streamBest.filesize_mb)[:-2] + " Mb"
    duration = convert_seconds(yt.length)

    audio70 = yt.streams.filter(only_audio=True, abr='70kbps').first()
    audio70size = str(audio70.filesize_mb)[:-1] + " Mb"

    audio128 = yt.streams.filter(only_audio=True, abr='128kbps').first()
    audio128size = str(audio128.filesize_mb)[:-1] + " Mb"

    audio160 = yt.streams.filter(only_audio=True, abr='160kbps').first()
    audio160size = str(audio160.filesize_mb)[:-1] + " Mb"
    
    audio50 = yt.streams.filter(only_audio=True, abr='50kbps').first()
    audio50size = str(audio50.filesize_mb)[:-1] + " Mb"

    info = {"img": yt.thumbnail_url, "title": yt.title, "SizeFast": fileFast, "SizeBest": fileBest, "duration": duration , "url": linkDetails
            , "audio70": audio70size, "audio128": audio128size, "audio160": audio160size, "audio50":audio50size}

    return info


def baixarVideoBest(url):
    video_url = url.format('')
    # Cria um objeto YouTube
    yt = YouTube(video_url)

    pasta = 'videos'

    if os.path.isdir(pasta):
        shutil.rmtree(pasta)

    os.mkdir("videos")  

    # Seleciona a stream de vídeo em 1440p
    video_stream = yt.streams.filter(only_video=True, mime_type="video/mp4").first()

    # Seleciona a stream de áudio
    audio_stream = yt.streams.filter(only_audio=True, abr='160kbps').first()

    # Define os caminhos temporários onde o vídeo e o áudio serão salvos
    video_temp_path = 'videos/temp_video.mp4'
    audio_temp_path = 'videos/temp_audio.mp4'

    # Define os caminhos finais dos arquivos
    video_path = 'videos/video.mp4'
    audio_path = 'videos/audio.mp4'

    # Baixa o vídeo e o áudio
    video_stream.download(filename=video_temp_path)
    audio_stream.download(filename=audio_temp_path)

    # Renomeia os arquivos temporários para os caminhos finais
    os.rename(video_temp_path, video_path)
    os.rename(audio_temp_path, audio_path)

    # Combina o vídeo e o áudio usando moviepy
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    # Adiciona o áudio ao vídeo
    final_clip = video_clip.set_audio(audio_clip)

    # Define o caminho do arquivo final
    final_path = 'videos\final_video.mp4'

    # Salva o vídeo final com áudio
    final_clip.write_videofile(final_path, codec='libx264')   
    
    video_clip.close()
    audio_clip.close()
    final_clip.close()

    return final_path

def baixarVideo(url):
    video_url = url.format('')
    
    yt = YouTube(video_url)

    return yt.streams.filter(progressive=True).first().download()


def baixarAudio70(url):

    audio_url = url.format('')

    yt = YouTube(audio_url)

    return yt.streams.filter(only_audio=True, file_extension='mp4', abr='70kbps').first().download()


def baixarAudio128(url):

    audio_url = url.format('')

    yt = YouTube(audio_url)

    return yt.streams.filter(only_audio=True, abr='128kbps').first().download()


def baixarAudio160(url):

    audio_url = url.format('')

    yt = YouTube(audio_url)

    return yt.streams.filter(only_audio=True, abr='160kbps').first().download()


def baixarAudio50(url):

    audio_url = url.format('')

    yt = YouTube(audio_url)

    return yt.streams.filter(only_audio=True, abr='50kbps').first().download()

# import os
# import shutil
# from pytube import YouTube
# from pytube import Playlist  # Importe Playlist se você planeja lidar com playlists do YouTube
# from moviepy.editor import *


# def convert_seconds(seconds):
#     hours = seconds // 3600
#     minutes = (seconds % 3600) // 60
#     seconds = seconds % 60
#     return f"{hours:02}:{minutes:02}:{seconds:02}"


# def details(url):
#     yt = YouTube(url)

#     streamFast = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
#     streamBest = yt.streams.get_highest_resolution()

#     fileFast = f"{streamFast.filesize // (1024 * 1024)} Mb" if streamFast else "N/A"
#     fileBest = f"{streamBest.filesize // (1024 * 1024)} Mb" if streamBest else "N/A"
#     duration = convert_seconds(yt.length)

#     audio70 = yt.streams.filter(only_audio=True, abr='70kbps').first()
#     audio70size = f"{audio70.filesize // (1024 * 1024)} Mb" if audio70 else "N/A"

#     audio128 = yt.streams.filter(only_audio=True, abr='128kbps').first()
#     audio128size = f"{audio128.filesize // (1024 * 1024)} Mb" if audio128 else "N/A"

#     audio160 = yt.streams.filter(only_audio=True, abr='160kbps').first()
#     audio160size = f"{audio160.filesize // (1024 * 1024)} Mb" if audio160 else "N/A"

#     audio50 = yt.streams.filter(only_audio=True, abr='50kbps').first()
#     audio50size = f"{audio50.filesize // (1024 * 1024)} Mb" if audio50 else "N/A"

#     info = {
#         "img": yt.thumbnail_url,
#         "title": yt.title,
#         "SizeFast": fileFast,
#         "SizeBest": fileBest,
#         "duration": duration,
#         "url": url,
#         "audio70": audio70size,
#         "audio128": audio128size,
#         "audio160": audio160size,
#         "audio50": audio50size
#     }

#     return info


# def baixarVideoBest(url):
#     yt = YouTube(url)

#     pasta = 'videos'

#     if os.path.isdir(pasta):
#         shutil.rmtree(pasta)

#     os.mkdir("videos")

#     video_stream = yt.streams.filter(only_video=True, file_extension="mp4").first()
#     audio_stream = yt.streams.filter(only_audio=True, abr='160kbps').first()

#     video_temp_path = 'videos/temp_video.mp4'
#     audio_temp_path = 'videos/temp_audio.mp4'

#     video_stream.download(output_path='videos', filename='temp_video')
#     audio_stream.download(output_path='videos', filename='temp_audio')

#     video_path = 'videos/video.mp4'
#     audio_path = 'videos/audio.mp4'

#     os.rename(video_temp_path, video_path)
#     os.rename(audio_temp_path, audio_path)

#     video_clip = VideoFileClip(video_path)
#     audio_clip = AudioFileClip(audio_path)

#     final_clip = video_clip.set_audio(audio_clip)

#     final_path = 'videos/final_video.mp4'

#     final_clip.write_videofile(final_path, codec='libx264')

#     video_clip.close()
#     audio_clip.close()
#     final_clip.close()

#     return final_path


# def baixarVideo(url):
#     yt = YouTube(url)
#     video_stream = yt.streams.get_highest_resolution()
#     return video_stream.download()


# def baixarAudio70(url):
#     yt = YouTube(url)
#     audio_stream = yt.streams.filter(only_audio=True, abr='70kbps').first()
#     return audio_stream.download()


# def baixarAudio128(url):
#     yt = YouTube(url)
#     audio_stream = yt.streams.filter(only_audio=True, abr='128kbps').first()
#     return audio_stream.download()


# def baixarAudio160(url):
#     yt = YouTube(url)
#     audio_stream = yt.streams.filter(only_audio=True, abr='160kbps').first()
#     return audio_stream.download()


# def baixarAudio50(url):
#     yt = YouTube(url)
#     audio_stream = yt.streams.filter(only_audio=True, abr='50kbps').first()
#     return audio_stream.download()
