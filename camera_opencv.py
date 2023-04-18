import cv2

camera_index = 0
cap = cv2.VideoCapture(camera_index)

if not cap.isOpened():
    print("Error: Unable to open the camera")
else:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if the frame is valid
        if not ret:
            print("Error: Unable to read a frame from the camera")
            break

        # Display the frame
        cv2.imshow('Camera Feed', frame)

        # Exit the loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()
