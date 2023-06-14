from picamera2 import PiCamera2
from ultralytics import YOLO
import cv2
import numpy as np

model = YOLO("yolov8n.onnx")

with PiCamera2(resolution=(480, 480), framerate=30) as camera:
    output = np.empty((480, 480, 3), dtype=np.uint8)
    while True:
        camera.capture(output, 'bgr')
        frame = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

        results = model(frame)

        # Uncomment the following lines if you want to process the results
        #for r in results:
        #   boxes = r.boxes  # Boxes object for bbox outputs
        #   probs = r.probs  # Class probabilities for classification outputs
        #   print(boxes.xyxy[0])  # print img1 predictions (pixels)

        #cv2.imshow("frame", frame)

        if (cv2.waitKey(30) & 0xFF == 27):  # break with escape key
            break
