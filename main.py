import cv2

# Replace with your video stream URL
video_url = 'http://192.168.137.62:8080/video'

# Open the video stream
cap = cv2.VideoCapture(video_url)

if not cap.isOpened():
    print("Error: Unable to open video stream.")
    exit()

print("Press 'q' to quit.")

while True:
    # Read a frame from the video stream
    ret, frame = cap.read()

    if not ret:
        print("Error: Unable to read frame. Stream may have ended.")
        break

    # Display the frame
    cv2.imshow('Video Stream', frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()