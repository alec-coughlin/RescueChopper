import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Unable to open the camera")
    exit(1)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Unable to read a frame from the camera")
        break

    cv2.imshow("Frame", frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
