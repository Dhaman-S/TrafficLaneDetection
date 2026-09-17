# main.py

import cv2
import time
from src.preprocessor import Preprocessor
from src.lane_detector import LaneDetector
from src.traffic_detector import TrafficDetector
from src.visualizer import Visualizer
from data import get_video_path  # Import our new utility function

# Set to 1 to process every frame. Set to 2 or 3 if the video is too large/heavy.
FRAME_SKIP = 1 

def main():
    # Initialize modules
    preprocessor = Preprocessor()
    lane_detector = LaneDetector()
    traffic_detector = TrafficDetector()
    visualizer = Visualizer()

    # 1. Get the absolute path to the MP4 file
    try:
        video_path = get_video_path("test_video.mp4")
        print(f"Loading video from: {video_path}")
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        return

    # 2. Load the compressed MP4 Video
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: OpenCV could not open the video file. It might be corrupted or using an unsupported codec.")
        return

    # 3. Print Video Metadata (Helpful for debugging compressed videos)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps_video = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    print(f"Video Loaded Successfully!")
    print(f"Resolution: {width}x{height}")
    print(f"Video FPS: {fps_video:.2f}")
    print(f"Total Frames: {total_frames}")
    print("Press 'q' to quit the video window.\n")

    prev_time = time.time()
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("End of video stream.")
            break

        frame_count += 1
        
        # Skip frames if specified (helps with heavy compressed videos)
        if frame_count % FRAME_SKIP != 0:
            continue

        # Resize for consistent processing (Standardize to 1280x720)
        # This is important because your config.py ROI_VERTICES are set for 1280x720
        frame = cv2.resize(frame, (1280, 720))

        # 1. Preprocessing (Grayscale, Histogram Equalization, Canny, ROI)
        cropped_edges = preprocessor.process(frame)

        # 2. Lane Detection (Hough Transform)
        left_lane, right_lane = lane_detector.detect(cropped_edges, frame)

        # 3. Traffic Detection (Background Subtraction & Contours)
        vehicle_count, bounding_boxes = traffic_detector.detect(frame)

        # 4. Visualization
        frame = visualizer.draw_lanes(frame, left_lane, right_lane)
        frame = visualizer.draw_traffic(frame, bounding_boxes)
        
        # Calculate FPS of our processing pipeline
        current_time = time.time()
        processing_fps = 1 / (current_time - prev_time)
        prev_time = current_time
        
        frame = visualizer.draw_info(frame, vehicle_count, processing_fps)

        # Show output
        cv2.imshow("Automated Traffic & Lane Detection", frame)

        # Press 'q' to exit early
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Video processing complete.")

if __name__ == "__main__":
    main()
