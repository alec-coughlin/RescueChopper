import cv2

# Initialize video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error capturing frame. Check camera connection.")
        break

    # Show the video
    cv2.imshow("Camera Test", frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
