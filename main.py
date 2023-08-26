# Import necessary libraries
from cvzone.PoseModule import PoseDetector  # Import the PoseDetector class from cvzone module
import cv2  # Import OpenCV library

# Create a VideoCapture object to capture video from the default camera (camera index 0)
cap = cv2.VideoCapture(0)

# Create an instance of the PoseDetector class
detector = PoseDetector()

# Infinite loop to continuously process frames from the camera
while True:
    # Read a frame from the video capture
    success, img = cap.read()

    # Use the detector to find the pose (body landmarks) in the current frame
    img = detector.findPose(img)

    # Find pose landmarks and bounding box information (without hands)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False)

    # Check if bounding box information is available
    if bboxInfo:
        center = bboxInfo["center"]  # Get the center coordinates of the bounding box
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)  # Draw a filled circle at the center of the bounding box

    # Display the modified image with detected pose and bounding box information
    cv2.imshow("Image", img)

    # Check if the 'q' key is pressed to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
