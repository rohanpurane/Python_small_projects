# ************ If we want to download video and audio only ************#

'''
from pytube import YouTube

link = 'https://youtube.com/shorts/gRpkNT2hSfA?feature=share'
youtube_1 = YouTube(link)

print('================================')
print()
print(youtube_1.title)
print(youtube_1.thumbnail_url)
video = youtube_1.streams.all()
vid = list(enumerate(video))
for i in vid:
    print(i)

print()
strm = int(input("Enter : ")) # Input is "2" to choose the number of resolution of video for example =>
#(2, <Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">)
#This is For Video and Audio
video[strm].download()
print('Done')
'''



# ************ If we want to download audio only ************#

'''
from pytube import YouTube

link = 'https://youtube.com/shorts/gRpkNT2hSfA?feature=share'
youtube_1 = YouTube(link)

print('================================')
print()
print(youtube_1.title)
print(youtube_1.thumbnail_url)
# video = youtube_1.streams.all() # for audio we don't need this
audio = youtube_1.streams.filter(only_audio=True)
vid = list(enumerate(audio))
for i in vid:
    print(i)

print()
strm = int(input("Enter : ")) # Input is "3" to choose the number of resolution of video for example =>
(3, <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">)
#This is For Audio
audio[strm].download()
print('Done')
'''


# ************ If we want to download Plyalist ************#

from pytube import Playlist

py = Playlist('https://youtube.com/playlist?list=PL2Xy7_YZ-e9w1V2XU1EuZOaAtsGNbtJOq')

print(f"Downloading : {py.title}")

for video in py.videos:
    video.streams.first().download()
