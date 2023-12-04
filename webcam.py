import cv2
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc

def webcam():
    # open the webcam video stream
    webcam = cv2.VideoCapture(0)

    # open output video file stream
    video = VideoWriter('/home/usama/PycharmProjects/LipNet-PyTorch/s1/video/mpg_6000/bbaf2n.mp4',
                        VideoWriter_fourcc(*'mp4v'), 25.0, (640, 480))

    # main loop
    while True:
        # get the frame from the webcam
        stream_ok, frame = webcam.read()

        # if webcam stream is ok
        if stream_ok:
            # display current frame
            cv2.imshow('Webcam', frame)

            # write frame to the video file
            video.write(frame)

        # escape condition
        if cv2.waitKey(1) & 0xFF == 27: break

    # clean ups
    cv2.destroyAllWindows()

    # release web camera stream
    webcam.release()

    # release video output file stream
    video.release()

