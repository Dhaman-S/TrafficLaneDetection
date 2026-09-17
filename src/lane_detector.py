import cv2
import numpy as np
import config

class LaneDetector:
    def __init__(self):
        pass

    def detect(self, cropped_edges, frame):
        # Hough Transform to detect lines
        lines = cv2.HoughLinesP(
            cropped_edges,
            rho=config.HOUGH_RHO,
            theta=config.HOUGH_THETA,
            threshold=config.HOUGH_THRESHOLD,
            minLineLength=config.HOUGH_MIN_LINE_LEN,
            maxLineGap=config.HOUGH_MAX_LINE_GAP
        )
        
        left_lines, right_lines = self._separate_lines(lines, frame.shape[1])
        
        left_lane = self._average_lines(frame, left_lines)
        right_lane = self._average_lines(frame, right_lines)
        
        return left_lane, right_lane

    def _separate_lines(self, lines, width):
        left_lines, right_lines = [], []
        if lines is None:
            return left_lines, right_lines
            
        for line in lines:
            x1, y1, x2, y2 = line[0]
            if x2 == x1: continue # Skip vertical lines
            slope = (y2 - y1) / (x2 - x1)
            
            # Filter based on slope to separate left and right lanes
            if slope < 0 and x1 < width / 2 and x2 < width / 2:
                left_lines.append(line[0])
            elif slope > 0 and x1 > width / 2 and x2 > width / 2:
                right_lines.append(line[0])
        return left_lines, right_lines

    def _average_lines(self, frame, lines):
        if not lines:
            return None
            
        # Fit a polynomial (y = mx + b) to the lines
        x_coords, y_coords = [], []
        for x1, y1, x2, y2 in lines:
            x_coords.extend([x1, x2])
            y_coords.extend([y1, y2])
            
        poly = np.polyfit(y_coords, x_coords, 1) # Degree 1 polynomial (linear)
        
        # Calculate points for the bottom and top of the ROI
        y_bottom = frame.shape[0]
        y_top = int(frame.shape[0] * 0.6)
        
        x_bottom = int(np.polyval(poly, y_bottom))
        x_top = int(np.polyval(poly, y_top))
        
        return (x_bottom, y_bottom, x_top, y_top)
