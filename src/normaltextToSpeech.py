from gtts import gTTS
import os


text_file_name="MyFile.txt"
#language used for converting
language_preference = 'en'
speed=True # helps to determine the fast pace for true and false for slow pace

file1 = open(str(text_file_name),"r",encoding='latin-1')

print( "reading the file")
mytext=file1.read()

myobj = gTTS(text=str(mytext), lang=str(language_preference), slow=True)

print( "making audio file")
audio_file="cptr1.mp3"
myobj.save(audio_file)
print( "saving audio file")

print( "starting audio file")
os.system(audio_file)
print( "closing the file and have a good day")
file1.close()