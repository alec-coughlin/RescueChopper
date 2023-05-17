# import the opencv library
import cv2


# define a video capture object
vid = cv2.VideoCapture('v4l2src device=/dev/video0 ! videoscale ! video/x-raw,width=640,height=480 ! videoconvert ! appsink', cv2.CAP_GSTREAMER)


while(True):
	
	# Capture the video frame
	# by frame
	ret, frame = vid.read()

	# Display the resulting frame
	cv2.imshow('frame', frame)
	
	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
