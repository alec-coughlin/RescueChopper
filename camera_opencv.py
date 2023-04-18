import cv2

# Set the camera device path, replace /dev/video0 if needed
camera_device = "/dev/video0"

# Open the camera
cap = cv2.VideoCapture(camera_device)

if not cap.isOpened():
    print("Error: Unable to open the camera")
    exit(1)

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    if not ret:
        print("Error: Unable to read a frame from the camera")
        break

    # Display the captured frame
    cv2.imshow("Frame", frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
