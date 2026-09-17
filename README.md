# Automated Traffic & Lane Detection
A Computer Vision project utilizing OpenCV and Python to detect lane lines and count vehicles in real-time video feeds.

## Features
- Lane detection using Canny Edge Detection and Hough Transform.
- Vehicle counting using Background Subtraction (MOG2) and Contour detection.
- Real-time FPS monitoring and visual overlays.

## Technologies Used
- Python 3.8+
- OpenCV (cv2)
- NumPy

## Installation & Setup
1. Clone the repository: `git clone https://github.com/yourusername/TrafficLaneDetection.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Place a dashcam video in the `data/` folder and name it `test_video.mp4`.
4. Run the project: `python main.py`

## Testing
- Run `pytest tests/` to execute unit tests for image preprocessing.
