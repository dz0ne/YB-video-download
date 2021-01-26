from pytube import YouTube
link = input("sami put your YB vedio url")
yt = YouTube(link)
#get video name

print("Titel :", yt.title)
#get duration 
print("duration :",yt.length)
#:)
#now let make it download with hight resolution possible
stream = yt.streams.get_highest_resolution()
stream.download()
#print if video downloaded
print("video download complite")