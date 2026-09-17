import cv2
import numpy as np
import config

class TrafficDetector:
    def __init__(self):
        # Background Subtraction (Segmentation)
        self.bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=True)
        
    def detect(self, frame):
        # Apply background subtractor to isolate moving vehicles
        mask = self.bg_subtractor.apply(frame)
        
        # Morphological Operations (Module 4: Opening and Closing)
        # Remove noise (opening) and fill holes (closing)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
        # Find contours for moving objects
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        vehicle_count = 0
        bounding_boxes = []
        
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > config.MIN_CONTOUR_AREA:
                x, y, w, h = cv2.boundingRect(contour)
                bounding_boxes.append((x, y, w, h))
                vehicle_count += 1
                
        return vehicle_count, bounding_boxes
