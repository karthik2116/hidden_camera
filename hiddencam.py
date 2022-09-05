
import cv2
import logging as log
import datetime as dt
from time import sleep

video_capture = cv2.VideoCapture(0)
anterior = 0

while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()

   

    # Display the resulting frame
    cv2.imshow('Video', frame)
    currentframe = 0

    while (True):
        sleep(5)  # take schreenshot every 5 seconds
        # reading from frame
        ret, frame = video_capture.read()

        if ret:
            # if video is still left continue creating images
            name = 'frame' + str(currentframe) + '.jpg'
            print('Creating...' + name)

            # writing the extracted images
            cv2.imwrite(name, frame)

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Display the resulting frame
    cv2.imshow('Video', frame)

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
