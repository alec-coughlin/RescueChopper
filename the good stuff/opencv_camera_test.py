from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.onnx")

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#cap.set(cv2.CAP_PROP_FPS, 0.1)

while True:

    ret, frame = cap.read()
        
    results = model(frame)

    #for r in results:

     #   boxes = r.boxes  # Boxes object for bbox outputs
     #   probs = r.probs  # Class probabilities for classification outputs

    #print(boxes.xyxy[0])  # print img1 predictions (pixels)

    #cv2.imshow("frame", frame)

    if (cv2.waitKey(30) == 27): # break with escape key
        
        break
