#Import the required Libraries
import os
from tkinter import *
from tkinter import ttk

from tqdm import tk

from webcam import webcam
from cam import cam
import random
import subprocess
def demo():
    cmd = "python3 demo.py s1/video/mpg_6000/bbaf2n.mp4"
    os.system(cmd)
    file = open("result.txt", "r+")
    result = Label(text=file.readline(), pady=100)
    result.pack(side=TOP)

#file = open("result.txt", "r+")
#file.truncate()
#file.close()
def player():
    cmd = "python3 players.py"
    os.system(cmd)

#Create an instance of Tkinter frame
win = Tk()
#Set the geometry of Tkinter frame
win.geometry("750x400")
#Define an Entry widget
#Create Buttons with proper position
button1= ttk.Button(win, text= "Webcam", command=cam,padding=10)
button1.pack(side= TOP)
button1= ttk.Button(win, text= "System file", command=player,padding=10)
button1.pack(side= TOP)
button2= ttk.Button(win, text= "Result", command=demo,padding=10)
button2.pack(side=TOP)
label= Label(text = "Output",pady=100)
label.pack(side=TOP)


win.mainloop()