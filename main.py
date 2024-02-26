print("-"*31 + " loading " + "-"*31)
from pytube import YouTube 
import os
import music_tag
from moviepy.editor import VideoFileClip
from pathlib import Path

print('''
Ishaan Takrani's
              _____ 
/\_/\___  _   _| |_ _   _| |__   ___  | |_ ___    _ __ ___  _ __|___ / 
\_ _/ _ \| | | | __| | | | '_ \ / _ \ | __/ _ \  | '_ ` _ \| '_ \ |_ \ 
 / \ (_) | |_| | |_| |_| | |_) |  __/ | || (_) | | | | | | | |_) |__) |
 \_/\___/ \__,_|\__|\__,_|_.__/ \___|  \__\___/  |_| |_| |_| .__/____/ 
                                                           |_|         
v 1.3.0
      ''')


def tag(yt,base):

    tagging_dict = {
        '1':'title',
        '2':'artist',
        '3':'album',
        '4':'genre',
        '5':'year'
    }

    status = ""

    while(status != "" or status.lower() != "y" or status.lower() != "n"):

        print("-"*20)
        status = str(input("mp3 tag? (Y/n), (blank for auto-tagging)\n>> "))

        f = music_tag.load_file(base + ".mp3")

        if(status.lower() == "n"):
            return
        
        elif(status == ""): 
            f['title'] = yt.title
            f['artist'] = yt.author
            return

        elif(status.lower() == "y"):
            
            key_to_tag = -1

            while(key_to_tag != 0):

                print("-"*30)

                print("\n---------")
                for key, value in tagging_dict.items():
                    print(f"{key}: {value}")
                print("---------\n ")

                key_to_tag = str(input("Enter number key for desired tag modification (0 to exit):\n>> "))

                if(key_to_tag == "0"):
                    f.save()
                    return
                
                value_of_tag = str(input("Enter desired data\n>> "))
                
                par = tagging_dict[key_to_tag]
                f[str(par)] = value_of_tag
        
        else:
            print("invalid command, try again")
            pass

    f.save()

continue_status = True

while(continue_status):

    print("-"*20)
    yt = YouTube(str(input("Enter URL: \n>> "))) 

    print("Working...")

    if(" - ") in yt.title:
        yt.title = yt.title.split(" - ")[1]
        yt.author = yt.title.split(" - ")[0]
    
    video = yt.streams.filter().first()

    print("-"*20)
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
    os.remove(base + ".mp4")

    tag(yt,base)
    
    print("Success! Video downloaded as mp3\n--------------------------------")
    
    
    continue_status = ""

    while (continue_status.lower() != "n"):
        
        continue_status = str(input("Convert another file(Y/n)\n>> "))

        if(continue_status.lower() == "n"):
            music_phrases = [
                "Keep rocking!",
                "Stay tuned!",
                "Keep vibing!",
                "Keep jamming!",
                "Stay in sync!",
                "Stay in tune!",
                "Stay groovy!",
                "Keep bopping!",
            ]
            from random import randint
            print(music_phrases[randint(0,(len(music_phrases)-1))])
            exit()
        elif(continue_status.lower() == "y"):
            print("-"*20)
            break
        else:
            print("invalid command, try again")
    
print("-"*71)

