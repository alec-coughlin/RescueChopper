# import the opencv library
import cv2
from picamera2 import Picamera2
from ultralytics import YOLO
import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
from ultralytics.yolo.utils.plotting import Annotator

# define a video capture object

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()


# Create a new YOLO model from scratch
#model = YOLO('yolov8n.yaml')

# Load a pretrained YOLO model (recommended for training)
model = YOLO('yolov8n.pt')

# Train the model using the 'coco128.yaml' dataset for 3 epochs
#model.train(data='coco128.yaml', epochs=2)

# Evaluate the model's performance on the validation set
#results = model.val()

# Perform object detection on an image using the model
#results = model('https://ultralytics.com/images/bus.jpg')

# Export the model to ONNX format
#success = model.export(format='onnx')
im = picam2.capture_array()

while True:
    ret, frame = im.read()
    
    # Make detections 
    results = model(frame)

    for r in results:
        
        annotator = Annotator(frame)
        
        boxes = r.boxes

        for box in boxes:
            
            b = box.xyxy[0]  # get box coordinates in (top, left, bottom, right) format
            c = box.cls
            annotator.box_label(b, model.names[int(c)])
          
    frame = annotator.result()  
    
    cv2.imshow('YOLO', frame)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
