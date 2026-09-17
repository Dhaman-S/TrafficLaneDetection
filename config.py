# config.py

# Image Preprocessing
GAUSSIAN_BLUR_KERNEL = (5, 5)
CANNY_LOW_THRESHOLD = 50
CANNY_HIGH_THRESHOLD = 150

# Region of Interest (ROI) - Trapezoid shape focusing on the road
# These values are for a 1280x720 video. Adjust based on your video size.
ROI_VERTICES = [
    (int(1280 * 0.1), int(720 * 0.95)), # Bottom left
    (int(1280 * 0.45), int(720 * 0.6)), # Top left
    (int(1280 * 0.55), int(720 * 0.6)), # Top right
    (int(1280 * 0.9), int(720 * 0.95))  # Bottom right
]

# Hough Transform
HOUGH_RHO = 2
HOUGH_THETA = np.pi / 180
HOUGH_THRESHOLD = 50
HOUGH_MIN_LINE_LEN = 40
HOUGH_MAX_LINE_GAP = 100

# Traffic Detection
MIN_CONTOUR_AREA = 500 # Minimum area to be considered a vehicle
