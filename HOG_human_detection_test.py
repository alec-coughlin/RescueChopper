import cv2
import imutils

# load the serialized HOG + Linear SVM model
# this model was trained on the INRIA person dataset and can detect people in images
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# open the video stream from the Arducam
cap = cv2.VideoCapture(0)

# continuously process frames from the video stream
while True:
    # read a frame from the video stream
    r, frame = cap.read()
    if r:
        # resize the frame to reduce processing time
        frame = imutils.resize(frame, width=min(400, frame.shape[1]))
        
        # detect people in the frame
        # this returns a list of bounding boxes for detected people
        (boxes, weights) = hog.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.05)
        
        # draw the bounding boxes
        for (x, y, w, h) in boxes:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        
        # show the output frame
        cv2.imshow("output", frame)
    
    # if the 'q' key is pressed, break from the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# clean up
cv2.destroyAllWindows()
cap.release()
