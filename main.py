import cv2
import time
from src.preprocessor import Preprocessor
from src.lane_detector import LaneDetector
from src.traffic_detector import TrafficDetector
from src.visualizer import Visualizer

def main():
    # Initialize modules
    preprocessor = Preprocessor()
    lane_detector = LaneDetector()
    traffic_detector = TrafficDetector()
    visualizer = Visualizer()

    # Load Video (Replace with 0 for webcam)
    video_path = "data/test_video.mp4" 
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video {video_path}")
        return

    prev_time = time.time()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("End of video stream.")
            break

        # Resize for consistent processing (Optional, but recommended for performance)
        frame = cv2.resize(frame, (1280, 720))

        # 1. Preprocessing (Grayscale, Canny, ROI)
        cropped_edges = preprocessor.process(frame)

        # 2. Lane Detection (Hough Transform)
        left_lane, right_lane = lane_detector.detect(cropped_edges, frame)

        # 3. Traffic Detection (Background Subtraction & Contours)
        vehicle_count, bounding_boxes = traffic_detector.detect(frame)

        # 4. Visualization
        frame = visualizer.draw_lanes(frame, left_lane, right_lane)
        frame = visualizer.draw_traffic(frame, bounding_boxes)
        
        # Calculate FPS
        current_time = time.time()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time
        
        frame = visualizer.draw_info(frame, vehicle_count, fps)

        # Show output
        cv2.imshow("Automated Traffic & Lane Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
