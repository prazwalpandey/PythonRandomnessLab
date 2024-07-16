#pip install pytube
import pytube
link = input("Enter Youtube Video Url:")
yt = pytube.YouTube(link)
yt.streams.first().download()
print("Downloaded",link)