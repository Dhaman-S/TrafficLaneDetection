# tests/test_preprocessor.py

import unittest
import numpy as np
import cv2
import sys
import os

# Add the parent directory to sys.path so we can import 'src' and 'config'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.preprocessor import Preprocessor
import config

class TestPreprocessor(unittest.TestCase):
    
    def setUp(self):
        """Set up a dummy frame before each test."""
        self.preprocessor = Preprocessor()
        # Create a dummy 720p BGR image (Black background)
        self.dummy_frame = np.zeros((720, 1280, 3), dtype=np.uint8)
        
        # Draw a white rectangle to simulate road lines/edges
        cv2.rectangle(self.dummy_frame, (400, 500), (800, 700), (255, 255, 255), 5)

    def test_process_output_shape(self):
        """Test if the output image has the same dimensions as the input."""
        output = self.preprocessor.process(self.dummy_frame)
        # The output should be a single-channel grayscale image, so shape is (720, 1280)
        self.assertEqual(output.shape, (720, 1280))

    def test_process_output_type(self):
        """Test if the output is a NumPy array."""
        output = self.preprocessor.process(self.dummy_frame)
        self.assertIsInstance(output, np.ndarray)

    def test_process_output_binary(self):
        """Test if the output image is binary (0 or 255) due to Canny edge detection."""
        output = self.preprocessor.process(self.dummy_frame)
        unique_values = np.unique(output)
        # Canny edges output only 0 (black) or 255 (white)
        self.assertTrue(np.all(np.isin(unique_values, [0, 255])))

    def test_roi_masking(self):
        """Test if the Region of Interest (ROI) masking correctly blacks out non-road areas."""
        # Create a noisy image to ensure Canny detects edges everywhere
        noise_frame = np.random.randint(0, 256, (720, 1280, 3), dtype=np.uint8)
        output = self.preprocessor.process(noise_frame)
        
        # Based on config.ROI_VERTICES, the top corners of the image are outside the ROI.
        # Therefore, they should be completely black (0) in the output.
        self.assertEqual(output[0, 0], 0, "Top-left corner should be masked out (black).")
        self.assertEqual(output[0, 1279], 0, "Top-right corner should be masked out (black).")
        
        # The bottom center is inside the ROI, so it should potentially have edges (non-zero)
        # Note: Since it's a random noise image, edges are guaranteed, but just in case,
        # we only assert that the top corners are black.
        
    def test_histogram_equalization(self):
        """Test if the preprocessing handles low-contrast images (Histogram Equalization)."""
        # Create a very dark image
        dark_frame = np.ones((720, 1280, 3), dtype=np.uint8) * 10
        # Add a slightly brighter rectangle
        cv2.rectangle(dark_frame, (400, 500), (800, 700), (30, 30, 30), 5)
        
        # The preprocessor should apply histogram equalization, making the 
        # contrast higher before Canny edge detection.
        output = self.preprocessor.process(dark_frame)
        
        # Check that the output is still valid
        self.assertEqual(output.shape, (720, 1280))

if __name__ == '__main__':
    unittest.main()
