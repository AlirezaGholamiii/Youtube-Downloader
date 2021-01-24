import pafy
x = 0 
url = "https://www.youtube.com/watch?v=KxT0MMlH1lY"

video = pafy.new(url)

streams = video.streams

print("\n\nAll the available qualities :\n")
for i in streams:
    x += 1
    print(x,i,"\n")

best = video.getbest()

print("The best one :\n")
print(best.resolution, best.extension)

best.download(filepath="C:/Users/kasra/Downloads/Video")
print("\t\tVideo downloaded successfully")