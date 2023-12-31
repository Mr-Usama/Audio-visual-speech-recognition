import cv2
import sys
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc

cascPath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)
video = VideoWriter('/home/usama/PycharmProjects/LipNet-PyTorch/s1/video/mpg_6000/bbaf3s.mp4',
                        VideoWriter_fourcc(*'mp4v'), 25.0, (640, 480))

while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        video.write(frame)
        # Display the resulting frame
        cv2.imshow('Video', frame)


        if cv2.waitKey(1) & 0xFF == 27: break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()



