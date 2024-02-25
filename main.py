print("-----------------------------------------------------------------------")
from pytube import YouTube 
import os
import music_tag
from moviepy.editor import VideoFileClip
from pathlib import Path

print('''
              _____ 
/\_/\___  _   _| |_ _   _| |__   ___  | |_ ___    _ __ ___  _ __|___ / 
\_ _/ _ \| | | | __| | | | '_ \ / _ \ | __/ _ \  | '_ ` _ \| '_ \ |_ \ 
 / \ (_) | |_| | |_| |_| | |_) |  __/ | || (_) | | | | | | | |_) |__) |
 \_/\___/ \__,_|\__|\__,_|_.__/ \___|  \__\___/  |_| |_| |_| .__/____/ 
                                                           |_|         
v 1.1
      ''')

yt = YouTube(str(input("Enter URL: \n>> "))) 

print("Working...")

if(" - ") in yt.title:
    yt.title = yt.title.split(" - ")[1]
  
video = yt.streams.filter().first()

inp_path = str(input("Enter Directory (curr for current directory, empty for default music directory): \n>> "))

if (inp_path == "curr"):
    destination = str('.')
elif (inp_path == ''):
    destination = str(Path.home() / "Music")
else:
    destination = str(rf'{inp_path}')

out_file = video.download(output_path=destination) 

base, _ = os.path.splitext(out_file)
new_file = base + '.mp4'
os.rename(out_file, new_file)

video = VideoFileClip(base + ".mp4")
video.audio.write_audiofile(base + ".mp3")
video.close()

file_path = new_file
f = music_tag.load_file(base + ".mp3")
f["title"] = yt.title
f['artist'] = yt.author


f.save()
print("Success! Video downloaded as mp3")


try:
    os.remove(base + ".mp4")
except OSError as e:
    print(f"Error deleting original MP4 file: {e}")

