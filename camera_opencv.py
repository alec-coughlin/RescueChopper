from ultralytics import YOLO
import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
from ultralytics.yolo.utils.plotting import Annotator

model = YOLO('yolov8n.pt')

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cap.isOpened():
    ret, frame = cap.read()
    
    # Make detections 
    results = model(frame)

    for r in results:
        
        annotator = Annotator(frame)
        
        boxes = r.boxes

        for box in boxes:
            
            b = box.xyxy[0]  # get box coordinates in (top, left, bottom, right) format
            c = box.cls
            
            # Check if the detected class is 'person'
            if model.names[int(c)] == 'person':
                annotator.box_label(b, model.names[int(c)])
          
    frame = annotator.result()  
    
    cv2.imshow('YOLO', frame)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
