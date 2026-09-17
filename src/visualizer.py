import cv2

class Visualizer:
    def __init__(self):
        pass

    def draw_lanes(self, frame, left_lane, right_lane):
        overlay = frame.copy()
        if left_lane:
            cv2.line(overlay, (left_lane[0], left_lane[1]), (left_lane[2], left_lane[3]), (0, 255, 0), 10)
        if right_lane:
            cv2.line(overlay, (right_lane[0], right_lane[1]), (right_lane[2], right_lane[3]), (0, 255, 0), 10)
            
        # Blend the overlay with the original frame for transparency
        cv2.addWeighted(overlay, 0.8, frame, 0.2, 0, frame)
        return frame

    def draw_traffic(self, frame, bounding_boxes):
        for (x, y, w, h) in bounding_boxes:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        return frame

    def draw_info(self, frame, vehicle_count, fps):
        cv2.putText(frame, f"Vehicles: {vehicle_count}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(frame, f"FPS: {fps:.2f}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
        return frame
