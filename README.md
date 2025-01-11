# 🚗 Object Detection with Distance & Speed Calculation

This project utilizes YOLOv5 (a state-of-the-art object detection model) for real-time object detection from a video stream. It calculates the distance and speed of detected objects based on their pixel width and camera parameters. It also provides an alert when an object comes too close to the camera.

![Object Detection Demo](https://media.giphy.com/media/3o7btNq0nRclXyOM3O/giphy.gif)

## 🧑‍💻 Overview

This program takes a video file as input, detects objects using YOLO, calculates their distance from the camera, and estimates their speed. If an object is detected to be within a dangerous proximity (less than 5 meters), it triggers a warning sound. 

## ⚙️ Features

- **Real-time Object Detection** using YOLO model (`yolo11l.pt`)
- **Distance Calculation** in meters based on object size and camera parameters
- **Speed Estimation** based on object movement between frames
- **Proximity Alert** with sound when an object is too close
- **Adjustable Video Input** for different sources (file or camera)

## 🛠️ Requirements

- Python 3.x
- OpenCV
- YOLO model (weights file: `yolo11l.pt`)
- `ultralytics` package for YOLOv5

### Install the necessary libraries:
```bash
pip install opencv-python ultralytics

🎥 How It Works
The program works by processing each frame of the video in real-time:

Frame Capture: The video is read frame by frame.
YOLO Detection: Objects are detected in each frame using the YOLOv5 model.
Distance Calculation: Using the width of the object in pixels, the program calculates the real-world distance.
Speed Estimation: The program estimates the speed of objects based on the change in position between consecutive frames.
Proximity Alert: If an object is within 5 meters, a warning is displayed and a sound alert is triggered.
📽️ Example Video
Here is a demo of the object detection in action:


🏁 Getting Started
To run the script, use the following steps:

Download YOLO Weights: Download the model weights file (yolo11l.pt) from the official YOLO repository or your preferred model source.
Modify the Input Path: Update the video input path in the code:
python
Copy code
cap = cv2.VideoCapture("path_to_your_video.mp4")
Run the Script:
bash
Copy code
python object_detection_speed.py
Press 'q' to exit the video stream.
🧑‍🤝‍🧑 Collaborate
If you want to contribute to this project, feel free to open an issue or submit a pull request.

Contributors: Najeeb Ullah
💬 Contact
Email: najeebullah5502@gmail.com
GitHub: https://github.com/najeebullah3124
🚀 Future Enhancements
Add real-time webcam detection.
Improve object tracking for speed accuracy.
Integrate with other ML models for more advanced object detection.
Implement a user-friendly GUI for ease of use.



### Explanation of Sections:

1. **Project Overview**: A brief introduction to what your code does.
2. **Features**: Highlights the main features and functionality of the project.
3. **Requirements**: Lists all necessary libraries and dependencies.
4. **How It Works**: Explains the flow of the code and how the video is processed.
5. **Getting Started**: Instructions on how to run the project, including installing dependencies and running the script.
6. **Example Video**: A GIF showing the detection process in action. (Replace the links with your actual GIF or demo).
7. **Collaborate**: Encourages others to contribute to your project.
8. **Future Enhancements**: Potential improvements and features to add in the future.

---

Let me know if you need any further customization! 😊
