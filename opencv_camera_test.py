import cv2

# Define GStreamer pipeline
gst_pipeline = (
    "v4l2src device=/dev/video0 ! "
    "video/x-raw, width=640, height=480, framerate=30/1, format=UYVY ! "
    "videoconvert ! "
    "video/x-raw, format=BGR ! appsink"
)

# Initialize video capture with GStreamer pipeline
cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error capturing frame. Check camera connection.")
        break

    # Show the video
    cv2.imshow("Camera Test", frame)

    # Exit the loop when 'q'
