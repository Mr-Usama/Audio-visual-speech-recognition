import os
from tkinter import *
from PIL import Image, ImageTk
import cv2
from tkVideoPlayer import TkinterVideo
from cv2 import VideoWriter, VideoWriter_fourcc
from tkvideo import tkvideo
import players
from time import sleep
import tkinter as tk
from tkinter import messagebox
win = Tk()
win.attributes('-zoomed', True)
# Set the size of the window
win.geometry("700x350")
# the label for user_name
user_name = Label(win,
                     text="Instructions",font='Helvetica 18 bold',bg="#FFFF00").place(x=320,
                                            y=10)
user_name = Label(win,
                     text="""
                     Start the Webcam and speak. Press Esc key when done.
                     
                     
                     Play the recording to check if you like the video. if you don't, record again.
                     
                     
                     Click 'TestModel' when you want to test it.
                     
                     
                     Wait for the model to display its predictions.
                     
                     
                     It might take a while usually around 5 6 mins.
                     """
                  ,font='Helvetica 12 bold').place(x=40,
                                            y=50)
# Create a Label to capture the Video frames
label =Label(win)
label.place(x=20,y=40)
cam_on = False
cap = None
player=None
#cap= cv2.VideoCapture(0)
video = VideoWriter('/home/usama/PycharmProjects/LipNet-PyTorch/s1/video/mpg_6000/bbaf2n.mp4',
                        VideoWriter_fourcc(*'mp4v'), 25.0, (640, 480))
#video = cv2.VideoWriter('outpy.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (640, 480))
# Define function to show frame
def show_frames():
    if cam_on:
        # Get the latest frame and convert into Image
        frame = cap.read()[1]
        cv2.imwrite('test.png',frame)
        video.write(frame)
        cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        # Convert image to PhotoImage
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.configure(image=imgtk)
        # Repeat after an interval to capture continiously
        label.after(20, show_frames)
def start_vid():
    global cam_on, cap
    stop_vid()
    cam_on = True
    #os.remove('/home/usama/PycharmProjects/LipNet-PyTorch/s1/video/mpg_6000/bbaf2n.mpg')
    cap = cv2.VideoCapture(0)
    show_frames()
def stop_vid():
    global cam_on
    cam_on = False
    if cap:
        cap.release()
def play_vid():
    cap = cv2.VideoCapture("/home/usama/PycharmProjects/LipNet-PyTorch/s1/video/mpg_6000/bbaf3s.mp4")
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if(length==0):
        messagebox.showerror("Error", "Please Record video first !")
    else:
        cmd = "python3 final_gui.py"
        os.system(cmd)
def demo():
    cap = cv2.VideoCapture("/home/usama/PycharmProjects/LipNet-PyTorch/s1/video/mpg_6000/bbaf3s.mp4")
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if (length == 0):
        messagebox.showerror("Error", "Please Record video first !")
    else:
        file = open("result.txt", "r+")
        file.truncate()
        os.remove('/home/usama/PycharmProjects/LipNet-PyTorch/s1/video/mpg_6000/bbaf2n.mp4')
        cmd1="ffmpeg -i /home/usama/PycharmProjects/LipNet-PyTorch/s1/video/mpg_6000/bbaf3s.mp4 -c:v libx264 -crf 18 -preset veryslow -c:a copy /home/usama/PycharmProjects/LipNet-PyTorch/s1/video/mpg_6000/bbaf2n.mp4"
        os.system(cmd1)
        cmd = "python3 demo.py s1/video/mpg_6000/bbaf2n.mp4"
        os.system(cmd)
        file = open("result.txt", "r+")
        print(file.readline())
def cam():
    cmd = "python3 cam.py"
    os.system(cmd)

def update():
    file = open("result.txt", "r+")
    aktTemp['text'] = file.readline()
    win.after(1000, update)  # run itself again after 1000 ms
def Close():
    win.destroy()
    cmd="python3 test_gui.py"
    os.system(cmd)
#show_frames()
btn_start = Button(win, text="Webcam",height=2,width=20,bg="#00FF00",command=cam)
btn_start.place(x=250,y=540)
btn_stop = Button(win, text="Refresh",height=2,width=20,bg="#CEF9EE",command=Close)
btn_stop.place(x=420,y=540)
user_names = Label(win,
                     text="Recording",font='Helvetica 18 bold').place(x=950,
                                            y=10)
btn_starts = Button(win, text="Play video",height=2,width=20,bg="#00FF00",command=play_vid)
btn_starts.place(x=800,y=50)

btn_starts = Button(win, text="Test Model",height=2,width=20,bg="#808080",command=demo)
btn_starts.place(x=1000,y=50)
user_name = Label(win,
                     text="Model Output:",font='Helvetica 18 bold',bg="#90ee90",height=2,width=20).place(x=800,
                                            y=270)
#file = open("result.txt", "r+")
aktTemp = tk.Label(win,text="",font='Helvetica 18 bold',bg="#90ee90",height=10,width=40)
aktTemp.place(x=800,y=330)
update()
win.mainloop()
