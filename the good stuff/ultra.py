from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.onnx")
model.predict(source = 0, show = True)
