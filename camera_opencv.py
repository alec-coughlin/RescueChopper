import cv2

# Load the captured image
image = cv2.imread('test_image.jpg')

if image is None:
    print("Error: Unable to load the image")
else:
    # Perform any desired processing here
    # For example, you can convert the image to grayscale:
    # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the image
    cv2.imshow('Captured Image', image)

    # Wait for a keypress and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
