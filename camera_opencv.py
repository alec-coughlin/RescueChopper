from ultralytics import YOLO
import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
from ultralytics.yolo.utils.plotting import Annotator

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

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# cap.set(cv2.CAP_PROP_FPS, 10)

while cap.isOpened():
    ret, frame = cap.read()
    
    # Make detections 
    results = model(frame)

    for r in results:
        
        annotator = Annotator(frame)
        
        boxes = r.filter(class_names=['person']).boxes

        for box in boxes:
            
            b = box.xyxy[0]  # get box coordinates in (top, left, bottom, right) format
            c = box.cls
            annotator.box_label(b, model.names[int(c)])
          
    frame = annotator.result()  
    
    cv2.imshow('YOLO', frame)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()