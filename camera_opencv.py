import cv2
import numpy as np
from picamera import PiCamera
from picamera.array import PiRGBArray
from time import sleep

# Initialize the camera
camera = PiCamera()
camera.resolution = (640, 480)  # You can set your desired resolution here
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# Allow the camera to warm up
sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # Get the NumPy array representing the image
    image = frame.array

    # Display the image using OpenCV
    cv2.imshow("Frame", image)

    # Clear the stream to prepare for the next frame
    rawCapture.truncate(0)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Close all OpenCV windows
cv2.destroyAllWindows()
