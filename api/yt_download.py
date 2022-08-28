from pytube import YouTube

def download_video(url:str):
    video = YouTube(url)
    name = f"{video.title}.mp4"

    v = video.streams.get_audio_only(subtype= 'mp4')
    print(video.streams.filter(only_audio=True))
    v.download(filename=name,  output_path='./app/assets/')
    return name
