import cv2

for i in range(16):
    cap = cv2.VideoCapture(f"v4l2src device=/dev/video{i} ! videoconvert ! appsink", cv2.CAP_GSTREAMER)
    ret, frame = cap.read()
    if ret:
        print(f"Camera found at /dev/video{i}")
        break
    cap.release()
