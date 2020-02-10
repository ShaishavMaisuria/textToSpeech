from gtts import gTTS
import os
from pydub import AudioSegment



def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
         "frame_rate": int(sound.frame_rate * speed)
      })
     # convert the sound with altered frame rate to a standard frame rate
     # so that regular playback programs will work right. They often only
     # know how to play audio at standard frame rate (like 44.1k)
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)



mytext = 'Welcome to geeksforgeeks!'

file1 = open("MyFile.txt","r",encoding='latin-1')




print( "reading the file")
mytext=file1.read()
#language used for converting
language_preference = 'en'
speed=False # helps to determine the fast pace for true and false for slow pace
myobj = gTTS(text=str(mytext), lang=str(language_preference), slow=True)
sound_pace_audio=0.75

audio_file="cptr1.mp3"
myobj.save(audio_file)

soundnote = AudioSegment.from_file(audio_file)
sound_slow = speed_change(soundnote, sound_pace_audio)


os.system(audio_file)

file1.close()