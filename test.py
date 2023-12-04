#ffmpeg -i /home/usama/PycharmProjects/LipNet-PyTorch/s1/video/mpg_6000/bbaf2n.mp4
#-c:v libx264 -crf 18 -preset veryslow -c:a copy /home/usama/PycharmProjects/LipNet-PyTorch/s1/video/mpg_6000/bbaf2n.mp4
import os

os.remove('/home/usama/PycharmProjects/LipNet-PyTorch/s1/video/mpg_6000/output.mp4')