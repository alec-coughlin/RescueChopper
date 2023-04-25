import cv2
import imutils

# Initialize the HOG descriptor for human detection
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Initialize video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Resize the frame to reduce computation time
    frame = imutils.resize(frame, width=min(400, frame.shape[1]))

    # Detect humans in the frame
    (rects, weights) = hog.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.05)

    # Draw bounding boxes around detected humans
    for (x, y, w, h) in rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show the video with detections
    cv2.imshow("Human Detection", frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
