playsound('s1/video/mpg_6000/my_result.mp3')
def play():
    my_clip = mp.VideoFileClip(r"s1/video/mpg_6000/bbae8n.mpg")
    my_clip.audio.write_audiofile(r"s1/video/mpg_6000/my_result.mp3")