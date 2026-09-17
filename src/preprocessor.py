import cv2
import numpy as np
import config

class Preprocessor:
    def __init__(self):
        pass

    def process(self, frame):
        # 1. Convert to Grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # 2. Histogram Equalization (Module 2: Image Enhancement)
        # Helps with low-light or high-contrast dashcam footage
        gray = cv2.equalizeHist(gray)
        
        # 3. Gaussian Blur (Module 2: Removing Noise)
        blur = cv2.GaussianBlur(gray, config.GAUSSIAN_BLUR_KERNEL, 0)
        
        # 4. Canny Edge Detection (Module 3: Edge Detection)
        edges = cv2.Canny(blur, config.CANNY_LOW_THRESHOLD, config.CANNY_HIGH_THRESHOLD)
        
        # 5. Region of Interest (ROI) Masking (Module 2: Image Transformation)
        mask = np.zeros_like(edges)
        cv2.fillPoly(mask, [np.array(config.ROI_VERTICES)], 255)
        cropped_edges = cv2.bitwise_and(edges, mask)
        
        return cropped_edges
