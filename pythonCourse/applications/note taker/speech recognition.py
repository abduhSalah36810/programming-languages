# importing the libraries 

from gkeepapi.node import Note
import speech_recognition as sr 
import os , gkeepapi 
import datetime 

# intializing the recognizer 

rec = sr.Recognizer()
run = True
# audio source 


with sr.Microphone() as source : 
        
        # listing : 

        print("recording : ....")
        audio = rec.listen(source)
        
        # coverting to text : 

        try: 
            text = rec.recognize_google(audio) 
            print(text)

        except :
            
            print("voice isn't clear")


file = open("D:/python course/applications/notes.txt" , "a")
file.write(f"{text}")


# defining the email and password  :

email = "nanab9446@gmail.com"
password = "01126293880@"

keep = gkeepapi.Keep()
keep.login(email,password)
note = keep.createNote('TEST', text)
note.pinned = True
note.color = gkeepapi.node.ColorValue.Red
keep.sync()


#https://accounts.google.com/b/0/DisplayUnlockCaptcha 

