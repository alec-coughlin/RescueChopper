import cv2

def find_camera_index():
    camera_index = -1
    max_camera_devices = 5  # You can adjust this number based on your needs

    for i in range(max_camera_devices):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            camera_index = i
            cap.release()
            break

    return camera_index

camera_index = find_camera_index()

if camera_index == -1:
    print("Error: No camera found")
else:
    print("Camera found at index:", camera_index)
