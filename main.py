import cv2
import train
import threading
import helper

# Replace with your video stream URL
video_url = 'http://192.168.137.230:8080/video'

frame_count = 0
save_interval = 30  # Save every 30 frames

# Open the video stream
cap = cv2.VideoCapture(video_url)

def train_model(file_path):

    helper.generate(file_path)  # Make sure this function works independently

if not cap.isOpened():
    print("Error: Unable to open video stream.")
    exit()

print("Press 'q' to quit.")

threading.Thread(target=train_model, args=("frame.jpg",), daemon=True).start()

while True:
    # Read a frame from the video stream
    ret, frame = cap.read()

    if not ret:
        print("Error: Unable to read frame. Stream may have ended.")
        break
    
    _, jpeg_image = cv2.imencode('.jpg', frame)
    
    frame_count += 1
    if frame_count % save_interval == 0:  # Save only every 30th frame
        _, jpeg_image = cv2.imencode('.jpg', frame)
        with open("frame.jpg", "wb") as f:
            f.write(jpeg_image.tobytes())

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()