from pytube import YouTube

url = 'https://www.youtube.com/watch?v=464vbzc17oU'
video = YouTube(url)
print(video.title)