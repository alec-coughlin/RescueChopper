from ultralytics import YOLO
import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
from ultralytics.yolo.utils.plotting import Annotator

# Load a pretrained YOLO model (recommended for training)
model = YOLO('yolov8n.pt')

# Get the class index for 'person'
person_idx = model.names.index('person')

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    
    # Resize the frame for faster processing
    frame = cv2.resize(frame, (416, 416))  # Resize to whatever size fits your need
    
    # Make detections 
    results = model(frame)

    annotator = Annotator(frame)
    
    # Get only person detections
    person_detections = [r for r in results if r.cls == person_idx]

    for pd in person_detections:
        b = pd.boxes[0].xyxy[0]  # get box coordinates in (top, left, bottom, right) format
        annotator.box_label(b, model.names[int(pd.cls)])

    frame = annotator.result()  
    
    cv2.imshow('YOLO', frame)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
