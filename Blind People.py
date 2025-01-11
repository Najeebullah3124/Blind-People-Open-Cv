import cv2
from ultralytics import YOLO
import winsound
import time
model=YOLO("yolo11l.pt").to("cuda")
cap = cv2.VideoCapture("C:/Users/Najeeb ULLAH/Downloads/3318088-hd_1920_1080_25fps.mp4")

if cap.isOpened():
    print("Successfully Opened")
else:
    print("Failed to open video file")
    exit()


desired_width = 1280
desired_height = 720

KNOWN_WIDTH = 200.0  
FOCAL_LENGTH_MM = 24  
SENSOR_WIDTH_MM = 6.4  
IMAGE_WIDTH_PIXELS = 1920  

model = YOLO("yolo11l.pt").to("cuda")  

cv2.namedWindow("Blind", cv2.WINDOW_NORMAL)

# Initialize the previous time for speed calculation
prev_time = time.time()

while True:
    success, img = cap.read()

    if not success:
        print("Failed to read frames or End of Video")
        break

    print("Frames read successfully")

    img = cv2.resize(img, (desired_width, desired_height))

    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
            conf = box.conf[0].cpu().numpy()
            cls = int(box.cls[0].cpu().numpy())

            pixel_width = x2 - x1

            focal_length_pixels = (FOCAL_LENGTH_MM * IMAGE_WIDTH_PIXELS) / SENSOR_WIDTH_MM

            if pixel_width > 0:  
                real_distance = (KNOWN_WIDTH * focal_length_pixels) / pixel_width
                real_distance = real_distance / 1000  # Convert to meters
            else:
                real_distance = 0

            # Calculate speed based on delta time between frames
            current_time = time.time()
            deltatime = current_time - prev_time  # Time between current and previous frame

            if deltatime > 0:  # Avoid division by zero
                speed = real_distance / deltatime  # Speed in meters per second
            else:
                speed = 0

            # Update previous time for the next frame
            prev_time = current_time

            label = f"Distance: {real_distance:.2f} m, Speed: {speed:.2f} m/s, {model.names[cls]}:"

            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
            cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 1)

            # Warn if the object is too close
            if real_distance <= 5:
                cv2.putText(img, f'Warning: Object is near! (Distance: {real_distance:.2f} m)', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 3)
                winsound.Beep(1000, 500)  # Beep alert

    cv2.imshow("Blind", img)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
