import pyttsx3
from playsound import playsound
from tkinter import *


engine = pyttsx3.init()

def talk():
    try:
        text = textBox.get(1.0, END)
        engine.say(text)
        engine.runAndWait()
    except Exception:
        print("error")

def stopTalking():
    engine.stop()

root = Tk()
root.title("Text To Speech")
root.geometry("800x600")

textBox = Text(root, width=80, height=23, font=("Helvetica", 12))
textBox.pack(pady=10)

speakButton = Button(root, text="Speak", command=talk)
speakButton.pack(pady=10)
stopButton = Button(root, text="Stop", command=stopTalking)
stopButton.pack(pady=15)

root.mainloop()